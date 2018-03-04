from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length = 100)
    time = models.TimeField()
    date = models.DateField()
    venue = models.CharField(max_length = 100)

    def __str__(self):
        return self.name