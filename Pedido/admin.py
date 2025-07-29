from django.contrib import admin
from .models import *

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=('created',)

class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)

admin.site.register(Pedido,PedidoAdmin)
admin.site.register(LineaPedido,LineaPedidoAdmin)
