import datetime

from django.db import IntegrityError
from django.test import TestCase

from ..models import Member


class MemberTest(TestCase):
    def setUp(self):
        self.member = Member()

    def test_add_new_member(self):
        self.member.name = 'Nong Bee'
        self.member.birthdate = datetime.date(2014, 12, 30)
        self.member.dad_name = 'Ruk'
        self.member.mom_name = 'Ood'

        self.assertFalse(self.member.pk)

        self.member.save()

        self.assertTrue(self.member.pk)

        member = Member.objects.get(id=self.member.id)

        self.assertEqual(member.name, 'Nong Bee')
        self.assertEqual(member.birthdate, datetime.date(2014, 12, 30))
        self.assertEqual(member.dad_name, 'Ruk')
        self.assertEqual(member.mom_name, 'Ood')
        self.assertTrue(member.signup_date)

    def test_add_new_member_without_name_should_fail(self):
        self.member.name = None
        self.member.birthdate = datetime.date(2014, 12, 30)
        self.member.dad_name = 'Ruk'
        self.member.mom_name = 'Ood'

        self.assertRaises(IntegrityError, self.member.save)

    def test_add_new_member_without_birthdate_should_fail(self):
        self.member.name = 'Nong Bee'
        self.member.birthdate = None
        self.member.dad_name = 'Ruk'
        self.member.mom_name = 'Ood'

        self.assertRaises(IntegrityError, self.member.save)

    def test_add_new_member_without_dad_name_should_fail(self):
        self.member.name = 'Nong Bee'
        self.member.birthdate = datetime.date(2014, 12, 30)
        self.member.dad_name = None
        self.member.mom_name = 'Ood'

        self.assertRaises(IntegrityError, self.member.save)

    def test_add_new_member_without_mom_name_should_fail(self):
        self.member.name = 'Nong Bee'
        self.member.birthdate = datetime.date(2014, 12, 30)
        self.member.dad_name = 'Ruk'
        self.member.mom_name = None

        self.assertRaises(IntegrityError, self.member.save)
