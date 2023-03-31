from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movies


# Create your views here.
def index(request):
    movies=Movies.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie_details=Movies.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie_details})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movies(name=name,img=img,desc=desc,year=year)
        movie.save()
    return render(request,'add.html')

def update_movie(request,id):
    movie=Movies.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def delete_moive(request, id):
    mov = Movies.objects.get(id=id)
    if request.method=='POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html',{'movie':mov})
