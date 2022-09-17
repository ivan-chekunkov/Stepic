def a_minute_of_genetics():
    DNK_IN_RNA = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    dnk = input()
    for i in dnk:
        print(DNK_IN_RNA[i], end='')


def serial_number():
    words = {}
    text = input().split()
    for word in text:
        words[word] = words.get(word, 0) + 1
        print(words[word], end=' ')


def scrabble_game():
    table_score = {
        1: 'AEILNORSTU',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ'
    }
    score = 0
    for char in input():
        for key, v in table_score.items():
            if char in v:
                score += key
                break
    print(score)


def build_query_string(params):
    mas = list(str(k) + '=' + str(v) for k, v in params.items())
    mas.sort()
    result = '&'.join(i for i in mas)
    return result


def merging_dictionaries(values):
    values = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100},
              {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
    result = {}
    for sl in values:
        for k, v in sl.items():
            if result.get(k):
                result[k].add(v)
            else:
                result[k] = set()
                result[k].add(v)
    return result


def dangerous_virus():
    commands = {
        'execute': 'X',
        'read': 'R',
        'write': 'W',
    }
    virus_files = {}
    for _ in range(int(input())):
        file, *atr = input().split()
        virus_files[file] = set(atr)
    for _ in range(int(input())):
        command, file = input().split()
        atr = virus_files[file]
        command = commands[command]
        if command in atr:
            print('OK')
            continue
        print('Access denied')


def shopping_in_the_online_store():
    shopping = {}
    for _ in range(int(input())):
        name, product, count = input().split()
        if name in shopping:
            if product in shopping[name]:
                shopping[name][product] += int(count)
            else:
                shopping[name][product] = int(count)
        else:
            shopping[name] = {product: int(count)}
    names = list(shopping.keys())
    names.sort()
    for name in names:
        print(f'{name}:')
        products = list(shopping[name].keys())
        products.sort()
        for product in products:
            print(f'{product} {shopping[name][product]}')


def shopping_in_the_online_store_v2():
    data = {}
    for _ in range(int(input())):
        name, product, count = input().split()
        data.setdefault(name, {})
        data[name][product] = data[name].get(product, 0) + int(count)
    for person, products in sorted(data.items()):
        print(f'{person}:')
        for product, count in sorted(products.items()):
            print(product, count)


if __name__ == '__main__':
    shopping_in_the_online_store()
    # dangerous_virus()
    # merging_dictionaries()
    # print(build_query_string({'name': 'timur', 'age': 28}))
    # build_query_string()
    # scrabble_game()
    # serial_number()
    # a_minute_of_genetics()
    pass
