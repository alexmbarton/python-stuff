import sys

mealCost = float(sys.stdin.readline())
tipPercent = float(sys.stdin.readline())
taxPercent = float(sys.stdin.readline())

# Let's work out the tax
# mealCost x tax/100 
tax = mealCost * (taxPercent/100)

# Let's work out the tip
# mealCost x tip/100
tip = mealCost * (tipPercent/100)

# Finally, let's see how much it is
# for a pretty shitty meal
totalCost = mealCost + tax + tip

#And finally round this (down? WTF! Great restuarant)
totalCost = int(round(totalCost))

print ("The total meal cost is {} dollars.".format(totalCost))