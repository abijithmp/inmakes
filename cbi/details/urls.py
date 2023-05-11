from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('district.wikipedia_url', views.wikipedia, name='person_det'),

]
