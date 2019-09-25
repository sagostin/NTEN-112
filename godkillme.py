first_ip = input("Enter an IP address (eg. 192.168.1.1): ")
first_subnet_mask = input("Enter the subnet mask (255.255.255.0): ")


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


if validate_ip(first_ip) & validate_ip(first_subnet_mask):
    print("Your IP address and subnet mask are valid.")
else:
    exit("Invalid IP address, or subnet mask isn't in valid CIDR notation.")

compare_first_ip_number = []
number_first_ip = 0

for first_split_ip in first_ip.split('.'):
    compare_first_ip_number.insert(number_first_ip, first_split_ip)
    number_first_ip = number_first_ip + 1

compare_subnet_number = []
number_subnet = 0

for first_split_subnet in first_subnet_mask.split('.'):
    compare_subnet_number.insert(number_subnet, first_split_subnet)
    number_subnet = number_subnet + 1

binary_compare = []
binary_index = 0

while binary_index < 4:
    binary_num = int(compare_first_ip_number[binary_index])
    binary_sub = int(compare_subnet_number[binary_index])
    binary_compare.insert(binary_index, (bin(binary_num & binary_sub)))
    binary_index = binary_index + 1

print(str(int(binary_compare[0], 2)) + "." + str(int(binary_compare[1], 2)) + "."
      + str(int(binary_compare[2], 2)) + "." + str(int(binary_compare[3], 2)))
