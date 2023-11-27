alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ceasar(text, shift_amount, action):
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if action == "encode":
                new_position = (position + shift_amount) % 26
            elif action == "decode":
                new_position = (position - shift_amount) % 26
            result += alphabet[new_position]
        else:
            result += letter
    return result

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypted_text = ceasar(text, shift, "encode")
        print(f"The encoded text is {encrypted_text}")
    elif direction == "decode":
        decrypted_text = ceasar(text, shift, "decode")
        print(f"The decoded text is {decrypted_text}")

    user_choice = input("Do you want to continue? Write 'y' or 'n': ")
    if user_choice != 'y':
        break