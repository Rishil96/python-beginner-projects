# Caesar Cipher
import art

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# Encryption function
def encrypt(original_text, shift):
    encrypted_text = ""
    # Encrypt each letter from the alphabet
    for letter in original_text:
        if letter in alphabet:
            # Find index and loop it back inside valid alphabet index range using % 26
            encrypt_index = (alphabet.index(letter) + shift) % len(alphabet)
            encrypted_text += alphabet[encrypt_index]
        else:
            # Don't encrypt letter if not a valid alphabet letter
            encrypted_text += letter

    print(f"Encrypted Text: {encrypted_text}")


# Decryption function
def decrypt(original_text, shift):
    decrypted_text = ""
    for letter in original_text:
        print(letter)
        if letter in alphabet:
            # Find index and loop it back inside valid alphabet index range using % 26
            decrypt_index = (alphabet.index(letter) - shift) % len(alphabet)
            decrypted_text += alphabet[decrypt_index]
        else:
            # Don't decrypt letter if not a valid alphabet letter
            decrypted_text += letter

    print(f"Decrypted Text: {decrypted_text}")


# Caesar function that does both encryption and decryption based on direction
def caesar(original_text, shift, direction):

    # Based on direction we either add or subtract the shift amount so change it accordingly
    if direction == "decode":
        shift = -shift

    output_text = ""
    # Encrypt/Decrypt each letter from the alphabet
    for letter in original_text:
        if letter in alphabet:
            # Find index and loop it back inside valid alphabet index range using % 26
            encrypt_index = (alphabet.index(letter) + shift) % len(alphabet)
            output_text += alphabet[encrypt_index]
        else:
            # Don't encrypt/decrypt letter if not a valid alphabet letter
            output_text += letter

    print(f"{direction.title()}d Text: {output_text}")


# Main Code
is_on = True

while is_on:
    print(art.logo)
    type_of_encryption = input("Type \"encode\" to encrypt, type \"decode\" to decrypt: ").lower()

    if type_of_encryption not in ["encode", "decode"]:
        print("Invalid type of encryption added. Try again.")
        exit()

    text = input("Type your message:\n").lower()
    shift_number = int(input("Type your shift number:\n"))

    caesar(original_text=text, shift=shift_number, direction=type_of_encryption)

    restart = input("Do you want to continue using Caesar Cipher or exit. Type \"yes\" or \"no\": ")
    if restart == "yes":
        continue
    else:
        is_on = False
        print("Thanks for using Caesar Cipher! Goodbye.")
