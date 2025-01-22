from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class cpf(models.Model):
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome