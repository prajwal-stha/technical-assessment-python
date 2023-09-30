from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse



from hazesoft_form_core import views as core_views
from hazesoft_form_core import forms as core_forms
from hazesoft_form_core.models import HazeSoftFormModel
from hazesoft_users.permissions import superuser_required


def form_view(request):
	"""Display form"""
	return render(request, "hazesoft_form_front/form.html")


def register_form(request):
	if request.method  != 'POST':
		return redirect('form-view')
	core_views.create_form(request=request)
	return redirect("form-view")


@superuser_required
def get_form(request):
	data = core_views.read_form(request=request, order_by='-created_at')
	return render(request, 'hazesoft_form_front/form_list.html', {'data': data})


@superuser_required
def update_form(request, item_id):
	if not item_id:
		messages.warning(request, 'Item id is not provided')
		return redirect('form-list')
	
	try:
		item = HazeSoftFormModel.objects.get(id=item_id)
	except:
		messages.warning(f"Item not found")
		return redirect('form-list')

	if request.method != 'POST':
		return render(request, 'hazesoft_form_front/edit.html', {'item': item})

	core_views.update_form(request=request, instance=item)
	return redirect('form-list')


@superuser_required
def remove_form(request, item_id):
	if not item_id:
		messages.warning(request, 'Item id is not provided')
		return redirect('form-list')
	
	core_views.delete_form(request=request, item_id=item_id)
	return redirect('form-list')
