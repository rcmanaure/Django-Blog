from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo




