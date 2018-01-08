"""
def encrypt(plainText):

    evens = ''
    odds = ''

    charCount = 0
    for ch in plainText:
        if charCount % 2 is 0:
            evens = evens + ch
        else:
            odds = odds + ch

        charCount = charCount + 1

    cipherText = odds + evens
        
    return cipherText

msg = encrypt('Two Rail Cipher')

print(msg)
"""


def decrypt(plainText):

    evens = ''
    odds = ''

    characters = 0
    for ch in plainText:
        if characters % 2 is 0:
            odds = odds + ch
        else:
            evens = evens + ch

        characters = characters - 1

    cipherText = evens + odds

    return cipherText

msg = decrypt('w alCpeToRi ihr')

print(msg)
