from django.core.urlresolvers import reverse
from django.test import TestCase


class MemberAddViewTest(TestCase):
    def test_member_add_view_should_be_accesiable(self):
        response = self.client.get(reverse('member_add'))

        self.assertEqual(response.status_code, 200)

    def test_member_add_view_should_have_title(self):
        response = self.client.get(reverse('member_add'))

        expected = '<h1>New Member Information</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_member_add_view_should_have_member_form(self):
        response = self.client.get(reverse('member_add'))

        expected = '<form method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Name:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<input id="id_name" maxlength="300" name="name" '
        expected += 'type="text" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Birth Day:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<select id="id_birth_day" name="birth_day">'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Birth Month:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<select id="id_birth_month" name="birth_month">'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Birth Year:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<select id="id_birth_year" name="birth_year">'
        self.assertContains(response, expected, status_code=200)

        expected = "<label>Dad's Name:</label>"
        self.assertContains(response, expected, status_code=200)
        expected = '<input id="id_dad_name" maxlength="300" name="dad_name" '
        expected += 'type="text" />'
        self.assertContains(response, expected, status_code=200)

        expected = "<label>Mom's Name:</label>"
        self.assertContains(response, expected, status_code=200)
        expected = '<input id="id_mom_name" maxlength="300" name="mom_name" '
        expected += 'type="text" />'
        self.assertContains(response, expected, status_code=200)
