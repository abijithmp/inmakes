from django.http import HttpResponse
from django.shortcuts import render

from .models import Places,People


# Create your views here.


def demo(request):
    obj=Places.objects.all()
    obj_1=People.objects.all()
    return render(request,"index.html",{'result':obj,'people':obj_1})

# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("am contact")