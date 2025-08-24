from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from accounts.models import Post

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_post(self):
        data = {'title': 'Test', 'content': 'Test content'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, 201)