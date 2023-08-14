#PINGServer.py
import sys
import socket
import random
import time
import struct

# Constants for the ping protocol
PING_VERSION = 1
PING_HEADER_SIZE = struct.calcsize("!BBHHH")

# 2 command-line arguments
if len(sys.argv) != 3:
    print("ERR - incorrect number of arguments")
    sys.exit(1)
try:
    port = int(sys.argv[1])
    loss = int(sys.argv[2])
    if port <= 0 or port >= 65536:
        raise ValueError
    if loss < 0 or loss > 100:
        raise ValueError
except ValueError:
    print("ERR - arg value")
    sys.exit(1)

# Create server socket and bind to the specified port
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("", port))
    print(
        "PINGServer started with server IP: {}, port: {} ...".format(socket.gethostbyname(socket.gethostname()), port))
except socket.error:
    print("ERR - cannot create PINGServer socket using port number", port)
    sys.exit(1)

# Listen for incoming packets
while True:
    # Generate a random number to determine whether to drop the packet
    drop_packet = random.randint(1, 100) <= loss
    # Receive packet from client
    try:
        packet, client_address = server_socket.recvfrom(1024)
    except socket.timeout:
        print("ERR - failed to receive packet:")
        continue

    x = 1
    response_lines = packet.split(b"\n")
    response_payload = b"\n".join(response_lines[5:])
    timeStamp = time.time()
    payloadSize= len(packet) - PING_HEADER_SIZE

    # Print packet information
    ping_id = int(response_lines[1].decode().split(": ")[1])
    ping_seqnum = int(response_lines[2].decode().split(": ")[1])

    print("IP:{} :: Port:{} :: ClientID:{} :: Seq.no:{} :: {}".format(client_address[0], client_address[1], ping_id, ping_seqnum, "DROPPED" if drop_packet else "RECEIVED"))
    print("----------Received Ping Request Packet Header----------")
    print(response_lines[0].decode())
    print(response_lines[1].decode())
    print(response_lines[2].decode())
    print(response_lines[3].decode())
    print(response_lines[4].decode())
    print("---------Received Ping Request Packet Payload------------")
    print(response_payload.decode())
    print("---------------------------------------")

    # If the packet wasn't dropped, construct a response packet
    if not drop_packet:
        response_payload = "\n".join(line.upper() for line in response_payload.decode().split("\n")).encode()
        timee = time.time()
        response_header = struct.pack("HHHfH",PING_VERSION,ping_id,ping_seqnum,timee, len(response_payload))
        server_socket.sendto(response_header, client_address)
        server_socket.sendto(response_payload, client_address)
        print("-----------Ping Response Packet Header ----------")
        print("Version: ", PING_VERSION)
        print("Client ID:", ping_id)
        print("Sequence No.:", ping_seqnum)
        print("Time:", timee)
        print("Payload Size:", len(response_payload))
        print("---------- Ping Response Packet Payload -------------")
        print(response_payload.decode())
        print("---------------------------------------")
        
# Close server socket
server_socket.close()
