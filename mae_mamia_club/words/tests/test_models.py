import datetime

from django.db import IntegrityError
from django.test import TestCase

from ..models import Word


class WordTest(TestCase):
    def setUp(self):
        self.word = Word()

    def test_add_new_word(self):
        self.word.text = 'Member No. '
        self.assertFalse(self.word.pk)

        self.word.save()

        self.assertTrue(self.word.pk)

        word = Word.objects.get(id=self.word.id)

        self.assertEqual(word.text, 'Member No. ')

    def test_add_new_word_without_text_should_fail(self):
        self.word.text = None

        self.assertRaises(IntegrityError, self.word.save)

    def test_display_word_object_should_be_readable(self):
        self.word.text = 'Member No .'
        self.word.save()

        self.assertEqual(
            self.word.__unicode__(),
            'Member No. '
        )
