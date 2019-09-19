from django.contrib import admin
from .models import Apartamento


# Register your models here.
class ApartamentoAdmib(admin.ModelAdmin):
    list_display = ('numero', 'qtdQuartos', 'proprietario', 'valor')


admin.site.register(Apartamento, ApartamentoAdmib)
