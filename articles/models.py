from django.db import models


class HealthArticle(models.Model):
  title = models.CharField(max_length=200)
  category = models.CharField(max_length=50)
  summary = models.TextField()
  content = models.TextField()
  published_date = models.DateField()

  class Meta:
    ordering = ['-published_date']

  def __str__(self):
    return self.title
