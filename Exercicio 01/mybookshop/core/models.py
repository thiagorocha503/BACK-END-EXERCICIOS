from django.db import models


# Create your models here.
class Livro(models.Model):
    titulo = models.CharField("Título", max_length=50)
    autor = models.CharField("Autor", max_length=50)
    assunto = models.CharField("Assunto", max_length=30)
    editora = models.CharField("Editora", max_length=20)
    isbn = models.CharField("ISBN", max_length=20)
    ano_publicacao = models.DateField("Ano de publicação")

    def __str__(self):
        return self.titulo
