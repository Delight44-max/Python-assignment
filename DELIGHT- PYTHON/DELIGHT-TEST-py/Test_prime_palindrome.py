import unittest
import primepalindrome

class TestPalindromicPrime(unittest.TestCase):

    def test_smallest_prime_palindrome(self):
        self.assertTrue(primepalindrome.is_palindromic_prime(2))

    def test_common_prime_palindrome(self):
        self.assertTrue(primepalindrome.is_palindromic_prime(11))

    def test_larger_prime_palindrome(self):
        self.assertTrue(primepalindrome.is_palindromic_prime(101))

    def test_palindrome_not_prime(self):
        self.assertFalse(primepalindrome.is_palindromic_prime(121))

    def test_not_palindrome_nor_prime(self):
        self.assertFalse(primepalindrome.is_palindromic_prime(10))