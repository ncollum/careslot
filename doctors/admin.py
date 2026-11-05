from django.contrib import admin

from .models import Clinic, Doctor, Language, Specialty


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
  list_display = ['name', 'address', 'phone']
  search_fields = ['name', 'address']


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
  list_display = ['name', 'icon']
  search_fields = ['name', 'keywords']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
  search_fields = ['name']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
  list_display = ['name', 'specialty', 'clinic']
  list_filter = ['specialty', 'clinic', 'languages']
  search_fields = ['name', 'bio']
  filter_horizontal = ['languages']
