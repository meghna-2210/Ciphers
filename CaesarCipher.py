def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


#check the above function
if __name__ == "__main__":
    print("MEGHNA | 2018UCO1564 | INS")
    print("---------------------------")
    text = input("Enter text: ")
    shift = int(input("Enter s:"))
    cipher = encrypt(text, shift)
    print("Cipher:", cipher)
    shift = shift % 26
    # ensuring that shift lies between 0-25
    print("Decrypted Text:", encrypt(cipher, 26 - shift))
