import base64
encoded=input('enter encoded base64 string: \n')
decoded=base64.b64decode(encoded)
print(decoded)
