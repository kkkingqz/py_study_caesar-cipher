message = 'zZvVaaabbbbccHello, world!'
offset = 33
encoded_message = ''

for ch in message:
    if ord(ch) in range(ord('a'), ord('z')+1):
        pos = (ord(ch) - ord('a') + offset) % 26
        new_char = chr(pos + ord('a'))
    elif ord(ch) in range(ord('A'), ord('Z')+1):
        pos = (ord(ch) - ord('A') + offset) % 26
        new_char = chr(pos + ord('A'))
    else:
        new_char = ch
    encoded_message += new_char

print(encoded_message)
