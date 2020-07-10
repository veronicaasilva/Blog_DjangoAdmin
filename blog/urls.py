from django.urls import path
from .views import post_detail, AllPost

urlpatterns = [
    path('', AllPost.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]