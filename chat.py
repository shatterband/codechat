import socket
from encryption import text_to_bits, text_from_bits, bits_to_codebits, createkey

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
