from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']


def caesar(start_text, shift_amount,
           cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            elif cipher_direction == "decode":
                new_position = position - shift_amount
                end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}.")


print(logo)

should_continue = True
while should_continue:
    direction = input(
        "Type 'encode' to encrypt your message and 'decode' to decrypt your message:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if result == "no":
        should_continue = False
        print("End of the program. Goodbye.")
