from django.contrib import admin
from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserProfileView,UserLogoutView,UserChangePasswordView,UserPasswordResetView

urlpatterns = [
    path('register/',UserRegistrationView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('profile/',UserProfileView.as_view()),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('password-reset/',UserPasswordResetView.as_view()),
    
]