from django.db import models

# Create your models here.
class ToDoList(models.Model):
    list_title = models.CharField()
    created_at = models.DateField('ToDoList Creation Date', auto_now_add=True)
    
    def __str__(self):
        return f'{self.list_title} To Do List'

STATUS = (
    ('N', 'Not Done'),
    ('Y', 'Done')
)

PRIORITY = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High')
)

class Task(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task = models.CharField()
    is_done = models.CharField(max_length=1, choices=STATUS, default=STATUS[0][0])
    priority = models.CharField(max_length=1, choices=PRIORITY, default=PRIORITY[0][0])
    
    def __str__(self):
        return f'[{self.get_priority_display()}] - {self.task}'
