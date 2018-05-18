import socket
import sys
import os
import random, struct

from Crypto.Cipher import AES
import base64

key = "1111111111111111";


#encrypt file:
"""
o_fn = 0;
if not o_fn:
    o_fn = sys.argv[2] + '.enc';

iv = "1234567891234567" #''.join(chr(random.randint(0, 0xFF)) for i in range(16));
encryptor = AES.new(key, AES.MODE_CBC, iv);

filesize = os.path.getsize(sys.argv[2]);

with open(sys.argv[2], 'rb') as infile:
    with open(o_fn, 'wb') as outfile:
        outfile.write(struct.pack('<Q', filesize));
        outfile.write(iv);

        while True:
            chunk = infile.read(1024);
            if len(chunk) == 0:
                break;
            elif len(chunk) % 16 != 0:
                chunk += ' ' * (16 - len(chunk) % 16);

            outfile.write(encryptor.encrypt(chunk));
"""
#-----


def read_file(f):
    while True:
        data = f.read(1024);
        if not data:
            break;
        yield data;

if len(sys.argv) < 2:
    print("usage:");
    sys.exit(1);

print("sending file: " + sys.argv[2] + " to " + sys.argv[1] + "::5000");

client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM);

client.connect((sys.argv[1], 5000,  0, 0));

total_size = os.path.getsize(sys.argv[2]);

total_sent = 0;

f = open(sys.argv[2], "rb");

for chunk in read_file(f):
    total_sent = total_sent + len(chunk);
    print("sent: " + str(total_sent) + " | " + str(total_size));

    client.send(chunk);


f.close();

print("finished sending file");
