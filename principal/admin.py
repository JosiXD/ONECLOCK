from django.contrib import admin
from principal.models import *

class RelogioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor')

admin.site.register(Categoria)
admin.site.register(Relogio, RelogioAdmin)