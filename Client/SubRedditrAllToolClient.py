import socket
import time

host = '45.86.68.39'
port = 7787

print("INFO: Connecting")

print("INFO: You may now type in a subreddit and see if its included in /r/all")
print("INFO: type 'E' to close program, Checking is not capital sensitive.")
print("INFO: A suggestion is to comment on your target subreddit before checking due to how the tool searches.")
active = True
while active:
    response = input("Subreddit: ").lower()
    s = socket.socket()
    s.connect((host,port))
    print("INFO: Requesting server info")
    s.send(response.encode())
    recv = s.recv(1024).decode()
    if("1" == recv):
        print("INFO: " + response + " is opted into /r/all")
    else:
        print("INFO: " + response + " was not found out of " + recv + " results")
    s.close()
    


    
s.close()
