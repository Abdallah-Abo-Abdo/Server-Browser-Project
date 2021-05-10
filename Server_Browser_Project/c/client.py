import socket
import sys


HOST = "192.168.1.100"
PORT = 9999

s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))
print("[+] Connected with Server")

# get file name to send
f_send = "mytext.txt"
# open file
with open(f_send, "rb") as f:
    # send file
    print("[+] Sending file...")
    data = f.read()
    s.sendall(data)

    # close connection
    s.close()
    print("[-] Disconnected")
    sys.exit(0)