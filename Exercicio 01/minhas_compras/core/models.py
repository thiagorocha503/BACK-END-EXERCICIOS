from django.db import models


# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField("Descrição", max_length=128)
    unidadeCompra = models.CharField("Unidade de compra", max_length=30)
    qtdPrevistoMes = models.DecimalField("Quantidade prevista para o mês", max_digits=7, decimal_places=2)
    preco = models.DecimalField("Preço", max_digits=7, decimal_places=2)
    precoMaximo = models.DecimalField("Preço máximo", max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome
