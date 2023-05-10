from django.shortcuts import render

from details.models import District


# Create your views here.
def demo(request):

    dict_dist={
        'dist':District.objects.all()
    }
    return render(request,"index.html",dict_dist)