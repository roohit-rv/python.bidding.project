import art
import os
print(art.logo)
bids=[]
highest_bid=0
winner=""
cont=1
def bidder(name,price):
    global highest_bid, winner
    new_bidder={}
    new_bidder["name"]=name
    new_bidder["price"]=price
    bids.append(new_bidder)
    if price>highest_bid:
        highest_bid=price
        winner=name
while cont==1:
    name=input("Enter your name- ")
    price=int(input("enter your bidding price- "))
    bidder(name,price)
    ans=input("are there any other people for bidding (yes or no)").lower()
    if ans=="no":
        cont=0
    elif ans=="yes":
        os.system('cls')

print(winner, " won the bid by the highest amount of bid: ", highest_bid)
