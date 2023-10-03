from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile, CONTACT_CHOICES, GENDER_CHOICES

class DateInput(forms.DateInput):
    input_type = 'date'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'gender', 'phone', 'address', 'nationality', 'mode_of_contact', 'date_of_birth', 'education_background']
        widgets = {
            'date_of_birth': DateInput(),
            'gender': forms.RadioSelect(choices=GENDER_CHOICES),
            'mode_of_contact': forms.RadioSelect(choices=CONTACT_CHOICES)
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')
        return email

