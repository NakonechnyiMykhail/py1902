print(b'bytes')

print('байты'.encode('utf-8'))
print(b'\xd0\xb1\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))

print(chr(100)) # d
print(chr(1076)) # д

print(bytes('bytes', encoding='utf-8'))
print(bytes('байты', encoding='utf-8'))

print(bytes([72, 101, 108, 108, 111, 33]))
