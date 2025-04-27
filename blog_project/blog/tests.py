from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    def test_main_page_view(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)

    def test_create_post_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('create_post'), {'title': 'New Post', 'content': 'Content'})
        self.assertEqual(response.status_code, 302)
