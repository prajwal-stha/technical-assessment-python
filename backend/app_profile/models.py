from django.db import models


class Profile(models.Model):

    class GenderChoice(models.TextChoices):

        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    class ContactPreference(models.TextChoices):

        EMAIL = 'E', 'Email'
        PHONE = 'P', 'Phone'
        NONE = 'N', 'None'

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    dob = models.DateField()
    educational_background = models.CharField(max_length=50)
    preffered_contact = models.CharField(
        max_length=10, choices=ContactPreference.choices, default=ContactPreference.NONE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name
