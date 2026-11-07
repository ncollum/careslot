from django.contrib.auth.models import User
from django.db import models


class TimeSlot(models.Model):
  doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='time_slots')
  date = models.DateField()
  start_time = models.TimeField()
  is_booked = models.BooleanField(default=False)

  class Meta:
    ordering = ['date', 'start_time']
    constraints = [
      models.UniqueConstraint(fields=['doctor', 'date', 'start_time'], name='unique_doctor_date_time'),
    ]

  def __str__(self):
    return f'{self.doctor} - {self.date} {self.start_time:%H:%M}'


class Appointment(models.Model):
  class Reason(models.TextChoices):
    NEW_CONCERN = 'new_concern', 'New symptom or concern'
    FOLLOW_UP = 'follow_up', 'Follow-up visit'
    PRESCRIPTION = 'prescription', 'Prescription renewal'
    CHECK_UP = 'check_up', 'General check-up'
    OTHER = 'other', 'Other'

  class Status(models.TextChoices):
    BOOKED = 'booked', 'Booked'
    CANCELLED = 'cancelled', 'Cancelled'
    COMPLETED = 'completed', 'Completed'

  patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
  # ForeignKey and not OneToOne, so a slot can be booked again after a cancellation.
  time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, related_name='appointments')
  reason = models.CharField(max_length=20, choices=Reason.choices)
  details = models.TextField(blank=True)
  status = models.CharField(max_length=10, choices=Status.choices, default=Status.BOOKED)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-time_slot__date', '-time_slot__start_time']

  def __str__(self):
    return f'{self.patient.username} with {self.time_slot}'
