from django.urls import path

from . import views

urlpatterns = [
        path('', views.BlogListView.as_view(), name='home'),
        path('postagem/<int:pk>/', views.BlogDetalheView.as_view(), name='postagem_detalhe'),
        path('postagem/novo/', views.BlogCreateView.as_view(), name='postagem_novo'),
        path('postagem/<int:pk>/altera/', views.BlogAlteraView.as_view(), name='postagem_altera'),
        path('postagem/<int:pk>/apaga/', views.BlogApagaView.as_view(), name='postagem_apaga'),
]
