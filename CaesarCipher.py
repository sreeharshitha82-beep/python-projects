SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher Hacker')
print('Enter the encrypted message:')
message = input('> ')

for key in range(len(SYMBOLS)):
    text = ''

    for char in message:
        if char in SYMBOLS:
            pos = SYMBOLS.find(char)
            pos -= key

            if pos < 0:
                pos += len(SYMBOLS)

            text += SYMBOLS[pos]
        else:
            text += char

    print('Key {}: {}'.format(key, text))