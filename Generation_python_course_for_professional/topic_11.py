def im_in_hell():

    def is_phone_number(phone):
        if phone[0:2] not in ('7-', '8-'):
            return False
        if not phone[2:5].isdigit():
            return False
        if phone[5] != '-':
            return False
        groups = phone[6:].split('-')
        if phone[0:2] == '7-':
            if len(groups) == 3:
                if len(groups[0]) == 3 and len(groups[1]) == len(groups[2]) == 2:
                    chars = ''.join(groups)
                    return all(c.isdigit() for c in chars)
        if phone[0:2] == '8-':
            if len(groups) == 2 and len(groups[0]) == len(groups[1]):
                return all(gr.isdigit() for gr in groups)
        return False

    def get_all_numbers(text):
        for c in range(len(text)):
            chunk = text[c:c + 15]
            if is_phone_number(chunk):
                yield chunk

    text = input()
    phone_number = set(get_all_numbers(text))
    print(*phone_number, sep='\n')


def im_in_hell2():

    def is_phone_number(phone):
        sample1, sample2 = list('7-***-***-**-**'), list('8-***-****-****')
        res = [phone[0]]
        for char in phone[1:]:
            if char == '-':
                res.append('-')
            if char.isdigit():
                res.append('*')
        if res[:15] == sample1 or res[:15] == sample2:
            return True
        return False

    def get_all_numbers(text):
        for c in range(len(text)):
            chunk = text[c:c + 15]
            if is_phone_number(chunk):
                yield chunk

    text = input()
    phone_number = get_all_numbers(text)
    print(*phone_number, sep='\n')
    pass
