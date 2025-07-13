from django.urls import path

from weatherApp import views

urlpatterns = [
    path('',views.home, name='home'),
]