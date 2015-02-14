import datetime
from datetime import date

from django.test import TestCase

from ..forms import MemberForm
from ..models import Member


class MemberFormTest(TestCase):
    def test_form_should_contain_defined_fields(self):
        expected_fields = [
            'name',
            'birth_day',
            'birth_month',
            'birth_year',
            'dad_name',
            'mom_name',
        ]

        form = MemberForm()

        for each in expected_fields:
            self.assertTrue(each in form.fields)

    def test_input_valid_data_to_form(self):
        valid_data = [
            {
                'name': 'Nong Bee',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'dad_name': 'Roong',
                'mom_name': 'Ood'
            }
        ]

        for each in valid_data:
            form = MemberForm(data=each)

            self.assertTrue(form.is_valid())
            self.assertFalse(form.errors)

    def test_input_invalid_data_to_form(self):
        invalid_data = [
            {
                'name': '',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'dad_name': 'Roong',
                'mom_name': 'Ood'
            },
            {
                'name': 'Nong Bee',
                'birth_day': '',
                'birth_month': '2',
                'birth_year': '2010',
                'dad_name': 'Roong',
                'mom_name': 'Ood'
            },
            {
                'name': 'Nong Bee',
                'birth_day': '1',
                'birth_month': '',
                'birth_year': '2010',
                'dad_name': 'Roong',
                'mom_name': 'Ood'
            },
            {
                'name': 'Nong Bee',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '',
                'dad_name': 'Roong',
                'mom_name': 'Ood'
            },
            {
                'name': 'Nong Bee',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'dad_name': '',
                'mom_name': 'Ood'
            },
            {
                'name': 'Nong Bee',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'dad_name': 'Roong',
                'mom_name': ''
            },
        ]

        for each in invalid_data:
            form = MemberForm(data=each)

            self.assertFalse(form.is_valid())
            self.assertTrue(form.errors)

    def test_save_form_successfully_should_store_data(self):
        data = {
            'name': 'Nong Bee',
            'birth_day': '1',
            'birth_month': '2',
            'birth_year': '2010',
            'dad_name': 'Roong',
            'mom_name': 'Ood'
        }

        form = MemberForm(data=data)
        form.is_valid()
        form.save()

        member = Member.objects.get(name='Nong Bee')

        self.assertEqual(member.name, 'Nong Bee')
        self.assertEqual(member.birthdate, datetime.date(2010, 2, 1))
        self.assertEqual(member.dad_name, 'Roong')
        self.assertEqual(member.mom_name, 'Ood')
        self.assertEqual(member.signup_date, date.today())
