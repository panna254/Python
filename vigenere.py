ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    ciphertext = ""
    for p, k in zip(plaintext, keyword_repeated):
        p_index = ALPHABET.index(p)
        k_index = ALPHABET.index(k)
        c_index = (p_index + k_index) % 26
        ciphertext += ALPHABET[c_index]
    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    plaintext = ""
    for c, k in zip(ciphertext, keyword_repeated):
        c_index = ALPHABET.index(c)
        k_index = ALPHABET.index(k)
        p_index = (c_index - k_index) % 26
        plaintext += ALPHABET[p_index]
    return plaintext

keyword = "BIGGER"
plaintext = "MAKING LEMONADES"
ciphertext = vigenere_encrypt(plaintext, keyword)
decrypted = vigenere_decrypt(ciphertext, keyword)
print(f"Keyword: {keyword}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
