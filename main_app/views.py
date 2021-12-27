from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from .filters import fooditemFilter

# Create your views here.


@login_required(login_url='login')
@admin_only
def home(request):
    breakfast = Category.objects.filter(name='breakfast')[
        0].fooditem_set.all()[:5]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
    customers = Customer.objects.all()
    context = {'breakfast': breakfast,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               'customers': customers,
               }
    return render(request, 'main.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def fooditem(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    bcnt = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    lcnt = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    dcnt = dinner.count()
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
    scnt = snacks.count()
    context = {'breakfast': breakfast,
               'bcnt': bcnt,
               'lcnt': lcnt,
               'scnt': scnt,
               'dcnt': dcnt,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               }
    return render(request, 'fooditem.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createfood(request):
    form = fooditemForm()
    if request.method == 'POST':
        form = fooditemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form': form}
    return render(request, 'createfooditem.html', context)

@unauthorized_user
def registerPage(request):
    form=createUserForm()
    if request.method == 'POST':
        form=createUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get(name='username')
            group=Group.objects.get(name='user')
            user.groups.add(group)
            email=form.cleaned_data.get('email')
            Customer.objects.create(user=user, name=username, email=email)
            messages.success(request, 'Account created for ' + username)
            return redirect('login')
    context={'form': form}
    return render(request, 'register.html', context)

