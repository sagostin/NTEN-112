# user input
user_input = input("Enter input: ")

# make a list
user_list = ["Apples", "Oranges"]

# for every item in the user list
for item in user_list:
    # check if user input is equalsIgnoreCase
    if user_input.lower() == item.lower():
        # print yes
        print("Yes " + item)
    else:
        # print no
        print("No " + item)

    print("Yay")
