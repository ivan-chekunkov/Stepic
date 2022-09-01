def divisibility_predicate():
    def function_divisibility_predicate(number_one, number_two):
        if number_one % number_two == 0:
            return True
        return False

    number_one = int(input())
    number_two = int(input())
    if function_divisibility_predicate(number_one, number_two):
        print('делится')
    else:
        print('не делится')


if __name__ == '__main__':
    # divisibility_predicate()
    pass
