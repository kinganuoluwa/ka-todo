from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name="index"),
    path('create', views.todo_create, name="create"),
    path('<int:id>', views.todo_details, name="detail"),
    path('<int:id>/update-todo', views.todo_update, name="update"),
    path('<int:id>/delete-todo', views.todo_delete, name="delete")
]
