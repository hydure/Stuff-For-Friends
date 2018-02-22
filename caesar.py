def encrypt(plainText, distance):
    code = ""
    for char in plainText:
        ordValue = ord(char)
        cipherValue = (ordValue + distance) % 127 # Gives remainder
        code += chr(cipherValue)
    print(code)
    return code

def decrypt(cyphertext, distance):
    code = ""
    for char in cyphertext:
        ordValue = ord(char)
        cipherValue = (ordValue - distance) % 127
        code += chr(cipherValue)
    print(code)

text = input("Enter plaintext: ")
distance = int(input("Enter distance: "))

cipher = encrypt(text, distance)
decrypt(cipher, distance)