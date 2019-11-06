# Input
networkIP = input("What is the network IP? (ie; 172.16.0.0) : ")
subnetMask = input("What is the network's subnet mask? (ie; 255.255.0.0) : ")
hostInput = input("How many hosts per network? (q to exit) (ie; 32) : ")

networkHostCount = {}


# Maximum Hosts
def maximumHosts(subnet):
    bitCount = 0
    for bits in subnet.split('.'):
        bitCount += bin(int(bits)).count("1")
    return (2 ** (32 - bitCount)) - 2


# Turn the host count into slash notation bit count
def hostCountToSubnet(hostCount):
    startingBits = 32
    while (2 ** (32 - startingBits) - 2) < hostCount:
        startingBits -= 1

    return startingBits


def hostRequiredSubnetCount(hostCount):
    return (2 ** (32 - hostCountToSubnet(hostCount))) - 1


# Functions
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


# Loop to keep adding networks
while (hostInput != "q"):
    networkHostCount[len(networkHostCount.values()) + 1] = int(hostInput)
    hostInput = input("How many hosts per network? (q to exit) (ie; 32) : ")

totalHostCount = 0

for hosts in networkHostCount.values():
    totalHostCount += hosts + len(networkHostCount.values()) * 2

if hosts >= maximumHosts(subnetMask):
    exit("You don't have enough address space for these hosts.")

networks = {}


# Create the broadcast ip based on the ip given
def createNewAddress(network, incrementCount):
    octets = []
    bitPosition = 0

    for ip in network.split('.'):
        if len(octets) == 3:
            if (int(ip) + incrementCount) >= 255:
                bitPosition = len(octets) - 1
            else:
                octets.append(int(ip) + incrementCount)
        else:
            octets.append(int(ip))

    if bitPosition != 0:
        octets[bitPosition] = octets[bitPosition] + 1
        octets.append(incrementCount - 254)

    return str(octets[0]) + "." + str(octets[1]) + "." + str(octets[2]) + "." + str(octets[3])


def createNetworkAndBroadcast(previousNetworkBroadcast, hostCount):
    network = []

    network.append(createNewAddress(previousNetworkBroadcast, 1))
    network.append(createNewAddress(network[0], hostCount))

    return network


networks = {}

for networkNum, hostCount in networkHostCount.items():
    if len(networks) == 0:
        networks[networkNum] = [networkIP,
                                createNewAddress(networkIP, hostRequiredSubnetCount(hostCount))]
    else:
        networks[networkNum] = createNetworkAndBroadcast(str(networks.get(int(networkNum) - 1)[1]),
                                                         hostRequiredSubnetCount(hostCount))

    # check if it's higher than the possible 255, then increment the second last number

for network, ipList in networks.items():
    print("Network #" + str(network) + " : ", ipList, sep=" ")
