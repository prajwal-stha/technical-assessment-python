from django.shortcuts import redirect
from django.contrib import messages

def superuser_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            messages.warning(request, 'Do login for access.')
            return redirect('user-login')
        return view_func(request, *args, **kwargs)
    return wrapped_view
