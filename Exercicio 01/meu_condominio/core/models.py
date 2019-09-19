from django.db import models

# Create your models here.
class Apartamento(models.Model):
    numero = models.PositiveIntegerField("Número")
    qtdQuartos = models.PositiveIntegerField("Quantidade de quartos")
    proprietario = models.CharField("Proprietário",max_length=60)
    valor = models.DecimalField(decimal_places=2,max_digits=9)
