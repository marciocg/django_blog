from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Postagem


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username = 'testuser',
                email = 'test@email.com',
                password = 'secret',
        )

        self.postagem= Postagem.objects.create(
                titulo = 'Um título comum',
                corpo = 'Um texto legal',
                autor = self.user,
        )

    def test_string_representation(self):
        postagem = Postagem(titulo='Título exemplo')
        self.assertEqual(str(postagem), postagem.titulo)

    def test_post_content(self):
        self.assertEqual(self.postagem.titulo, 'Um título comum')
     #  self.assertEqualf'{self.postagem.autor}', 'testuser')
        self.assertEqual(str(self.postagem.autor), str('testuser'))
        self.assertEqual(self.postagem.corpo, 'Um texto legal')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Um texto legal')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/postagem/1/')
        no_response = self.client.get('/postagem/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Um título comum')
        self.assertTemplateUsed(response, 'postagem_detalhe.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('postagem_novo'), {
            'titulo': 'Novo título',
            'corpo': 'Novo texto do corpo',
            'autor': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Novo título')
        self.assertContains(response, 'Novo texto do corpo')

    def test_post_update_view(self):
        response = self.client.post(reverse('postagem_altera', args='1'), {
            'titulo': 'Título alterado',
            'corpo': 'Corpo alterado',
    })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('postagem_apaga', args='1'))
        self.assertEqual(response.status_code, 200)
