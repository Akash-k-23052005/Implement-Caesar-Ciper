def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decrypted += char
    return decrypted

# User interaction
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

enc = caesar_encrypt(message, shift)
print("Encrypted:", enc)

dec = caesar_decrypt(enc, shift)
print("Decrypted:", dec)
