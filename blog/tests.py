from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from blog.models import Post

# Create your tests here.
class BlogTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email = 'test@email.com', 
            password = 'secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.post), f'{self.post.title}')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content') 

    def test_post_list_view(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')

    def test_post_detail_view(self):
        res = self.client.get('/post/1/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'post_detail.html')