from django import forms
from datetime import date

from .models import HazeSoftFormModel


class HazeSoftForm(forms.ModelForm):
    class Meta:
        model = HazeSoftFormModel
        fields = '__all__'
    
    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob and dob > date.today():
            raise forms.ValidationError('Date of Birth cannot be in the future.')
        return dob
