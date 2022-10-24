from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class List(models.Model):
    item = models.CharField(max_length=200)
    user = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)

    def publish(self):
        self.created_date = timezone.now()
        self.save()


class Room(models. Model):
    user_name = models.CharField(max_length=100, blank=True)
    room_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user_name + '|' + self.room_name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    room = models.CharField(max_length=2000000)
    user = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.room
