import random

wager = int(input("Enter the amount of money you want to wager: "))
highest = wager
print(wager)
turn = 0

while (wager > 0):                          # while you have money
    turn += 1
    roll1 = random.randint(1, 6)            # Get first die roll
    roll2 = random.randint(1, 6)            # Get second die roll

    total = roll1 + roll2

    if total == 7:                          # You won a turn
        wager += 4
        highest = max(highest, wager)       # Check to see if you made money

    else:                                   # It's ok, keep playing
        wager -= 1    


print("The number of turns it took you to lose was " + str(turn) +  ".")
print("The maximum amount of money in the pot was " + str(highest) + ".")