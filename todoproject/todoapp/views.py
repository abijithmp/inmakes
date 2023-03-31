from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import TaskName
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class TaskListView(ListView):
    model = TaskName
    template_name = 'index.html'
    context_object_name = 'task_all'

class TaskDetailView(DetailView):
    model=TaskName
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = TaskName
    template_name = 'update.html'
    context_object_name ='i'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = TaskName
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def add(request):
    taskall=TaskName.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=TaskName(name=name,priority=priority,date=date)
        task.save()
    return render(request,'index.html',{"task_all":taskall})

def delete(request,task_id):
    tasks=TaskName.objects.get(id=task_id)
    if request.method=='POST':
        tasks.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task_all=TaskName.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task_all)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task_all':task_all})