import sys
import random

random_num = random.randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
	try:
		guess_num = int(input(f"Guess a number between {sys.argv[1]}-{sys.argv[2]} : "))
		if 0 < guess_num < 11:
			if guess_num == random_num:
				print("You're a GENIUS!")
				break
		else:
			print("Please enter a number between entered arguments!")
	except ValueError:
		print("Hey! I asked a number!")
		continue


