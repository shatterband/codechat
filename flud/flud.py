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

def createkey(x = ''):
    import random

    file = open(x + 'keycode.rbmk', 'w')
    i = 4096
    writeb = ''
    while i:
        writeb += str(random.randint(0, 1))
        i = i - 1
    file.write(writeb)
    file.close()
print('###HELLO###')
print('Welcome to codechat. That program send messanges to all ip on one of port. If you wanna begin write "start", if you wanna generate new keycode write "generate"')
wish = input('##:')
if wish == 'generate':
    createkey()

print('Please coose the port for sending messages')
port = int(input('enter port :>>'))

print('If you wanna close the chat write "//exit"')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while 1:
        message = input(' :>>')
        if message == '//exit':
            break
        message = text_to_bits(message)
        message = bits_to_codebits(message)
        message = bytes(message, encoding='ASCII')
        sock.sendto(message,('255.255.255.255',port))
