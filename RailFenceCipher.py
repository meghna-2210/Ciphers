# function to encrypt a message
def encryptRailFence(text, key):

    # create the matrix to cipher
    # key(number of rails) = rows ,
    # length(plain_text) = columns
    # rail matrix
    rail = [['\n' for i in range(len(text))] for j in range(key)]

    # to find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):

        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("".join(result))


def decryptRailFence(cipher, key):

    rail = [['\n' for i in range(len(cipher))] for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    # read the matrix in zig-zag manner to construct the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))


# Driver code
if __name__ == "__main__":
    plain_text = input('Enter the string to be encrypted: ')
    n = int(input('Enter the number of rails: '))
    #encryption of cipher-text
    encrypt_text = encryptRailFence(plain_text, n)
    print('Encrypted Text: ')
    print(encrypt_text)

    # decryption of the same cipher-text
    print('Decrypted Text: ')
    decrypt_text = decryptRailFence(encrypt_text, n)
    print(decrypt_text)
