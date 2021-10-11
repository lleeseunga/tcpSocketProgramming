import socket
import sys

host = socket.gethostname()
port = 12345
FORMAT = "utf-8"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    filename = sys.argv[1]
    
    with open(filename,"rb") as f:
        print("Sending...")

        l = f.read(1024)
        s.send(filename.encode(FORMAT))
        s.recv(1024).decode(FORMAT)

        while (l):
            #print("Sending...")
            s.send(l)
            s.recv(1024).decode(FORMAT)
            l = f.read(1024)
    print("Done Sending")
