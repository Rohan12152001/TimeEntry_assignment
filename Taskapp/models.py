from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime as dt

# Helpers
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
Project_Choices = (('AWS', 'AWS'),
                   ('Heroku', 'Heroku'),
                   ('GoogleCloud', 'GoogleCloud'))


# Create your models here.

# previous model
# class Task(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=150)
#     created = models.DateTimeField(auto_now_add=True)
#     # "project working on" drop down
#     startTime = models.TimeField()
#     endTime = models.TimeField()
#     # timer =
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ['created']

"""# class Project(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=150)
#     created = models.DateTimeField(auto_now_add=True)
#     pass"""

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    # "project working on" drop down
    project = models.CharField(max_length=100, choices=Project_Choices, default='AWS')
    startTime = models.TimeField(choices=HOUR_CHOICES)
    endTime = models.TimeField(choices=HOUR_CHOICES)
    # timer =

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


