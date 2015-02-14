from django.core.urlresolvers import reverse
from django.test import TestCase


class MemberAddViewTest(TestCase):
    def test_member_add_view_should_be_accesiable(self):
        response = self.client.get(reverse('member_add'))

        self.assertEqual(response.status_code, 200)
