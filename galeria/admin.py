from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

#criando uma classe de visualização
#é necessário passar a classe para o register
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    #criar links para acessar os itens
    list_display_links = ('id', 'nome')
    #cria uma campo de busca
    search_fields = ('nome',)

admin.site.register(Fotografia, ListandoFotografias)