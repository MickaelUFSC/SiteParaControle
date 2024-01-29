from django.contrib import admin
from .models import Venda, Cliente, ItemVenda
# Register your models here.
admin.site.register(Venda)
admin.site.register(Cliente)
admin.site.register(ItemVenda)
