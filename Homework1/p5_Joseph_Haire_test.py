"""Unit tests for p5_Joseph_Haire.py."""

import unittest

from p5_Joseph_Haire import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):
    def test_cipher_preserves_case_spaces_and_punctuation(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

    def test_cipher_wraps_and_accepts_large_shift(self):
        self.assertEqual(caesar_cipher("Zebra", 27), "Afcsb")

    def test_decipher_returns_original_text(self):
        original = "Meet me at 7:30 PM."
        self.assertEqual(caesar_decipher(caesar_cipher(original, 12), 12), original)


class TestLetterFrequency(unittest.TestCase):
    def test_frequency_ignores_case_and_non_letters(self):
        frequencies = letter_frequency("Apple pie! 123")
        self.assertEqual(frequencies["a"], 1)
        self.assertEqual(frequencies["p"], 3)
        self.assertEqual(frequencies["e"], 2)
        self.assertEqual(frequencies["z"], 0)

    def test_frequency_has_all_alphabet_letters(self):
        frequencies = letter_frequency("")
        self.assertEqual(len(frequencies), 26)
        self.assertTrue(all(count == 0 for count in frequencies.values()))


if __name__ == "__main__":
    unittest.main()
