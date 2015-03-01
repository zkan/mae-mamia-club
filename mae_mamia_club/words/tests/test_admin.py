from django.test import TestCase
from django.contrib.auth.models import User


class WordAdminTest(TestCase):
    def test_access_word_admin(self):
        User.objects.create_superuser(
            'admin',
            'admin@autowash.com',
            'maemamiaclub'
        )
        self.client.login(username='admin', password='maemamiaclub')

        response = self.client.get('/admin/words/word/')

        self.assertEqual(response.status_code, 200)
