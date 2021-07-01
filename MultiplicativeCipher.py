#Extended Euclidean Algorithm for finding modular inverse # it is assumed that gcd(k, n) = 1 otherwise the inverse of k will exist
def inv(k, n):
    q, r1, r2, r, t1, t2, t = (0, n, k, 0, 0, 1, 0
                               )  # r1=n r2=k initially t1=0 t2=1 while r2:
    q = r1 // r2  # q=n/k q=quotient
    r = r1 % r2  # r=n%k r=remainder
    t = t1 - q * t2
    r1 = r2
    r2 = r
    r = t1
    t1 = t2
    t2 = t
    return (t1 + n) % n


#a and b are the 2 keys used in affine cipher


#ENCRYPTION
def Multilicative_Encryption(plainText, K):
    encrypt_text = ""
    for c in plainText:
        asci = ord(c)
        value = 97 if asci >= 97 else 65
        encrypt_text += chr(value + (asci - value) * K % 26)
    return encrypt_text


#DECRYPTION
def Multilicative_Decryption(cypherText, K):
    decrypt_text = ""
    invK = inv(K, 26)
    for c in cypherText:
        asci = ord(c)
        value = 97 if asci >= 97 else 65
        decrypt_text += chr(value + (asci - value) * invK % 26)
    return decrypt_text


#MAIN_FUNCTION
if __name__ == "__main__":
    print("MULTIPLICATIVE CIPHER TECHNIQUE")
    plainText = input("Plain Text: ")
    K = int(input("Enter key: "))
    E = Multilicative_Encryption(plainText, K)
    D = Multilicative_Decryption(E, K)
    print("Original text: {}\nencrypt_text text: {}\ndecrypt_text text: {}".
          format(plainText, E, D))
