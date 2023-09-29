from django.shortcuts import render

# Create your views here.
def login_form_view(request):
    """
    Currently only super admin is allowed
    """
    return render(request, "hazesoft_users/login.html")