#https://www.codeproject.com/Articles/791914/How-to-train-your-Pokerbot
#https://github.com/dickreuter/Poker

from Tournament import Tournament
from Strategy import PositionStrategy


players = int(input("Enter the number of players for the tournament: "))
name = input("Enter the tournament name: ")
buyin = float(input("Enter the tournament buyin: "))
speed = input("Enter the tournament speed: ")

Tourn = Tournament(players, name, buyin, speed)
Main = PositionStrategy(Tourn)

while True:
    cards = input("Enter your cards: ")
    if cards == "":
        break
    try:
        position = int(input("Enter your position: "))
    except ValueError:
        continue
    Main.action(cards, position)




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
