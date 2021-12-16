from lib import *

arr = file2arr("day-16.txt")

def hex2bin(s):
    b = ""
    scale = 16
    for c in s:
        b += str(bin(int(c, scale))[2:].zfill(4))
    
    return b

def bin2dec(s):
    d = 0
    for i in range(len(s)):
        val = int(s[i])
        d += 2 ** (len(s) - i - 1) * val
    return d

def dec2bin(i):
    return str(bin(i))[2:]

def iszero(s):
    if len(s) == 0:
        return True
    for c in s:
        if int(c) != 0:
            return False
    return True

def parse_packet(packet, packet_number = 0):
    packet_number += 1
    if not iszero(packet) and len(packet) > 0:
        value = 0
        loc = 0
        # print("{}: Parsing packet".format(packet_number))
        v_sum = 0

        # Get version number and type ID
        # print("{}: \tVersion bits: \t\t{}".format(packet_number, packet[loc:loc+3]))
        v = bin2dec(packet[loc:loc+3])
        loc += 3

        v_sum += v

        # print("{}: \tType bits: \t\t{}".format(packet_number, packet[loc:loc+3]))
        type_id = bin2dec(packet[loc:loc+3])
        loc += 3

        # Packet is not a literal, so parse subpackets
        if type_id != 4:
            # print("{}: \tPacket is operator".format(packet_number))

            # Make empty list to put values into
            values = []

            # Get subpacket format bit
            length_type_id = bin2dec(packet[loc])
            loc += 1

            if length_type_id == 0:
                # Parse total length of subpackets
                subpacket_length = bin2dec(packet[loc:loc+15])

                # print("{}: \tLength bits: \t\t{}".format(packet_number, packet[loc:loc+15]))
                # print("{}: \tContains subpackets of length {}".format(packet_number, subpacket_length))

                loc += 15
                start = loc

                # While there is still data to parse, try to 
                # parse the next subpacket
                subpackets = packet[loc:]
                
                while not iszero(subpackets) and loc < start + subpacket_length:
                    # Get subpacket
                    subpackets = packet[loc:]
                    if subpackets != "":
                        # Parse subpacket and update values array and version sum
                        v, _, val, sub = parse_packet(subpackets, packet_number=packet_number)
                        v_sum += v
                        values.append(bin2dec(val))
                        subpackets = sub
                        loc = len(packet) - len(sub)
            else:
                # Next 11 bits represent number of subpackets
                subpacket_number = bin2dec(packet[loc:loc+11])
                # print("{}: \tContains {} packets".format(packet_number, subpacket_number))
                loc += 11

                # Parse subpackets until you reach the number
                count = 0
                while count < subpacket_number:
                    count += 1
                    if packet[loc:] != "":
                        # Parse subpacket and update values array and version sum
                        # print("{}: \tProcessing packet {}".format(packet_number, count))
                        v, _, val, sub = parse_packet(packet[loc:], packet_number = packet_number)
                        v_sum += v
                        values.append(bin2dec(val))
                        # print(values)
                        loc = len(packet) - len(sub)
            
            # Handle typing
            # print("{}: \tInputs: \t\t{}".format(packet_number, values))
            if type_id == 0:
                # Sum packets
                for val in values:
                    value += val
                # print("{}: \tSum packet, value = {}".format(packet_number, value))
            if type_id == 1:
                # Product of packets
                value = 1
                for val in values:
                    value *= val
                # print("{}: \tProduct packet, value = {}".format(packet_number, value))
            if type_id == 2:
                # Minimum
                value = min(values)
                # print("{}: \tMin packet, value = {}".format(packet_number, value))
            if type_id == 3:
                # Maximum
                value = max(values)
                # print("{}: \tMax packet, value = {}".format(packet_number, value))
            if type_id == 5:
                # Greater than
                if values[0] > values[1]:
                    value = 1
                else:
                    value = 0
                # print("{}: \tGreater than packet, value = {}, comparison {} > {}".format(packet_number, value, values[0], values[1]))
            if type_id == 6:
                # Less than
                if values[0] < values[1]:
                    value = 1
                else:
                    value = 0
                # print("{}: \tLess than packet, value = {}, comparison {} < {}".format(packet_number, value, values[0], values[1]))
            if type_id == 7:
                # Equal to
                if values[0] == values[1]:
                    value = 1
                else:
                    value = 0
                # print("{}: \tEqual packet, value = {}, comparison {} == {}".format(packet_number, value, values[0], values[1]))
            value = dec2bin(value)
        else:
            # Packet represents a literal, so parse it
            # print("{}: \tPacket is literal".format(packet_number))
            literal = ""
            lit_length = 5
            next = packet[loc:loc + lit_length]
            for n in next[1:]:
                literal += n
            loc += lit_length

            while int(next[0]) != 0:
                # Parse the next literal
                next = packet[loc:loc + lit_length]
                loc += lit_length
                for n in next[1:]:
                    literal += n
            # print("{}: \tLiteral value: \t\t{}".format(packet_number, literal))

            value = literal

        return v_sum, type_id, str(value), packet[loc:]
    

v, t, val, p = parse_packet(hex2bin(arr[0]))

problem(1)

print(v)

problem(2)

print(bin2dec(val))
