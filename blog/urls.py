from django.urls import path

from . import views

urlpatterns = [
        path('', views.BlogListView.as_view(), name='home'),
        path('postagem/<int:pk>/', views.BlogDetalheView.as_view(), name='postagem_detalhe'),
]
