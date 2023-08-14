alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift_amount) % 26
                cipher_text += alphabet[new_position]
            else:
                cipher_text += letter
        print(f"The encoded text is {cipher_text}")

    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for letter in cipher_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position - shift_amount) % 26
                plain_text += alphabet[new_position]
            else:
                plain_text += letter
        print(f"The decoded text is {plain_text}")

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, shift_amount=shift)

    user_choice = input("Do you want to continue? Write 'y' or 'n': ")
    if user_choice != 'y':
        break