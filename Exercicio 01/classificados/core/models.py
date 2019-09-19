from django.db import models


# Create your models here.
class Anuncio(models.Model):
    cliente = models.CharField("Cliente", max_length=50)
    titulo = models.CharField("Título", max_length=30)
    texto = models.CharField("Texto", max_length=300)
    nomeContato = models.CharField("Nome do contato", max_length=50)
    telefone = models.CharField("Telefone", max_length=20)
    secao = models.CharField("Seção", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)

    class Meta:
        verbose_name = "Anúncio"
        verbose_name_plural = "Anúncios"
