import socket
import PIL.Image as Image
import base64
import io

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (SERVER, PORT)
HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)


full_message = ""
new_msg = True

while True:
    msg = s.recv(16)
    if new_msg:
        msg_len = int(msg[:HEADERSIZE])
        new_msg = False
    
    
    full_message += msg.decode("utf-8")

    if len(full_message) - HEADERSIZE == msg_len:
        b = base64.b64decode(full_message[HEADERSIZE:])
        img = Image.open(io.BytesIO(b)) # convert the base64 to the image data and open the image
        img.show()
        new_msg = True
        full_message = ""

