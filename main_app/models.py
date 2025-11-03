from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class ToDoList(models.Model):
    list_title = models.CharField()
    created_at = models.DateField('ToDoList Creation Date', auto_now_add=True)
    
    def __str__(self):
        return f'{self.list_title} To Do List'

STATUS = (
    (False, 'Not Done'),
    (True, 'Done')
)

PRIORITY = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High')
)

class Task(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')
    task = models.CharField()
    is_done = models.CharField(choices=STATUS, default=STATUS[0][0])
    priority = models.CharField(max_length=1, choices=PRIORITY, default=PRIORITY[0][0])
    
    def __str__(self):
        return f'[{self.get_priority_display()}] - {self.task}'

class Distraction(models.Model):
    distraction_name = models.CharField()
    distraction_icon = models.ImageField(upload_to='main_app/static/images/')
    
    def __str__(self):
        return f'{self.distraction_name.capitalize()}'

class Tag(models.Model):
    tag_name = models.CharField()
    tag_color = models.CharField()

    def __str__(self):
        return f'{self.tag_name.capitalize()} Tag'

LOG_STATUS = (
    ('S', 'Started'),
    ('P', 'Paused'),
    ('E', 'Ended')
)

FOCUS_LEVEL = (
    (1, 'Distracted'),
    (2, 'Unfocused'),
    (3, 'Average'),
    (4, 'Focused'),
    (5, 'Flow State')
)

class FocusLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    distraction = models.ManyToManyField(Distraction)
    start_time = models.DurationField('Started At:', null=True, blank=True)
    end_time = models.DurationField('Ended At:', null=True, blank=True)
    total_duration =  models.DurationField(null=True, blank=True)
    focus_level = models.CharField(max_length=1, choices=FOCUS_LEVEL, null=True, blank=True)
    outcomes = models.TextField(blank=True)
    todolist = models.OneToOneField(ToDoList, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'FocusLog Session #{self.id}'