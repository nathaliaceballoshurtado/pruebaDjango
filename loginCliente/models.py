from django.db import models

# Create your models here.

class Post(models.Model):
    cedula = models.CharField(max_length=200)
    tipo = models.TextField()

    def __str__(self):
        return self.cedula