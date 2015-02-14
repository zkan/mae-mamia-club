from django.test import TestCase

from ..forms import MemberForm


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
