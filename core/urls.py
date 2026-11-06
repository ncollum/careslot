from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
  # Placeholder until the real home page view is built
  path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
]
