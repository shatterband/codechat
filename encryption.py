
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

def chngstr(stg, rule):

    if rule > 255 or rule < 0:
        raise NameError('rule is not in 0 - 255')
    rule = text_to_bits(chr(rule))

    string = stg[-1] + stg + stg[0]

    _string = ''
    for x in range(len(stg)):
        if string[x] == '1' and string[x+1] == '1' and string[x+2] == '1':
             _string += rule[0]
        elif string[x] == '1' and string[x+1] == '1' and string[x+2] == '0':
             _string += rule[1]
        elif string[x] == '1' and string[x+1] == '0' and string[x+2] == '1':
             _string += rule[2]
        elif string[x] == '1' and string[x+1] == '0' and string[x+2] == '0':
             _string += rule[3]
        elif string[x] == '0' and string[x+1] == '1' and string[x+2] == '1':
             _string += rule[4]
        elif string[x] == '0' and string[x+1] == '1' and string[x+2] == '0':
             _string += rule[5]
        elif string[x] == '0' and string[x+1] == '0' and string[x+2] == '1':
             _string += rule[6]
        elif string[x] == '0' and string[x+1] == '0' and string[x+2] == '0':
             _string += rule[7]
    return _string



