huge_number = 0
last_digit = 0
last_digit_large = 0
for i in range(256):
    i += 1
    if len(str(i)) == 2:
        if int(str(int(i))[0:1] + "0") != last_digit:
            huge_number = int(huge_number) + int(str(int(i))[0:1] + "0")
            last_digit = int(str(int(i))[0:1] + "0")
        else:
            huge_number = int(huge_number) + int(str(int(i))[1:2])
    elif len(str(i)) == 1:
        huge_number = int(huge_number) + int(i)
    elif len(str(i)) == 3:
        if int(str(int(i))[0:2]) != last_digit_large:
            huge_number = int(huge_number) + int(str(int(i))[0:1] + "0")
            last_digit = int(str(int(i))[0:1] + "0")
        else:
            huge_number = int(huge_number) + int(str(int(i))[1:2])

    print(huge_number)

print(huge_number)
print(huge_number % 3)
