import socket
from encryption import text_to_bits, text_from_bits, bits_to_codebits, createkey, readkey, chngstr

print('###HELLO###')
print('Welcome to codechat. That program send messanges to all ip on one port. If you wanna begin write "start", if you wanna generate new keycode write "generate"')
wish = input('##:')
if wish == 'generate':
    createkey()

print('Please coose the port for sending messages')
port = int(input('enter port :>>'))

print('If you wanna close the chat write "//exit"')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

x = readkey()
keycode = x[0]
rule = ord(text_from_bits(x[1]))

while 1:
        message = input(' :>>')
        if message == '//exit':
            break
        message = text_to_bits(message)
        message = bits_to_codebits(message, keycode, rule)
        message = bytes(message, encoding='ASCII')
        sock.sendto(message,('255.255.255.255',port))
        keycode = chngstr(keycode, rule)
        print('resived')
    
