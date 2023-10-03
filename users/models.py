from django.db import models

CONTACT_CHOICES = [('Email','Email'),('Phone','Phone'),('None', 'None')]
GENDER_CHOICES = [('M','Male'),('F','Female')]

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='M')
    phone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    education_background = models.CharField(max_length=255)
    mode_of_contact = models.CharField(max_length=255, choices=CONTACT_CHOICES, default='Email')

    def __str__(self):
        return self.name

