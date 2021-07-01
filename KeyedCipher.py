import string
import secrets


def convert_to_int(key):
    key = list(key)
    return [int(k) for k in key]


def permuteGrid(grid, key):
    numRows, numCols = len(grid), len(grid[0])
    gridPerm = [[''] * numCols for i in range(numRows)]
    for r in range(numRows):
        for idx, val in enumerate(key):
            gridPerm[r][idx] = grid[r][val - 1]

    return gridPerm


def invertKey(key):
    idx = 1
    invKey = [0] * len(key)

    for i in range(len(key)):
        invKey[key[i] - 1] = 1 + i

    return invKey


def encryptKeyed(plainText, k):
    k = convert_to_int(k)
    l = len(plainText)
    numCols = len(k)
    numRows = (l + numCols - 1) // numCols

    plainText += ''.join(
        secrets.choice(string.ascii_letters)
        for i in range(numCols * numRows - l))
    print(plainText)

    numRows += 1
    grid = [[''] * numCols for i in range(numRows)]

    for i in range(numCols):
        grid[0][i] = 1 + i

    idx = 0
    for r in range(1, numRows):
        for c in range(numCols):
            grid[r][c] = plainText[idx]
            idx += 1

    gridPerm = permuteGrid(grid, k)
    E = ""

    for col in range(numCols):
        for row in range(1, numRows):
            E += gridPerm[row][col]

    return E


def decryptKeyed(cipherText, k):
    k = invertKey(convert_to_int(k))

    l = len(cipherText)
    numCols = len(k)
    numRows = 1 + l // numCols

    grid = [[''] * numCols for i in range(numRows)]
    gridPerm = [[''] * numCols for i in range(numRows)]

    for i in range(numCols):
        grid[0][i] = 1 + i
    idx = 0
    for c in range(numCols):
        for r in range(1, numRows):
            grid[r][c] = cipherText[idx]
            idx += 1

    gridPerm = permuteGrid(grid, k)
    D = ""

    for r in range(1, numRows):
        for c in range(numCols):
            D += gridPerm[r][c]

    return D


# Driver code
if __name__ == "__main__":
    plain_text = input('Enter the string to be encrypted: ')
    key = input("Enter the key: ")
    cipher = encryptKeyed(plain_text, key)
    print("Encrypted Message: {}".format(cipher))
    print("Decrypted Message: {}".format(decryptKeyed(cipher, key)))
