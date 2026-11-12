from django import forms

from .models import Clinic, Language, Specialty


class DoctorSearchForm(forms.Form):
  q = forms.CharField(
    label='Name or symptom',
    required=False,
    widget=forms.SearchInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Chen, rash, back pain'}),
  )


class DoctorFilterForm(forms.Form):
  specialty = forms.ModelChoiceField(
    queryset=Specialty.objects.all(),
    required=False,
    empty_label='All specialties',
    widget=forms.Select(attrs={'class': 'form-select'}),
  )
  clinic = forms.ModelChoiceField(
    queryset=Clinic.objects.all(),
    required=False,
    empty_label='All clinics',
    widget=forms.Select(attrs={'class': 'form-select'}),
  )
  language = forms.ModelChoiceField(
    queryset=Language.objects.all(),
    required=False,
    empty_label='Any language',
    label='Language spoken',
    widget=forms.Select(attrs={'class': 'form-select'}),
  )
