from django.contrib import admin
from apps.galeria.models import Fotografia

# Register your models here.

#criando uma classe de visualização
#é necessário passar a classe para o register
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    #criar links para acessar os itens
    list_display_links = ('id', 'nome')
    #cria uma campo de busca
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario',)
    list_editable = ('publicada', )
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)