from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateForm


# CRUD Create, Read, Update, Delete
def todo_list(request):
    todos = Todo.objects.all().order_by('-date_created')
    context = {"todos":todos}
    return render(request, 'todo-list.html', context)

def todo_details(request, id):
    todo = Todo.objects.get(id=id)
    context = {'todo':todo}
    return render(request, 'todo-detail.html', context)

def todo_create(request):
    form = CreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/todos')
    context = {
        'form':form
        }
    return render(request, 'todo-create.html', context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = CreateForm(request.POST or None, instance=todo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/todos')
    context = {
        'form':form
    }
    return render(request, 'todo-update.html', context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos')

# Authentication
