from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Postagem

class BlogListView(ListView):
    model = Postagem
    template_name = 'home.html'

class BlogDetalheView(DetailView):
    model = Postagem
    template_name = 'postagem_detalhe.html'

class BlogCreateView(CreateView):
    model = Postagem
    template_name = 'postagem_novo.html'
    fields = '__all__'

class BlogAlteraView(UpdateView):
    model = Postagem
    fields = ['titulo', 'corpo']
    template_name = 'postagem_altera.html'

class BlogApagaView(DeleteView):
    model = Postagem
    template_name = 'postagem_apaga.html'
    success_url = reverse_lazy('home')
