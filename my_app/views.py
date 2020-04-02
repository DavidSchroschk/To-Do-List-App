from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from . import models


# Create your views here.
def home(request):
    todo_items = models.Todo.objects.all().order_by("-added_date")

    return render(request, 'my_app/index.html', {"todo_items": todo_items})


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    create_obj = models.Todo.objects.create(added_date=current_date, text=content)
    length_of_todos = models.Todo.objects.all().count()
    print(length_of_todos)

    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    print(todo_id)
    models.Todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect("/")
