from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_form_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                messages.success(request, 'Login successful')
                return redirect('form-list')
        messages.warning(request, 'Login failed. Not a superuser')
    return render(request, 'hazesoft_users/login.html')


def logout_view(request):
    logout(request)
    return redirect('user-login')