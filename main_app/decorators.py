from django.http import HttpResponse
from django.shortcuts import redirect

# User auth function to prevent access w/o login


def unauthorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all() [0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("<h1>You are not authorized to acces this page, chump!</h1>")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group=None
        