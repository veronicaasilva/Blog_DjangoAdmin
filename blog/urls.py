from django.urls import path
from .views import post_detail, AllPost, post_por_categoria, AllCategorias

urlpatterns = [
    path('', AllPost.as_view(), name='home'),
    path('categorias', AllCategorias.as_view(), name='categorias'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<int:id>', post_por_categoria, name='post_por_categoria')
]