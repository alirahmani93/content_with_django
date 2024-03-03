from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class ContentTestCase(APITestCase):
    fixtures = [
        'content/base_user.yaml',
        'content/model_content.yaml']

    def setUp(self):
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        self.client = APIClient()
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_valid_data(self):
        response = self.client.get(reverse('content-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {'title': 'test title 1', 'average_score': 4.0, 'count_score': 2},
             {'title': 'test title 2', 'average_score': 1.0, 'count_score': 1}
        ])
