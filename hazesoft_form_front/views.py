from django.shortcuts import render

# create a function
def form_create_view(request):
	context ={
		"data":"Gfg is the best",
		"list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	}
	return render(request, "hazesoft_form_front/form.html", context)
