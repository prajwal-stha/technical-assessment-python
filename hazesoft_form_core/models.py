from django.db import models
from django.contrib.auth.models import User

# Create  your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HazeSoftFormModel(TimeStampModel):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=100, default='bhuwan@example.com')
    nationality = models.CharField(max_length=50)
    dob = models.CharField(max_length=50, verbose_name='Date of Birth')
    education = models.CharField(max_length=50, verbose_name='Education')
    mode_of_contact = models.CharField(max_length=50, verbose_name='Mode of Contact')
    