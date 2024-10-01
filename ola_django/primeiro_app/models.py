from django.db import models

class NovaModel(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.nome