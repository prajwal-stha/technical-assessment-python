from django.core.exceptions import ValidationError
from django.contrib import messages

from .models import HazeSoftFormModel
from .forms import HazeSoftForm


# Create your views here.
def create_form(request):
    hazesoft_form = HazeSoftForm(request.POST)
    if hazesoft_form.is_valid():
        hazesoft_form.save()
        messages.success(request, 'Form created successfully')
    else:
        if hazesoft_form.errors:
            messages.warning(request, hazesoft_form.errors)


def read_form(request, order_by: str):
    data = HazeSoftFormModel.objects.all().order_by(order_by).values()
    return data


def update_form(request, instance):
    hazesoft_form = HazeSoftForm(request.POST, instance=instance)
    if hazesoft_form.is_valid():
        hazesoft_form.save()
    else:
        if hazesoft_form.errors:
            messages.warning(request, hazesoft_form.errors)
        
def delete_form(request, item_id):
    try:
        item = HazeSoftFormModel.objects.get(id=item_id)
    except:
        messages.warning(request, f"{item_id} not found. Error deleting item")
        return False

    item.delete()
    messages.success(request, f"{item_id} deleted successfully")
    return True
