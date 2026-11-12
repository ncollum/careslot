from django.db import models


class Clinic(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  phone = models.CharField(max_length=20)
  opening_hours = models.TextField()

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class Specialty(models.Model):
  name = models.CharField(max_length=50, unique=True)
  icon = models.CharField(max_length=50, help_text='Bootstrap Icons name, for example bandaid')
  keywords = models.TextField(blank=True, help_text='Symptoms separated by commas, for example rash, acne, eczema')

  class Meta:
    ordering = ['name']
    verbose_name_plural = 'specialties'

  def __str__(self):
    return self.name


class Language(models.Model):
  name = models.CharField(max_length=50, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class Doctor(models.Model):
  name = models.CharField(max_length=100)
  specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name='doctors')
  clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT, related_name='doctors')
  languages = models.ManyToManyField(Language, related_name='doctors')
  bio = models.TextField(blank=True)
  photo = models.ImageField(upload_to='doctors/', blank=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return f'Dr. {self.name}'

  @property
  def initials(self):
    return ''.join(word[0] for word in self.name.split())[:2]
