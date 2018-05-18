import socket
import os
import random, struct

from Crypto.Cipher import AES
import base64

key = "1111111111111111";


print("starting server");

"""
addrinfo = socket.getaddrinfo(None, "", 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE);

for add in addrinfo:
    print(add);

server = socket.socket(add[0], add[1], add[2]);

if add[0] == socket.AF_INET6:
    server.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1);

server.bind(add[4]);
"""

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM);
server.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1);

server.bind(("::1", 5000));

server.listen(2);

client, address = server.accept();

print("client connected to server");

f = open("recv.data" , "wb");

total_received = 0;

while True:
    data = client.recv(1024);

    if not data:
        break;

    total_received = total_received + len(data);
    print("received: " + str(total_received));

    f.write(data);

f.close();

#decrypt file


"""
with open("recv.data.enc", 'rb') as infile:
    origsize = struct.unpack('<Q', infile.read(struc.calcsize('Q')))[0];
    iv = infile.read(16);
    decryptor = AES.new(key, AES.MODE_CBC, iv);

    with open("recv.data", 'wb') as outfile:
        while True:
            chunk = infile.read(1024);
            if len(chunk) == 0:
                break;
            outfile.write(decryptor.decrypt(chunk));

        outfile.truncate(origsize);
"""
#-----

"""
f = open("recv.enc", "rb");
f_d = open("recv.data", "wb");


chunk = bytearray(64);
print(chunk);

f_size = os.path.getsize("recv.enc");

while True:
    chunk = f.read(64);

    if not chunk:
        break;

    print(chunk);

    print("processing");

    print("f_size: " + str(f_size));

    if len(chunk) == 64 and f_size >= 64:
        chunk = cipher.decrypt(base64.b64decode(chunk));

    f_size = f_size - len(chunk);

    f_d.write(chunk);


print("recevied complete file");

f.close();

    
"""
