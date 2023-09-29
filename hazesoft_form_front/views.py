from django.shortcuts import render, redirect

from hazesoft_form_core import views as core_views
from django.contrib import messages


# create a function
def form_view(request):
	return render(request, "hazesoft_form_front/form.html")

def register_form(request):
	print(f"Hello {request.POST}")
	is_created = core_views.create_form(request=request)
	if is_created:
		messages.success(request, 'Form created successfully')
	else:
		messages.warning(request, 'Form creation issues')
	return redirect('form-view')

def get_form(request):
	# todo: validate user is superadmin or not
	# todo: read is only allowed to superadmin user
	# todo: get id as param
	data = core_views.read_form(request=request, id=None)
	return render(request, 'hazesoft_form_front/form_list.html', data)


def update_form(request):
	# todo: validate user is superadmin or not
	# todo: updating form value is only allowed to superadmin user
	pass

def remove_form(request):
	# todo: validate user is superadmin or not
	# todo: deletion is only allowed to superadmin user
	pass