import unittest
import random_guessing_game2

class TestRandom(unittest.TestCase):
	def setup(self):
		print("about to run a function!")

	def test_input_right(self):
		result = random_guessing_game2.guess_game(5,5)
		self.assertTrue(result)

	def test_input_wrong(self):
		result = random_guessing_game2.guess_game(5,0)
		self.assertFalse(result)

	def test_input_wrong_num(self):
		result = random_guessing_game2.guess_game(5,22)
		self.assertFalse(result)
		
	def test_input_wrong_type(self):
		result = random_guessing_game2.guess_game(5,"hdbdbvb")
		self.assertFalse(result)





if __name__ == "__main__":
	unittest.main()