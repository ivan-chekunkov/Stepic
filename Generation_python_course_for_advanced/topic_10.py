def string_representation():
    nums = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    for num in [int(i) for i in input()]:
        print(nums[num], end=' ')


def information_about_training_courses():
    courses = {'CS101': ['3004', 'Хайнс', '8:00'],
               'CS102': ['4501', 'Альварадо', '9:00'],
               'CS103': ['6755', 'Рич', '10:00'],
               'NT110': ['1244', 'Берк', '11:00'],
               'CM241': ['1411', 'Ли', '13:00']}
    name = input()
    print(f'{name}: {courses[name][0]}, '
          f'{courses[name][1]}, {courses[name][2]}')


def a_set_of_messages():
    symbols = {".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
               "A": '2', "B": '22', "C": '222',
               "D": '3', "E": '33', "F": '333',
               "G": '4', "H": '44', "I": '444',
               "J": '5', "K": '55', "L": '555',
               "M": '6', "N": '66', "O": '666',
               "P": '7', "Q": '77', "R": '777', "S": '7777',
               "T": '8', "U": '88', "V": '888',
               "W": '9', "X": '99', "Y": '999', "Z": '9999',
               " ": '0'
               }
    text = input()
    for char in text:
        if char.upper() in symbols:
            print(symbols[char.upper()], end='')


def morse_code():
    letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
             '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
             '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----',
             '.----', '..---', '...--', '....-', '.....', '-....', '--...',
             '---..', '----.']
    result = {}
    for char in range(len(letters)):
        result[letters[char]] = morse[char]
    text = input().upper()
    for char in text:
        if char in result:
            print(result[char], end=' ')


def the_rarest_word():
    words = {}
    for word in input().split():
        word = word.strip('.,!?:;-').lower()
        words[word] = words.get(word, 0) + 1
    min_value = min(words.values())
    min_key = [key for key in words.keys() if words[key] == min_value]
    print(min(min_key))


def fixing_duplicates():
    letters = {}
    for letter in input().split():
        if letter in letters:
            print(f'{letter}_{letters[letter]}', end=' ')
            letters[letter] += 1
            continue
        letters[letter] = 1
        print(letter, end=' ')


def programmers_dictionary():
    terms = {}
    for _ in range(int(input())):
        term, decryption = input().split(': ')
        terms[term.lower()] = decryption
    for _ in range(int(input())):
        word = input().lower()
        if word in terms:
            print(terms[word])
        else:
            print('Не найдено')


def anagrams_1():
    letters_1 = {}
    letters_2 = {}
    for char in input():
        letters_1[char] = letters_1.get(char, 0) + 1
    for char in input():
        letters_2[char] = letters_2.get(char, 0) + 1
    if letters_1 == letters_2:
        print('YES')
    else:
        print('NO')


def anagrams_2():
    letters_1 = {}
    letters_2 = {}
    for char in input():
        if not char.isalpha():
            continue
        char = char.lower()
        letters_1[char] = letters_1.get(char, 0) + 1
    for char in input():
        if not char.isalpha():
            continue
        char = char.lower()
        letters_2[char] = letters_2.get(char, 0) + 1
    if letters_1 == letters_2:
        print('YES')
    else:
        print('NO')


def dictionary_of_synonyms():
    synonyms = {}
    for _ in range(int(input())):
        word_1, word_2 = list(input().split())
        synonyms[word_1] = word_2
    word = input()
    if word in synonyms:
        print(synonyms[word])
    else:
        if word in synonyms.values():
            for key in synonyms:
                if synonyms[key] == word:
                    print(key)
                    break


def countries_and_cities():
    cities = {}
    for _ in range(int(input())):
        country, *city = list(input().split())
        cities[country] = city
    for _ in range(int(input())):
        city = input()
        for country in cities:
            if city in cities[country]:
                print(country)


def phone_book():
    ph_book = {}
    for _ in range(int(input())):
        phone, name = list(input().split())
        name = name.lower()
        if name in ph_book:
            ph_book[name].append(phone)
        else:
            ph_book[name] = [phone]
    for _ in range(int(input())):
        name = input().lower()
        if name in ph_book:
            print(*ph_book[name])
        else:
            print('абонент не найден')


def secret_word():
    crypt = input()
    crypt_dict = {}
    for char in crypt:
        crypt_dict[char] = crypt_dict.get(char, 0) + 1
    text_dict = {}
    for _ in range(int(input())):
        char, num = input().split(': ')
        text_dict[num] = char
    for char in crypt:
        print(text_dict[str(crypt_dict[char])], end='')


if __name__ == '__main__':
    secret_word()
    # phone_book()
    # countries_and_cities()
    # dictionary_of_synonyms()
    # anagrams_2()
    # anagrams_1()
    # programmers_dictionary()
    # fixing_duplicates()
    # the_rarest_word()
    # morse_code()
    # a_set_of_messages()
    # information_about_training_courses()
    # string_representation()
