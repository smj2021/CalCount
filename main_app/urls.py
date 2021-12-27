from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.userPage, name='userPage'), #userPage
    path('product/', views.fooditem, name='fooditem'),
    path('createfooditem/', views.createfooditem, name='createfooditem'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('addFooditem/', views.addFooditem, name='addFooditem'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'), #protected view for user pw reset
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
]