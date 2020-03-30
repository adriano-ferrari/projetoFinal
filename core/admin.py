from django.contrib import admin
from .models import Marca, Veiculo, Pessoa, Parametro, MovRotativo, Mensalista


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total', 'horas_total')


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(Mensalista)
admin.site.register(MovRotativo, MovRotativoAdmin)
