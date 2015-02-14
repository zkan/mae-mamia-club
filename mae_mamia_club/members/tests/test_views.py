from django.core.urlresolvers import reverse
from django.test import TestCase


class MemberAddViewTest(TestCase):
    def test_member_add_view_should_be_accesiable(self):
        response = self.client.get(reverse('member_add'))

        self.assertEqual(response.status_code, 200)

    def test_member_add_view_should_have_member_form(self):
        response = self.client.get(reverse('member_add'))

        expected = '<th><label for="id_name">Name:</label></th>'
        expected += '<td><input id="id_name" maxlength="300" name="name" '
        expected += 'placeholder="Name" type="text" /></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<th><label for="id_birth_day">Birth Day:</label></th>'
        expected += '<td><select id="id_birth_day" name="birth_day">'
        self.assertContains(response, expected, status_code=200)

        expected = '<th><label for="id_birth_month">Birth Month:</label></th>'
        expected += '<td><select id="id_birth_month" name="birth_month">'
        self.assertContains(response, expected, status_code=200)

        expected = '<th><label for="id_birth_year">Birth Year:</label></th>'
        expected += '<td><select id="id_birth_year" name="birth_year">'
        self.assertContains(response, expected, status_code=200)

        expected = '<th><label for="id_dad_name">Dad Name:</label></th>'
        expected += '<td><input id="id_dad_name" maxlength="300" '
        expected += 'name="dad_name" placeholder="Dad Name" type="text" />'
        expected += '</td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<th><label for="id_mom_name">Mom Name:</label></th>'
        expected += '<td><input id="id_mom_name" maxlength="300" '
        expected += 'name="mom_name" placeholder="Mom Name" type="text" />'
        expected == '</td>'
        self.assertContains(response, expected, status_code=200)
