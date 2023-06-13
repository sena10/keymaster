from django.contrib import admin
from .models import Chave,Funcionario,AluguelChave,Sala
# Register your models here.
admin.site.register(Chave)
admin.site.register(Funcionario)
admin.site.register(AluguelChave)
admin.site.register(Sala)