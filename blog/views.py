from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Post, Categoria
from .forms import ComentarioForm


class AllPost(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-data')
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AllPost, self).get_context_data(**kwargs)
        context['categoria_list'] = Categoria.objects.all()
        return context

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comentarios = post.comentarios.filter(aprovado=True)
    novo_comentario = None

    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.post = post
            novo_comentario.save()
    else:
        comentario_form = ComentarioForm()
    
    context = {
        'post': post,
        'comentarios': comentarios,
        'novo_comentario': novo_comentario,
        'comentario_form': comentario_form,
    }

    return render(request, 'post_detail.html', context)


def post_por_categoria(request, id):
    post_list = Post.objects.filter(categoria__id=id)
    return render(request, 'post_por_categoria.html', {'post_list':post_list})