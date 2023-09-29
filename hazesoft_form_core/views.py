"""Only validated form is processed here"""

from django.shortcuts import render

from .models import HazeSoftFormModel
from .forms import HazeSoftForm

# Create your views here.
def create_form(request):
    print("IM here")
    print(request.POST)
    if request.method == "POST":
        print("IM here 2")
        hazesoft_form = HazeSoftForm(request.POST)
        if hazesoft_form.is_valid():
            print("IM here 3")
            hazesoft_form.save()
            return True
    return False 

def read_form(request, id: int=None):
    if id:
        data = HazeSoftFormModel.objects.filter(id=id)
    else:
        data = HazeSoftFormModel.objects.all().values()
    return data

def update_form(request):
    pass

def delete_form(request):
    pass
