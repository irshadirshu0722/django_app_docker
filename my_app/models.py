from django.db import models

# Create your models here.
class TestModal(models.Model):
  count = models.IntegerField(default=0)
