from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class List(models.Model):
    item = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
