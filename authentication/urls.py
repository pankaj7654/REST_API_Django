from unicodedata import name
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.HelloAuthView.as_view(),name='hello_auth'),
    path('signup/',views.UserCreateView.as_view(),name='sign_up')
]