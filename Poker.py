#https://www.codeproject.com/Articles/791914/How-to-train-your-Pokerbot
#https://github.com/dickreuter/Poker

from Tournament import Tournament
from Strategy import PositionStrategy

REVERSE_HANDS = ["KA", "QK", "JQ", "TK", "TQ", "TJ", "KAs", "QKs", "JQs", "TKs", "TQs", "TJs"]
NOREVERSE_HANDS = ["AK", "AKs", "KQ", "KQs", "QJ", "QJs", "JT", "JTs", "KT", "KTs", "QT", "QTs", "JT", "JTs"]

players = int(input("Enter the number of players for the tournament: "))
# name = input("Enter the tournament name: ")
# buyin = float(input("Enter the tournament buyin: "))
# speed = input("Enter the tournament speed: ")

Tourn = Tournament(players)
Main = PositionStrategy(Tourn)

def clean_cards(cards):
    cards = cards.upper()
    if 'S' in cards:
        cards = cards[:2] + cards[2:].lower()
    print(cards)
    if cards in REVERSE_HANDS:
        if len(cards) == 2:
            cards = cards[1] + cards[0]
        else:
            cards = cards[1] + cards[0] + cards[2]
    elif cards in NOREVERSE_HANDS:
        cards = cards
    elif cards[0] < cards[1]:
        if len(cards) == 2:
            cards = cards[1] + cards[0]
        else:
            cards = cards[1] + cards[0] + cards[2]
    print(cards)
    return cards

while True:
    cards = input("Enter your cards: ")
    print(cards)
    if cards == "":
        break
    # Clean data to account for S capital for suited and entering
    # data in reverse order.
    cards = clean_cards(cards)
    # try:
    #     position = int(input("Enter your position: "))
    # except ValueError:
    #     continue
    # Main.action(cards, position)




#TESTING
# Test = Tournament(9, "Double-up", 30.00, "Turbo")
# Test2 = Tournament(6, "SNG", 20.00)
#
# #action("AA", 3, Test)
# #action("TT", 4, Test)
# #action("AK", 2, Test2)
# #action("QQ", 6, Test2)
#
# Justin = PositionStrategy(Test2)
# Justin.action("AA", 5) #Else raise limper
# Justin.action("T5", 6)
# Justin.action("TT", 5) #Else call standard
# Justin.action("22", 6) #Else calls stanard
# Justin.action("J3", 6) #Else fold
#Justin.action("QQ", 9)
#Justin.action("98s", 8)
#Justin.action("Q9", 9)
