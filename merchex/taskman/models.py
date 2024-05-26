from django.contrib.auth.models import User

from django.db import models

"""
class home(models.Model):
    def __str__(self):
        return f' {self.name}'
"""


class home(models.Model):
    def __str__(self):
        pass 




class Task(models.Model):
    """
    classe pour créer les tâches
    """
    DIFFICULTY_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    PROGRESS_CHOICES = [
        ('none', 'None'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 3)
    comment = models.CharField(max_length=1000, default='')
    content = models.CharField(max_length=500, default='')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='low')
    progress = models.CharField(max_length=15, choices=PROGRESS_CHOICES, default='none')
    def __str__(self):
        return f' {self.content}'
    



class Chat(models.Model):
    content = models.CharField(max_length=500, default='')
    comment = models.CharField(max_length=500, default='')

    def __str__(self):
        return f' {self.content}'


    

























    