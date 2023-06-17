import socket
from datetime import datetime
import string
import random

target_host="localhost"
target_port= 8888

#socket object and handler
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    #connect
    client.connect((target_host, target_port))

    #send data
    data = bytes(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n", 'UTF-8')
    client.sendall(data)

    #receive data
    response = client.recv(4096)

    name = datetime.now()

    letters = string.ascii_lowercase
    random_string = ' '.join(random.choice(letters) for i in range(4))

    #create a file handler for the data
    with open(f"{name}{random_string}.html", mode='w', encoding = 'UTF-8') as output:
        print(response.decode(), file=output)

print("Script exit")        
