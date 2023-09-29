from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


from hazesoft_form_core import views as core_views
from hazesoft_form_core import forms as core_forms

from hazesoft_users.permissions import superuser_required

def form_view(request):
	form = core_forms.HazeSoftForm()
	return render(request, "hazesoft_form_front/form.html", {'form': form})


def register_form(request):
	is_created = core_views.create_form(request=request)
	if is_created:
		messages.success(request, 'Form created successfully')
	else:
		messages.warning(request, 'Form creation failed')
	return redirect('form-view')

@superuser_required
def get_form(request):
	print("get form", request.user)
	data = core_views.read_form(request=request, id=None)
	return render(request, 'hazesoft_form_front/form_list.html', {'data': data})

@superuser_required
def update_form(request, item_id):
	print("update form", request.user)
	item = core_views.update_form(request=request, item_id=item_id)
	return render(request, 'hazesoft_form_front/edit.html', {'item': item})

@superuser_required
def remove_form(request, item_id):
	print("remove form", request.user)
	if not item_id:
		messages.warning(request, 'Item id is not provided')
	try:
		status = core_views.delete_form(request=request, item_id=item_id)
		if status:
			messages.success(request, f'Item with id {item_id} deleted succesfully')
	except:
		messages.error(request, 'Error deleting item')
	return redirect('form-list')
