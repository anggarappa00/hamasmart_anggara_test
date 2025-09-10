from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name