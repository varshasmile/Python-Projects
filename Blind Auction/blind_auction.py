import os
clear = lambda: os.system('cls')

from art import logo

print(logo)
print("Welcome to secret auction program!")
try:
  bidders = {}
  while True:
    name = input("What's your name? ").capitalize()
    bid = int(input("How much do you want to bid? $"))
    bidders[name] = bid
    winner = max(bidders, key=bidders.get)
    value = bidders[winner]
    ask_bid = input("Is there any other bidder? ").lower()
    clear()
    if ask_bid == "yes":
      continue
    elif ask_bid == "no":
      print(f"The winner of this secret auction is {winner} : ${value}. Congratulations!")
      break
    else:
      print("You typed something unexpected! Type only yes/no!")
except Exception as e:
  print(f"Error Encountered : {e}")