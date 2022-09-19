# Getting started with Django
Step-by-step procedure of starting Django project

### 1. Set up Virtual Environment
```python
# install virutal environment
pip install virtualenv
# create virtual environment 
virtualenv venv
# activate virtual environment
source venv/Scripts/activate
```
### 2. Install Django
```python
pip install django
```
### 3. Create Django project in current folder
```python
django-adming startproject projectname .
```
### 4. Create app
```python
python manage.py startapp appname
```
### 5. Make migrations
```python
python manage.py makemigrations
```
### 6. Run migrations
```python
python manage.py migrate
```
### Database and Admin Panel
### 7. Create Model
### 8. Register Model
### 9. URL Config

## CRUD Functionalities

* ### **Create**
```python
def todo_create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todos')
    context = {
        'form':form
        }
    return render(request, 'todo-add.html', context)
```

* ### **Read**
```python
def todo_list(request):
    todos = Todo.objects.all().order_by('-date_created')
    context = {"todos":todos}
    return render(request, 'todo-list.html', context)

# read by id
def todo_details(request, id):
    todo = Todo.objects.get(id=id)
    context = {'todo':todo}
    return render(request, 'todo-detail.html', context)
```
* ### **Update**
```python
def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = CreateForm(instance=todo)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todos')
    context = {
        'form':form
    }
    return render(request, 'todo-update.html', context)
```

* ### **Delete**
```python
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos')
```

## Authentication