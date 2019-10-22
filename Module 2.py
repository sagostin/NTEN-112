import math

# Take a look at the personal projects and contributed ones.
# https://gitlab.dec0de.xyz/shaunagostinho

# print Hello World
print("Hello World!")

# print Seperator and End
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# Minimize and Simplify
print("    *\n"
      "   * *\n"
      "  *   *\n"
      " *     *\n"
      "***   ***\n"
      "  *   *\n"
      "  *   *\n"
      "  *****")

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

print("        *" * 2)
print("       * *" * 2)
print("      *   *" * 2)
print("     *     *" * 2)
print("    *       *" * 2)
print("   *         *" * 2)
print("  *           *" * 2)
print(" *             *" * 2)
print("******     ******" * 2)
print("     *     *" * 2)
print("     *     *" * 2)
print("     *     *" * 2)
print("     *     *" * 2)
print("     *     *" * 2)
print("     *     *" * 2)
print("     *******" * 2)

# "I'm"
# ""learning""
# """Python"""
print('"I\'m"')
print('""learning"')
print('"""Python"""')

# Total number of apples
john = 5
mary = 10
adam = 15

totalApples = john + mary + adam
print("Total number of apples: ", totalApples)

# Kilometers to Miles
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.609
kilometers_to_miles = kilometers / 1.609

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Floats and exponents

# import math
x = 1
x = float(x)
y = (3 * math.pow(x, 3)) - (2 * math.pow(x, 2)) + (3 * x) - 1
print("y =", y)

# Comments
# this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2  # number of hours
seconds = 3600  # number of seconds in 1 hour

print("Hours: ", a)  # printing the number of hours
print("Seconds in Hours: ", a * seconds)  # printing the number of seconds in a given number of hours

# here we should also print "Goodbye", but a programmer didn't have time to write any code
# this is the end of the program that computes the number of seconds in 3 hours

#
a = float(input("First number: "))
b = float(input("Second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("\nThat's all, folks!")

# I don't know, but it takes input
x = float(input("Enter value for x: "))

y = 1/(x+(1/(x+(1/(x+(1/x))))))

print("y =", y)

# Event Time
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura  # find a total of all minutes
hour = hour + mins // 60  # find a number of hours hidden in minutes and update the hour
mins = mins % 60  # correct minutes to fall in the (0..59) range
hour = hour % 24  # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')
