# from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .forms import TodolistForm
from .models import TodoList

# Create your views here.
def index(request):
    todo_items = TodoList.objects.order_by('id')
    form = TodolistForm()
    context = {'todo_items':todo_items,'form':form} 
    return render(request,'todolists/index.html',context)
@require_POST
def addTodoItem(request):
    form = TodolistForm(request.POST)
    if form.is_valid():
        new_todoitem = TodoList(text=request.POST['text'])
        new_todoitem.save()
    return redirect('index')

def completedTodo(request,todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompletedTodo(request):
    TodoList.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteallTodo(request):
    TodoList.objects.all().delete()
    return redirect('index')    