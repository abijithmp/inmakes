from django.urls import path
from . import views
from shopping_cart import views

app_name = 'home'

urlpatterns = [
    path("", views.allProdCat, name='allProdCat')

]
