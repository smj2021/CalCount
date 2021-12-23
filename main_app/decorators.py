from django.http import HttpResponse
from django.shortcuts import redirect

def unauthorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')