def rail_fence_encrypt(plaintext, keyword):
    plaintext = plaintext.upper().replace(" ", "")
    num_rails = len(keyword)
    rails = [[] for _ in range(num_rails)]
    rail = 0
    direction = 1
    for char in plaintext:
        rails[rail].append(char)
        rail += direction
        if rail == num_rails:
            rail = num_rails - 2
            direction = -1
        elif rail == -1:
            rail = 1
            direction = 1
    ciphertext = ""
    for rail in rails:
        ciphertext += "".join(rail)
    return ciphertext

def rail_fence_decrypt(ciphertext, keyword):
    num_rails = len(keyword)
    length = len(ciphertext)
    rail_lengths = [0] * num_rails
    rail = 0
    direction = 1
    for i in range(length):
        rail_lengths[rail] += 1
        rail += direction
        if rail == num_rails:
            rail = num_rails - 2
            direction = -1
        elif rail == -1:
            rail = 1
            direction = 1
    rails = []
    start = 0
    for length in rail_lengths:
        rails.append(list(ciphertext[start:start + length]))
        start += length
    plaintext = []
    rail = 0
    direction = 1
    for _ in range(len(ciphertext)):
        plaintext.append(rails[rail].pop(0))
        rail += direction
        if rail == num_rails:
            rail = num_rails - 2
            direction = -1
        elif rail == -1:
            rail = 1
            direction = 1
    return "".join(plaintext)

keyword = "BIGGER"
plaintext = "MAKING LEMONADES"
ciphertext = rail_fence_encrypt(plaintext, keyword)
decrypted = rail_fence_decrypt(ciphertext, keyword)
print(f"Keyword: {keyword}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")