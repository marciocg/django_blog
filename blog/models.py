from django.db import models
from django.urls import reverse

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
            'auth.User',
            on_delete=models.CASCADE,
    )
    corpo = models.TextField()


    def __str__(self):
        return self.titulo


    def get_absolute_url(self):
        return reverse('postagem_detalhe', args=[str(self.id)])
