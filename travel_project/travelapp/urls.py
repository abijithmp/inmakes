from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.demo,name='demo'),
    # path("about/",views.about,name='about'),
    # path("contact/",views.contact,name='contact'),
]