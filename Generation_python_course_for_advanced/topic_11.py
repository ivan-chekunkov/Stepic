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
