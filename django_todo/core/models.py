from django.db import models
from django.utils.text import Truncator

class Todo(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150, blank=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    conclused_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return Truncator(self.message).chars(20)
