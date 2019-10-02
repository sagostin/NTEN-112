import time

# Spathiphyllum tester
plant = str(input("Spathiphyllum? : "))
if plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
elif plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
else:
    print("Spathiphyllum! Not " + plant + "!")

# annual income tax calculator
annual_income = float(input("Enter annual income: "))
if annual_income > 85528.00:
    tax = 14839.02 + ((annual_income - 85528.00) * 0.32)
else:
    tax = (annual_income * .18) - 556.02

tax = round(tax, 0)
if tax <= 0.00:
    tax = 0.00

print("The tax is:", tax, "thalers")

# leap year calculator
year = int(input("What year? : "))
if year < 1582:
    print("Not within the Gregorian calendar.")
else:
    if year % 4 != 0:
        print("Common Year")
    elif year % 100 != 0:
        print("Leap Year")
    elif year % 400 != 0:
        print("Common Year")
    else:
        print("Leap Year")

# magician number thing
secret_number = 69
user_input = int(input("Enter a number : "))
while user_input != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_input = int(input("Enter a number : "))

print("Well done, muggle! You are free now.")
# greater or equal to
n = int(input("Enter a number: "))
print(str(n >= 100))

# sleep thread example
for i in range(5):
    print(str((i + 1)) + " Mississippi")
    time.sleep(1)

# break while loop
while True:
    user_input = str(input("Enter a word: "))
    if user_input == "chupacabra":
        print("You've successfully left the loop.")
        break

# ugly vowel
userWord = input("Input a word: ")
userWord = userWord.upper()
for wordLetter in userWord:
    if wordLetter == "A":
        continue
    elif wordLetter == "E":
        continue
    elif wordLetter == "I":
        continue
    elif wordLetter == "O":
        continue
    elif wordLetter == "U":
        continue
    else:
        print(wordLetter)

# nice vowel
userWord = input("Input a word: ")
userWord = userWord.upper()
niceLetters = ""
for wordLetter in userWord:
    if wordLetter == "A":
        continue
    elif wordLetter == "E":
        continue
    elif wordLetter == "I":
        continue
    elif wordLetter == "O":
        continue
    elif wordLetter == "U":
        continue
    else:
        niceLetters = niceLetters + wordLetter
print(niceLetters)

# Block height
blocks = int(input("How many blocks do you have? : "))
needed = 1
height = 0
while blocks >= needed:
    blocks = blocks - needed
    height = height + 1
    needed = needed + 1

print("Height is: " + str(height))

# c0 idk german dude
c0 = int(input("Enter a number: "))
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
    elif c0 != 1:
        c0 = c0 / 2
    print(int(c0))
    steps = steps + 1
print("Steps: " + str(steps))

# simple list stuff
hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

middle_number = int(input("Input a number to replace the middle number: "))
hatList[2] = middle_number
del hatList[len(hatList) - 1]
print(len(hatList))
print(hatList)

# Beatles shoit
# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for members in range(2):
    beatles.append(str(input("Enter another name: ")))

print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "RingoStarr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))

# remove double shits
mylist = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist = []

for num in mylist:
    if num not in newlist:
        newlist.append(num)
mylist = newlist[:]
print("The list with unique elements only: ")
print(mylist)
