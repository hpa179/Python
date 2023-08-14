#PINGClient.py 
import sys
import socket
import random
import time
import struct

# Constants
PING_VERSION = 1


responseCount = 0
rtt_total = 0
payload_total = 0
min_rtt = float('inf')
max_rtt = 0.0

# 5 command line arguments
args = sys.argv
if len(sys.argv) != 6:
    print("ERR - incorrect number of arguments")
    print("Usage: python3 <hostname/IP> <port> <ClientID> <number_of_ping_request_packets> <wait>")
    sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])
clientID = int(sys.argv[3])
num_reqPackets = int(sys.argv[4])
waitTime = int(sys.argv[5])

# Convert hostname to IP address
try:
    ip = socket.gethostbyname(hostname)
except:
    print("ERR - invalid hostname")
    sys.exit(1)

# Create socket and connect to server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(waitTime)

# Print start message for CLient
print("PINGClient started with server IP: {}, port: {}, client ID: {}, packets: {}, wait: {}".format(ip, port,
clientID, num_reqPackets, waitTime))

# Send ping request packets
for i in range(1, num_reqPackets+1):
    # Construct ping packet
    sequence_no = i
    timeStamp = time.time()
    payloadSize = random.randint(150, 300) 
    payload = f"Host: {hostname}\nClass-name: VCU-CMSC440-SPRING-2023\nUser-name: Agarwal, Harita \n Rest: {''.join([random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(payloadSize-61)])}"
    packet = f"Version: {PING_VERSION}\nClient ID: {clientID}\nSequence No.: {sequence_no}\nTime: {timeStamp}\nPayload Size: {payloadSize}\n{payload}\n"

    # Print ping request packet
    print("---------- Ping Request Packet Header ----------")
    print("Version: {}".format(PING_VERSION))
    print("Client ID: {}".format(clientID))
    print("Sequence No.: {}".format(sequence_no))
    print("Time: {}".format(timeStamp))
    print("Payload Size: {}".format(payloadSize))
    print("--------- Ping Request Packet Payload ------------")
    print(payload)
    print("---------------------------------------")

    # Send ping packet
    clientSocket.sendto(packet.encode(), (ip, port))
    
    # Wait for response
    try:
        modifiedPacket, serverAddress = clientSocket.recvfrom(1024)
        response_version, response_client_id, response_sequence_no, response_timestamp, response_payload_size = struct.unpack("HHHfH", modifiedPacket)
        responseCount += 1

        # Recieve the data received in response to a request
        response_payload, serverAddress = clientSocket.recvfrom(response_payload_size)
        # Print ping response packet
        print("----------- Received Ping Response Packet Header ----------")
        print("Version: {}".format(response_version))
        print("Client ID: {}".format(response_client_id))
        print("Sequence No.: {}".format(response_sequence_no))
        print("Time: {}".format(response_timestamp))
        print("Payload Size: {}".format(response_payload_size))
        print("-------- Received Ping Response Packet Payload -------------")
        print(response_payload.decode())
        print("--------------------------------------------------------")
        # Calculate and print RTT
        rtt = time.time() - timeStamp
        min_rtt = min(min_rtt, rtt)
        max_rtt = max(max_rtt, rtt)
        rtt_total += rtt
        payload_total += response_payload_size
        print(f"RTT: {rtt} seconds")
    except Exception as error:
        print("-----------------Ping Request Packet Timed Out-----------------")

packet_loss_rate = 1 - (responseCount / num_reqPackets)
if responseCount > 0:
    avg_rtt = rtt_total / responseCount
    avg_payload_size = payload_total / responseCount
else:
    avg_rtt = 0
    avg_payload_size = 0
print("Summary: {} :: {} :: {:.2f}% :: {:.6f} sec :: {:.6f} sec :: {:.6f} sec :: {:.2f} bytes".format(
    num_reqPackets, responseCount, packet_loss_rate * 100, min_rtt * 1000, max_rtt * 1000, avg_rtt, avg_payload_size))

