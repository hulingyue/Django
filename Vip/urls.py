from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from Vip import views

urlpatterns = [
    path("", views.Hello)
]
