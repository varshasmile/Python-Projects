import os
clear = lambda: os.system('cls')

from art import logo

print(logo)
print("Welcome to secret auction program!")

try:
  bidders = {}
  bidding_finished = False
  

  def bidding_calc(bidding_records):
    highest_bid = 0
    for bidder in bidding_records:
        bid_value = bidding_records[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f"The winner of this secret auction is {winner} : ${highest_bid}. Congratulations!")

  
  while not bidding_finished:
    name = input("What's your name? ").capitalize()
    bid = int(input("How much do you want to bid? $"))
    bidders[name] = bid
    ask_bid = input("Is there any other bidder? Yes/No? ").lower()
    clear()
    if ask_bid == "yes":
        continue
    elif ask_bid == "no":
        bidding_finished = True
        bidding_calc(bidders)
    else:
        print("You typed something unexpected! Type only yes/no!")
except Exception as e:
    print(f"Error Encountered : {e}")