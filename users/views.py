from django.shortcuts import render, redirect
from .forms import UserProfileForm

def create_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can define 'success' URL later
    else:
        form = UserProfileForm()
    return render(request, 'create_user.html', {'form': form})

def success(request):
    return render(request, 'success.html')

