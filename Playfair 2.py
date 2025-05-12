ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def prepare_playfair_key(keyword):
    keyword = keyword.upper().replace("J", "I")
    key = []
    for char in keyword:
        if char not in key and char in ALPHABET:
            key.append(char)
    for char in ALPHABET:
        if char not in key:
            key.append(char)
    return [key[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair_encrypt(plaintext, keyword):
    matrix = prepare_playfair_key(keyword)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    ciphertext = ""
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext):
            char1, char2 = plaintext[i], plaintext[i+1]
            i += 2
        else:
            char1, char2 = plaintext[i], None
            i += 1
        row1, col1 = find_position(matrix, char1)
        if char2 is None:
            ciphertext += char1
        else:
            row2, col2 = find_position(matrix, char2)
            if char1 == char2:
                ciphertext += char1 + char2
            elif row1 == row2:
                ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext, matrix

def playfair_decrypt(ciphertext, keyword):
    matrix = prepare_playfair_key(keyword)
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if i + 1 < len(ciphertext):
            char1, char2 = ciphertext[i], ciphertext[i+1]
            i += 2
        else:
            char1, char2 = ciphertext[i], None
            i += 1
        row1, col1 = find_position(matrix, char1)
        if char2 is None:
            plaintext += char1
        else:
            row2, col2 = find_position(matrix, char2)
            if char1 == char2:
                plaintext += char1 + char2
            elif row1 == row2:
                plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

keyword = "MUSAH"
plaintext = "THESE TOUGH TIMES TOO SHALL PASS"
ciphertext, matrix = playfair_encrypt(plaintext, keyword)
decrypted = playfair_decrypt(ciphertext, keyword)
print("Playfair Cipher 5x5 Matrix (Keyword: MUSAH):")
for row in matrix:
    print(" ".join(row))
print(f"\nKeyword: {keyword}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
