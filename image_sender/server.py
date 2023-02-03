import socket
import base64


IP = socket.gethostbyname(socket.gethostname()) # get the IP address of you'r computer
PORT = 9999
ADDR = (IP, PORT)
HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make the socket (wirless conniction)
s.bind(ADDR)
s.listen(5)

print("Wait for connections...")
conn, addr = s.accept()
print(f"connection from {addr}")


while True:
    msg = input("> ")

    with open(msg, "rb") as f:
        data = base64.b64encode(f.read()) # read the image
        base_image = data.decode('utf-8') # convert the image to a base64 format to send it to the client

    base_image = f"{len(base_image):<{HEADERSIZE}}" + base_image

    conn.send(base_image.encode("utf-8")) # send the image
