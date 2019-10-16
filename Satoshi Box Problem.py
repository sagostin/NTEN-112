crate_number = 1
number = 1
normal_direction = True

# change me
number_to_get_to = 54321

while number < number_to_get_to:
    if normal_direction:
        number = number + 1
        crate_number = crate_number + 1

        if crate_number >= 7:
            normal_direction = False

    else:
        crate_number = crate_number - 1
        number = number + 1

        if crate_number <= 1:
            normal_direction = True

print(str(number) + " number")
print(str(crate_number) + " crate number")
