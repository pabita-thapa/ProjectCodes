
def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)

def highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder_name = ""
  for bidder in bidding_record:
    bid_amount = auction[name_entered]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      highest_bidder_name = name_entered
  print(f"The winner of the auction is {highest_bidder_name} with the bidding amount of ${highest_bid}.")
    
auction = {} 
more_bidders = True
while more_bidders:
  name_entered = input("Type your name: ")
  bid_price_entered = int(input("Type your bid price: $"))
  auction[name_entered] = bid_price_entered
  add_more = input("Are there other bidders? Type 'yes' or 'no': ").lower()
  if add_more == "yes":
    clear() 
  elif add_more == "no":
    more_bidders = False
    clear()
    highest_bidder(bidding_record = auction)