alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Результат : {output_text}")


should_continue = True
while should_continue:

    direction = input("Для шифрования введите 'encode' для рассшифровки введите 'decode':\n").lower()
    text = input("Введите свое сообщение:\n").lower()
    shift = int(input("Введите номер смещения:\n"))
    print(f"Вы сместились {shift} в {direction}d направлении.")
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Введите 'yes' если хотите продолжить.В другом случае введите'no'.\n").lower()
    if restart == "no":
        should_continue = False
    
