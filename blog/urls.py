from django.urls import path
from .views import post_detail, AllPost, post_por_categoria

urlpatterns = [
    path('', AllPost.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<int:id>', post_por_categoria, name='post_por_categoria')
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]