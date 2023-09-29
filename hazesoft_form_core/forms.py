from django import forms
from .models import HazeSoftFormModel

class HazeSoftForm(forms.ModelForm):
    class Meta:
        model = HazeSoftFormModel
        fields = [
            'first_name', 'last_name', 
            'gender', 'address', 'dob', 'nationality']
