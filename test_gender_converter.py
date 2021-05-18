from unittest import TestCase

from gender_converter import convert_gender


class Test(TestCase):
    def test_convert_gender_male(self):
        expected = "MALE"
        actual = convert_gender("M")
        self.assertEqual(actual, expected)

    def test_convert_gender_female(self):
        expected = "FEMALE"
        actual = convert_gender("f")
        self.assertEqual(actual, expected)

    def test_convert_gender_unknown(self):
        expected = "UNKNOWN_GENDER"
        actual = convert_gender("hello")
        self.assertEqual(actual, expected)