from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addTodoItem,name='add'),
    path('completed/<todo_id>',views.completedTodo,name='completed'),
    path('deletecompleted',views.deleteCompletedTodo,name='deletecompleted'),
    path('deleteall',views.deleteallTodo,name='deleteall')

]
