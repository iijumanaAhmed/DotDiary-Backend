from django.contrib import admin
from .models import ToDoList, Task, Distraction, Tag

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Task)
admin.site.register(Distraction)
admin.site.register(Tag)