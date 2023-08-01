from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_user_list_api(self):
        url = reverse('user_list_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_posts_api(self):
        user_id = self.user.id
        url = reverse('user_posts_api', kwargs={'user_id': user_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_api(self):
        url = reverse('create_post_api')
        data = {'title': 'Test Post', 'content': 'This is a test post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_post_api(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.', user=self.user)
        url = reverse('delete_post_api', kwargs={'pk': post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthenticated_create_post_api(self):
        self.client.logout()
        url = reverse('create_post_api')
        data = {'title': 'Test Post', 'content': 'This is a test post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_delete_post_api(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.', user=self.user)
        self.client.logout()
        url = reverse('delete_post_api', kwargs={'pk': post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
