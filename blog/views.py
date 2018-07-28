from django.views.generic import ListView, DetailView
from . models import Postagem

class BlogListView(ListView):
    model = Postagem
    template_name = 'home.html'

class BlogDetalheView(DetailView):
    model = Postagem
    template_name = 'postagem_detalhe.html'

