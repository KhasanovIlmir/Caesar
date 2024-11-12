#include <iostream>
#include <string>
#include <stdexcept>

std::string caesar_cipher(const std::string& text, int shift, const std::string& language = "en", const std::string& mode = "encrypt") {
    std::string result;

    int start_upper, end_upper, start_lower, end_lower;

    if (language == "en") {
        start_upper = 'A'; end_upper = 'Z';
        start_lower = 'a'; end_lower = 'z';
    }
    else if (language == "ru") {
        start_upper = 'А'; end_upper = 'Я';
        start_lower = 'а'; end_lower = 'я';
    }
    else {
        throw std::invalid_argument("Unsupported language. Choose 'en' for English or 'ru' for Russian.");
    }

    if (mode == "decrypt") {
        shift = -shift;
    }

    auto shift_char = [shift](char ch, int start, int end) {
        return static_cast<char>((static_cast<int>(ch) - start + shift) % (end - start + 1) + start);
        };

    for (char ch : text) {
        if (start_upper <= ch && ch <= end_upper) {
            result += shift_char(ch, start_upper, end_upper);
        }
        else if (start_lower <= ch && ch <= end_lower) {
            result += shift_char(ch, start_lower, end_lower);
        }
        else {
            result += ch;
        }
    }

    return result;
}

int main() {
    setlocale(LC_ALL, "Rus");
    std::string text;
    std::cout << "Введите текст: ";
    std::getline(std::cin, text);

    int shift;
    std::cout << "Введите сдвиг: ";
    std::cin >> shift;

    std::string language;
    std::cout << "Выберите язык (en/ru): ";
    std::cin >> language;

    std::string mode;
    std::cout << "Выберите режим (encrypt/decrypt): ";
    std::cin >> mode;

    try {
        std::cout << "Результат: " << caesar_cipher(text, shift, language, mode) << std::endl;
    }
    catch (const std::invalid_argument& e) {
        std::cout << e.what() << std::endl;
    }

    return 0;
}

