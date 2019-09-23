numbers = {"zero": 0x7E,
           "one": hex(1),
           "two": hex(2),
           "three": hex(3),
           "four": hex(4),
           "five": hex(5),
           "six": hex(6),
           "seven": hex(7),
           "eight": hex(8),
           "nine": hex(9)}

number = input("Please enter a # (words): ").lower()
value = hex(numbers[number])
print(value)
