from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.views.generic import ListView

from .forms import DoctorFilterForm, DoctorSearchForm
from .models import Doctor


class DoctorListView(ListView):
  model = Doctor
  paginate_by = 6

  def get_queryset(self):
    doctors = Doctor.objects.select_related('specialty', 'clinic').prefetch_related('languages')

    self.search_form = DoctorSearchForm(self.request.GET)
    self.filter_form = DoctorFilterForm(self.request.GET)
    # A bad value in the URL is left out instead of causing an error
    self.search_form.is_valid()
    self.filter_form.is_valid()

    self.q = self.search_form.cleaned_data.get('q', '').strip()
    specialty = self.filter_form.cleaned_data.get('specialty')
    clinic = self.filter_form.cleaned_data.get('clinic')
    language = self.filter_form.cleaned_data.get('language')

    if self.q:
      doctors = doctors.filter(
        Q(name__icontains=self.q) | Q(specialty__name__icontains=self.q) | Q(specialty__keywords__icontains=self.q)
      )
    if specialty:
      doctors = doctors.filter(specialty=specialty)
    if clinic:
      doctors = doctors.filter(clinic=clinic)
    if language:
      doctors = doctors.filter(languages=language)

    if self.q or specialty or clinic or language:
      self.request.session['last_search'] = {
        'q': self.q,
        'specialty': specialty.pk if specialty else None,
        'clinic': clinic.pk if clinic else None,
        'language': language.pk if language else None,
      }

    return doctors

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['search_form'] = self.search_form
    context['filter_form'] = self.filter_form
    context['q'] = self.q
    # Page links keep the search and filters, so drop the old page number
    query = self.request.GET.copy()
    query.pop('page', None)
    context['query_string'] = query.urlencode()
    return context
