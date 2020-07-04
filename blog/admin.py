from django.contrib import admin
from .models import Post, Categoria

admin.site.site_header = "Post Admin"
admin.site.site_title = "Administração Postagens"
admin.site.index_title = 'Sistema de Gerenciamento de Posts'

admin.site.register(Categoria)

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor', 'categoria', 'data', 'status')
    list_filter = ('autor','categoria', 'data', 'status')
    exclude = ['autor']
    search_fields = ['titulo', 'conteudo', 'categoria']
    prepopulated_fields = {'slug': ('titulo',)}

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)






