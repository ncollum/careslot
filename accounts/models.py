from django.contrib.auth.models import User
from django.db import models


class PatientProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  phone = models.CharField(max_length=20)
  date_of_birth = models.DateField(null=True, blank=True)
  photo = models.ImageField(upload_to='profiles/', blank=True)

  class Meta:
    ordering = ['user__username']

  def __str__(self):
    return self.user.username
