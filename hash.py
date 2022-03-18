import hashlib
string = "Good morning "
sha = hashlib.new('sha1')
sha.update(string.encode())
print(sha.hexdigest())