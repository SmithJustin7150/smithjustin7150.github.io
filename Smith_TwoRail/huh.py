"""
string = "Hello world"
empty = ''

def encrypt(AnyString, empty):
    for i in (AnyString):
        x = ord(i)
        y = chr(x)
        empty = empty + y
    return empty

message = (encrypt(string, empty))
"""

string2 = "Hello World"
empty2 = ''

def decrypt(AnyString, empty2):
    for i in (AnyString):
        x = ord(i)
        y = chr(x)
        empty2 = empty2 + y
    return decrypt
print (decrypt(string2, empty2))
