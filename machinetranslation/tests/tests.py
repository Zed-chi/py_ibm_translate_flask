import unittest

from translator import english_to_french, french_to_english


class TestTranslate(unittest.TestCase):
    def test_english_to_french(self):
        """test from english to french"""
        src = "Hello"
        to_be = "Bonjour"
        self.assertEqual(english_to_french(src), to_be)

    def test_french_to_english(self):
        """test from french to english"""
        src = "Bonjour"
        to_be = "Hello"
        self.assertEqual(french_to_english(src), to_be)

    def test_null_french_to_english(self):
        """test null input to french_to_english"""
        self.assertRaises(TypeError, french_to_english)

    def test_null_english_to_french(self):
        """test null input to english_to_french"""
        self.assertRaises(TypeError, english_to_french)


unittest.main()
