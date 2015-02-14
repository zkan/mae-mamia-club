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
