from django.contrib import admin
from .models import Anuncio


# Register your models here
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'titulo', 'texto', 'nomeContato',
                    'telefone', 'secao', 'tipo')


admin.site.register(Anuncio, AnuncioAdmin)
