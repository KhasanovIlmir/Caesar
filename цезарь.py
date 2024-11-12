def caesar_cipher(text, shift, language='en', mode='encrypt'):
    result = ''


    if language == 'en':
        start_upper, end_upper = ord('A'), ord('Z')  
        start_lower, end_lower = ord('a'), ord('z') 
    elif language == 'ru':
        start_upper, end_upper = ord('А'), ord('Я')  
        start_lower, end_lower = ord('а'), ord('я')  
    else:
        raise ValueError("Unsupported language. Choose 'en' for English or 'ru' for Russian.")

    
    if mode == 'decrypt':
        shift = -shift

    
    def shift_char(char, start, end):
        return chr((ord(char) - start + shift) % (end - start + 1) + start)

    for char in text:
        if start_upper <= ord(char) <= end_upper:  
            result += shift_char(char, start_upper, end_upper)
        elif start_lower <= ord(char) <= end_lower:  
            result += shift_char(char, start_lower, end_lower)
        else:
            
            result += char

    return result


text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
language = input("Выберите язык (en/ru): ").strip().lower()
mode = input("Выберите режим (encrypt/decrypt): ").strip().lower()


try:
    print("Результат:", caesar_cipher(text, shift, language, mode))
except ValueError as e:
    print(e)
