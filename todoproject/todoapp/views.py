from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import table
from . forms import tabform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class lview(ListView):
    model = table
    template_name='home.html'
    context_object_name = 'task1'

class dview(DetailView):
    model = table
    template_name = 'display.html'
    context_object_name = 'task'
class uview(UpdateView):
    model=table
    template_name = 'classupdate.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvd',kwargs={'pk':self.object.id})

class delview(DeleteView):
    model = table
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy("cbv")
def home(request):
    task1 = table.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tab=table(name=name,priority=priority,date=date)
        tab.save()
    return render(request,'home.html',{'task1':task1})
# def display(request):
#     task=table.objects.all()
#     return render(request,'display.html',{'task':task})
def delete(request,id):
    task = table.objects.get(id=id)
    if request.method=='POST':
         task.delete()
         return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=table.objects.get(id=id)
    f=tabform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html',{'f':f,'task':task})
