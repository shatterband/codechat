import socket

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def bits_to_codebits(bits):
    codebits = ''
    key = open('keycode.rbmk', 'r')
    keycode = key.read()
    for x in range(len(bits)):
        if keycode[x] == '1':
            codebits = codebits + str(int(not(int(bits[x]))))
        elif keycode[x] == '0':
            codebits = codebits + bits[x]
    return codebits

print('###HELLO###')
print('Welcome to chatreader. That program read one port all time and write messages. Please enter port')
port = int(input('enter port :>>'))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0',port))
while 1:
	message = s.recv(512)
	message = message.decode('ASCII')
	message = bits_to_codebits(message)
	message = text_from_bits(message)
	print('###|', message)
