from django.contrib import admin
from .models import Gasto


# Register your models here.
class GastoAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'tipo_despesa', 'descricao',
                    'forma_pagamento', 'vencimento', 'quitado')


admin.site.register(Gasto, GastoAdmin)
