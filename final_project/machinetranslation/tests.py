import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFranch(unittest.TestCase):
    def testNull(self):
        self.assertEqual(english_to_french(''), '')
    def testHello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFranchToEnglish(unittest.TestCase):
    def testNull(self):
        self.assertEqual(french_to_english(''), '')
    def testHello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
