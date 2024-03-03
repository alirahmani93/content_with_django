from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class ContentTestCase(APITestCase):
    fixtures = [
        'content/base_user.yaml',
        'content/model_content.yaml']

    def setUp(self):
        user = User.objects.create_user(username='test', email='ts@ts.com', password='123')
        self.client = APIClient()
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create(self):
        response = self.client.post(reverse('content-score-list'), data={'content': 1, 'score': 2})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'content': 1, 'score': 2})

        response = self.client.post(reverse('content-score-list'), data={'content': 1, 'score': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'content': 1, 'score': 3})

    def test_create_fail(self):
        response = self.client.post(reverse('content-score-list'), data={'content': "a", 'wrong_filed': 3})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'content': ['Incorrect type. Expected pk value, received str.'],
            'score': ['This field is required.']})
