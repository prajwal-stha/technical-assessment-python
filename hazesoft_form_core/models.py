from django.db import models
from django.contrib.auth.models import User

# Create  your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HazeSoftFormModel(TimeStampModel):
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name'
        )
    middle_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default=None,
        verbose_name='Middle Name'
        )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name'
        )
    gender = models.CharField(
        max_length=50,
        verbose_name='Gender'
        )
    address = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default=None,
        verbose_name='Address'
        )
    email = models.EmailField(
        max_length=100, 
        verbose_name='Email'
        )
    nationality = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default=None,
        verbose_name='Nationality'
        )
    dob = models.DateField(
        verbose_name='Date of Birth'
        )
    education = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default=None,
        verbose_name='Education'
        )
    mode_of_contact = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default=None,
        verbose_name='Mode of Contact'
        )
