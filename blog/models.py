from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 


class Categoria(models.Model):
    categoria = models.CharField(
        max_length=100,
        help_text='Insira uma categoria (Ex.: Drama)'
    )

    def __str__(self):
        return self.categoria


class Post(models.Model):
    STATUS = (
        (0,"Aguardando"),
        (1,"Publicado")
    )
    autor = models.ForeignKey(
        get_user_model(), 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='blog_posts'
    )
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL,
        null =  True
    )
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    conteudo = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-data']

    '''def display_categoria(self):
        return ', '.join([categoria.categoria for categoria in self.categoria.all()[:3]])

    display_categoria.short_description = 'Categoria(s)' '''

    '''
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])'''

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comentarios')
    nome = models.CharField(max_length=80)
    email = models.EmailField(null=True, blank=True)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    class Meta:
        ordering = ['data']

    def __str__(self):
        return 'Comentando {} por {}'.format(self.mensagem, self.nome)