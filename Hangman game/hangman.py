import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for letter in range(word_length):
    display += '_'
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input('Guess a letter of the word: ')

    if guess in display:
      print('You already typed this letter!')

    if guess not in chosen_word:
        print('This letter is not in the chosen word. You lose a life.')
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f'The word was {chosen_word}.')
            print('You Lose!')

    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if '_' not in display:
            end_of_game = True
            print('You Win.')