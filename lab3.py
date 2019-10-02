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
