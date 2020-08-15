from Crypto.Cipher import DES
import base64
rock = open("./rockyou.txt").read().splitlines()
flag=base64.b64decode("kIi6qSDhcSVErHbkpy/M1hRHfDpr8TiaGbAIrKUXooxSXwNnaeJgTQ==")
for key in rock :
    if len(key) == 8 :
        cipher = DES.new(key , DES.MODE_ECB)
        txt=cipher.decrypt(flag)
        if txt.startswith(b'ASCTF{'):
            print(txt)
            print(key)
            break