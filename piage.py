# Log In Welcome Statetment!
print ("Welcome to Good Morning America")

# Menu Item Selection
menu = "Enter Item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hashbrown, toast, coffee, tea: "
# Input for Quantity
quantity = "Please enter ordered quantity: "

# Prices of Individual Items
egg = float(.99)
bacon = float(0.49)
sausage = float(1.49)
hashbrown = float(1.19)
toast = float(.79)
coffee = float(1.09)
tea = float(0.89)

# Prices for Pre-Made Breakfast Meals
smallBreakfast = egg + hashbrown + (2*toast) * (2*bacon) + sausage
regularBreakfast = (2*egg) + hashbrown + (2*toast) + (4*bacon) + (2*sausage)
bigBreakfast = (3*egg) + (2*hashbrown) + (4*toast) + (6*bacon) + (3*sausage)
# Float conversion
smallBreakfast = float(smallBreakfast)
regularBreakfast = float(regularBreakfast)
bigBreakfast = float(bigBreakfast)

# Assigning Values to Variables
menuItem = "Menu Item"
quantityChoice = int(0)
subtotal = float(0.0)

while menuItem != "q":
    menuItem = input(menu)

    def formatInput(menuItem) :
        menuItem = menuItem.lower().strip()
#DO THIS PART LATER

    if menuItem == "q":
        break

    quantityChoice = int(input(quantity))

    if menuItem == "small breakfast":
        subtotal = subtotal + (smallBreakfast*quantityChoice)
    elif menuItem == "regular breakfast":
        subtotal == subtotal + (regularBreakfast*quantityChoice)
    elif menuItem == "big breakfast":
        subtotal == subtotal + (bigBreakfast*quantityChoice)
    elif menuItem == "egg":
        subtotal == subtotal + (egg*quantityChoice)
    elif menuItem == "bacon":
        subtotal == subtotal + (bacon*quantityChoice)
    elif menuItem == "sausage":
        subtotal == subtotal + (sausage*quantityChoice)
    elif menuItem == "hashbrown":
        subtotal == subtotal + (hashbrown*quantityChoice)
    elif menuItem == "toast":
        subtotal == subtotal + (toast*quantityChoice)
    elif menuItem == "coffee":
        subtotal == subtotal + (coffee*quantityChoice)
    elif menuItem == "tea":
        subtotal == subtotal + (tea*quantityChoice)
    else:
        print ("Not a valid request. Please try again")

subtotal = float(subtotal)
subtotal = (round(subtotal,2))
print("Food & Beverage Total: ", subtotal)
tax = subtotal*0.13
tax = float(tax)
tax = (round (tax,2))
print("Applicable Tax: ", tax)
totalCost = subtotal + tax
totalCost = (round(totalCost,2))
print("Amount Due: ", totalCost)