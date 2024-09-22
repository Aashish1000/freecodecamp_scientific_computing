text = "Hello Aashish"
shift = 10


def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ""

    for char in message.lower():
        if char ==  " ":
            encrypted_text += char
        
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print("Plain Text:", message)
    print("Encrypted Text:", encrypted_text)


caesar("Hello", shift)
caesar(text, 20)