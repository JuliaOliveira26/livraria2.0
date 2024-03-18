from django.db import models


class Categoria(models.Model):
    descriçao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descriçao} ({self.id})"
