import socket               

host = socket.gethostname() 
port = 12345
FORMAT = "utf-8"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(5)
    
    while True:
        c,addr = s.accept()
        print("Got connection from", addr)

        l = c.recv(1024)
        arr = (l.decode(FORMAT)).split(".")
        filename = arr[0] + "_received." + arr[1]
        
        with open(filename,"wb") as f:
            c.send(filename.encode(FORMAT))
            print("Receiving...")
            while (l):
                l = c.recv(1024)
                f.write(l)
                c.send(filename.encode(FORMAT))
            print("Done Receiving")
        c.close()
