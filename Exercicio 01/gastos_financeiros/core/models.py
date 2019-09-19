from django.db import models


# Create your models here.
class Gasto(models.Model):
    data_criacao = models.DateField("Data da criação")
    tipo_despesa = models.CharField(max_length=30)
    descricao = models.CharField("Descrição", max_length=250)
    forma_pagamento = models.CharField(max_length=30)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    def __str__(self):
        return str(self.data_criacao)
