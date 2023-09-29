"""Only validated form is processed here"""

from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import HazeSoftFormModel
from .forms import HazeSoftForm

# Create your views here.
def create_form(request):
    print(request.POST)
    if request.method == "POST":
        hazesoft_form = HazeSoftForm(request.POST)
        if hazesoft_form.is_valid():
            # HazeSoftFormModel(**request.POST).save()
            hazesoft_form.save()
            return True
    return False 

def read_form(request, id: int=None):
    if id:
        data = HazeSoftFormModel.objects.filter(id=id)
    else:
        data = HazeSoftFormModel.objects.all().values()
    return data

def update_form(request, item_id):
    print('I am here')
    print(item_id)
    try:
        item = HazeSoftFormModel.objects.get(id=item_id)
        print('item i ', item)
    except:
        return False
    
    if request.method == 'POST':
        print('I am here 2')
        hazesoft_form = HazeSoftForm(request.POST, instance=item)
        if hazesoft_form.is_valid():
            hazesoft_form.save()
            item = HazeSoftFormModel.objects.get(id=item_id)
            print(f"---{item.email}")
    else:
        form = HazeSoftForm(instance=item)
        print(f"My form  {form}")
    return item

        
def delete_form(request, item_id):
    item = HazeSoftFormModel.objects.get(id=item_id)
    if item:
        item.delete()
        return True
    return False
