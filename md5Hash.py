from Crypto.Cipher import AES
key = 'abcdefghijklmnop'
cipher = AES.new(key, AES.MODE_ECB)
msg =cipher.encrypt('Hello World~ Good To See You!!!!')
print (type(msg))
print(msg)
decipher = AES.new(key, AES.MODE_ECB)
print(decipher.decrypt(msg))