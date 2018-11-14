import unittest
from src.math import Math

class MathTest(unittest.TestCase):

	def test_addition(self):
		# Make test fail
		self.assertEqual(Math.addition(3,4), 7)

	def test_subtraction(self):
		self.assertEqual(Math.subtraction(5,2), 3)

	def test_multiplication(self):
		self.assertEqual(Math.multiplication(3,5), 15)

	def test_division(self):
		self.assertEqual(Math.division(4,2), 2)