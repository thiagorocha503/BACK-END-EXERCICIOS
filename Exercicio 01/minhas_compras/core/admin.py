from django.contrib import admin
from .models import Produto


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'unidadeCompra', 'qtdPrevistoMes', 'preco', 'precoMaximo')


admin.site.register(Produto, ProdutoAdmin)
