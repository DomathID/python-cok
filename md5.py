import hashlib
mystring = input('word: ')
hash_obj = hashlib.md5(mystring.encode())
print(hash_obj.hexdigest())
