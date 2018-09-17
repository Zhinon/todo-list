from django.db import models
from django.utils import timezone


class Prioridad(models.Model):
    prioridad = models.CharField(max_length=200)

    def __str__(self):
        return self.prioridad


class Estate(models.Model):
    estate = models.CharField(max_length=200)

    def __str__(self):
        return self.estate


class Task(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    prioridad = models.ForeignKey(Prioridad)
    estate = models.ForeignKey(Estate)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
