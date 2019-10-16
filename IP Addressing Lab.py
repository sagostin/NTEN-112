ip_address = input("Input your IP address (CIDR Notation): ")
subnet_mask = input("Input your subnet mask (CIDR Notation): ")
default_gateway = input("Please input your default gateway (CIDR Notation): ")


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


def bitwise_ip(ip, subnet):
    if validate_ip(ip) & validate_ip(subnet_mask):
        bits = []

        for i in range(4):
            bits.insert(i, bin(int(ip.split(".")[i]) & int(subnet.split(".")[i])))

        return bits


if validate_ip(ip_address) & validate_ip(subnet_mask) & validate_ip(default_gateway):

    # print da shiet
    print("IP Address:" + ip_address +
          "\n" + "Subnet Mask: " + subnet_mask +
          "\n" + "Default Gateway: " + default_gateway)
else:
    exit("Invalid IP address, subnet mask, or default gateway. Exiting.")

ping_command = input("Enter the ping command (ex: PING 192.168.0.1): ")
ping = ping_command.split(" ")

if ping[0].lower() != "ping":
    exit("The PING command was not entered correctly... Exiting.")

if validate_ip(ping[1]):
    # check ip and check if its in the same lan
    bits_ip = bitwise_ip(ip_address, subnet_mask)
    bits_ping_ip = []

    for i in range(4):
        bits_ping_ip.insert(i, bin(int(ping[1].split(".")[i]) & int(ping[1].split(".")[i])))

    network_size = 0
    for ii in bits_ip:
        if ii == bin(0):
            break
        else:
            network_size += 1

    for net in range(network_size):
        if bits_ip[net] == bits_ping_ip[net]:
            continue
        else:
            exit("Sending frames from " + ip_address + " to " + default_gateway)
    exit("Sending frames from " + ip_address + " to " + ping[1])
else:
    exit("The IP address is not in CIDR notation. Exiting.")
