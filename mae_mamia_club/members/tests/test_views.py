import datetime
from datetime import date

from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Member
from mappings.models import Word


class MemberAddViewTest(TestCase):
    def test_member_add_view_should_be_accessible(self):
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

    def test_add_new_member_successfully(self):
        data = {
            'name': 'Nong Bee',
            'birth_day': '1',
            'birth_month': '2',
            'birth_year': '2010',
            'dad_name': 'Roong',
            'mom_name': 'Ood'
        }

        response = self.client.post(
            reverse('member_add'),
            data=data
        )

        member = Member.objects.get(name='Nong Bee')

        self.assertEqual(member.name, 'Nong Bee')
        self.assertEqual(member.birthdate, datetime.date(2010, 2, 1))
        self.assertEqual(member.dad_name, 'Roong')
        self.assertEqual(member.mom_name, 'Ood')
        self.assertEqual(member.signup_date, date.today())


class MemberViewTest(TestCase):
    def test_member_view_should_be_accessible(self):
        Member.objects.create(
            name='Nong Bee',
            birthdate=datetime.date(2014, 12, 30),
            dad_name='Roong',
            mom_name='Ood'
        )
        Word.objects.create(
            id=13,
            text='Nong'
        )
        Word.objects.create(
            id=14,
            text='Born on'
        )
        Word.objects.create(
            id=12,
            text='December'
        )
        Word.objects.create(
            id=15,
            text='Dad'
        )
        Word.objects.create(
            id=16,
            text='Mom'
        )
        Word.objects.create(
            id=17,
            text='Member No.'
        )
        response = self.client.get(reverse('member') + '?id=1')

        self.assertEqual(response.status_code, 200)

    def test_member_view_should_raise_page_not_found_error_if_no_id(self):
        response = self.client.get(reverse('member') + '?id=1')

        self.assertEqual(response.status_code, 404)

        response = self.client.get(reverse('member'))

        self.assertEqual(response.status_code, 404)
