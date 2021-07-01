#ENCRYPTION
def additive_Encryption(plainText, Key):
    encrypt_text = ""
    for i in plainText:
        asci = ord(i)
        value = 97 if asci >= 97 else 65
        encrypt_text += chr(value + (asci - value + Key) % 26)
    return encrypt_text


#DECRYPTION
def additive_Decryption(cypherText, Key):
    decrypt_text = ""
    for i in cypherText:
        asci = ord(i)
        value = 97 if asci >= 97 else 65
        decrypt_text += chr(value + (asci - value - Key) % 26)
    return decrypt_text


#MAIN_FUNCTION
if __name__ == "__main__":
    print("ADDITIVE/CAESAR CIPHER TECHNIQUE")
    plainText = input("Plain Text: ")
    K = int(input("Enter the key: "))
    E = additive_Encryption(plainText, K)

    D = additive_Decryption(E, K)
    print("Original text: {}\nencrypt_text text: {}\ndecrypt_text text: {}".
          format(plainText, E, D))
