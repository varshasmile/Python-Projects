alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_direction, start_text, shift_amount):
  end_text = ""
  if cipher_direction == 'decode':
      shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"The {cipher_direction}d text is {end_text}")

from caesar_cipher_art import logo
print(logo)

to_continue = True
while to_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26        # if user enters shifrt greater than the alphabets ie >26 (to avoid out of index error)
  caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

  ask_user = input("Type 'yes' if you want to go. Otherwise type 'no'.\n").lower()
  if ask_user == 'no':
    to_continue = False
    print('Thank You! GoodBye.')