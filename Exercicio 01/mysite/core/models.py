from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField("Endereço", max_length=200)
    email = models.EmailField('e-mail')
    data_nascimento = models.DateField("Dat de nascimento")
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
