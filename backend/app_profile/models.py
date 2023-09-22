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

    deleted = models.BooleanField(default=False, editable=False)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    dob = models.DateField(verbose_name="Date of Birth")
    educational_background = models.CharField(max_length=50)
    preffered_contact = models.CharField(
        max_length=10, choices=ContactPreference.choices, default=ContactPreference.NONE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name

    def handle_delete(self, recover=False):
        self.deleted = False if recover else True
        self.save()


class ProfileTrash(Profile):

    class Meta:
        verbose_name = "Trash"
        verbose_name_plural = "Trash"
        proxy = True

    def __str__(self):
        return self.name
