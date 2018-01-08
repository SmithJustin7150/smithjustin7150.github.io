empty = ''
empty2 = ''
decipher = ''
def encrypt(anyString, empty, empty2):
    count = 0
    for i in (anyString):
        if count%2 == 0:
            empty = empty + 1
        else:
            empty2 = empty2 + 1
        count = count + 1
    cipher = empty + empty2
    return cipher

def decrypt(anyString, empty, empty2, decipher):
    empty = "HloWrd"
    empty2 = "el ol"
    emptyCount = 0
    empty2Count = 0
    for i in (empty):
        if emptyCount%2 == 0:
            decipher = decipher + 1
        else:
            for i in (empty2):
                if empty2Count%2 == 0:
                    decipher = decipher + 1
                else:
                    decipher = decipher
    return decipher

anyString = input("Type: ")
encrypt(anyString, empty, empty2)
enc = encrypt(anyString, empty, empty2)
print(enc)
