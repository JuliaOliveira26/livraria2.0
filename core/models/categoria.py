from django.db import models

class Categoria(models.Model):
    descriçao = models.CharField(max_length= 100)