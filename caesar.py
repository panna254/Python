def caesar_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    shifted_alphabet_upper = alphabet_upper[key:] + alphabet_upper[:key]
    
    table = str.maketrans(alphabet + alphabet_upper, shifted_alphabet + shifted_alphabet_upper)
    return text.translate(table).replace(' ', '')  # Exclude spaces


action = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
text = input("Enter the text: ")

try:
    key = int(input("Enter the key (must be a positive integer): "))
    if key < 0:
        print("Invalid key. Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid key. Please enter a valid integer.")
    exit()

if action == "e":
    result = caesar_cipher(text, key)
    print(f"Encrypted: {result}")
elif action == "d":
    result = caesar_cipher(text, -key)
    print(f"Decrypted: {result}")
else:
    print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
