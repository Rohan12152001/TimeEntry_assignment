from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime as dt
from django.forms import widgets
from django.forms.widgets import MultiWidget, SelectDateWidget

# Helpers
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
Project_Choices = (('AWS', 'AWS'),
                   ('Heroku', 'Heroku'),
                   ('GoogleCloud', 'GoogleCloud'))


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=100, choices=Project_Choices, default='AWS')
    startTime = models.TimeField(choices=HOUR_CHOICES)
    endTime = models.TimeField(choices=HOUR_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


