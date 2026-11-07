from django.contrib import admin

from .models import Appointment, TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
  list_display = ['doctor', 'date', 'start_time', 'is_booked']
  list_filter = ['is_booked', 'doctor__clinic', 'doctor']
  search_fields = ['doctor__name']
  date_hierarchy = 'date'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
  list_display = ['patient', 'time_slot', 'reason', 'status', 'created_at']
  list_filter = ['status', 'reason']
  search_fields = ['patient__username', 'time_slot__doctor__name']
  # Clinic staff mark visits as completed right from the list.
  list_editable = ['status']
  autocomplete_fields = ['patient', 'time_slot']
