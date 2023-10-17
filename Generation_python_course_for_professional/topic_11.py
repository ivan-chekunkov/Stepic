import re
import sys
import keyword


def im_in_hell():
    def is_phone_number(phone):
        if phone[0:2] not in ("7-", "8-"):
            return False
        if not phone[2:5].isdigit():
            return False
        if phone[5] != "-":
            return False
        groups = phone[6:].split("-")
        if phone[0:2] == "7-":
            if len(groups) == 3:
                if (
                    len(groups[0]) == 3
                    and len(groups[1]) == len(groups[2]) == 2
                ):
                    chars = "".join(groups)
                    return all(c.isdigit() for c in chars)
        if phone[0:2] == "8-":
            if len(groups) == 2 and len(groups[0]) == len(groups[1]):
                return all(gr.isdigit() for gr in groups)
        return False

    def get_all_numbers(text):
        for c in range(len(text)):
            chunk = text[c : c + 15]
            if is_phone_number(chunk):
                yield chunk

    text = input()
    phone_number = set(get_all_numbers(text))
    print(*phone_number, sep="\n")


def im_in_hell2():
    def is_phone_number(phone):
        sample1, sample2 = list("7-***-***-**-**"), list("8-***-****-****")
        res = [phone[0]]
        for char in phone[1:]:
            if char == "-":
                res.append("-")
            if char.isdigit():
                res.append("*")
        if res[:15] == sample1 or res[:15] == sample2:
            return True
        return False

    def get_all_numbers(text):
        for c in range(len(text)):
            chunk = text[c : c + 15]
            if is_phone_number(chunk):
                yield chunk

    text = input()
    phone_number = get_all_numbers(text)
    print(*phone_number, sep="\n")
    pass


def phone_numbers():
    pattern = r"(\d+)[ -](\d+)[ -](\d+)"
    for line in sys.stdin.readlines():
        nums = re.search(pattern=pattern, string=line).groups()
        print(
            f"Код страны: {nums[0]}, "
            f"Код города: {nums[1]}, "
            f"Номер: {nums[2]}"
        )


def beegeek_online_school():
    pattern = r"_\d+[A-Za-z]*_?"
    for line in sys.stdin.readlines():
        match = re.search(pattern=pattern, string=line)
        if match:
            print("True")
        else:
            print("False")


def identical_syllables():
    pattern = r"\b(\w+)\1\b"
    for line in sys.stdin.readlines():
        match = re.search(pattern=pattern, string=line)
        if match:
            print(match.group())


def beegeek():
    pattern1 = r"bee.*bee"
    pattern2 = r"\bgeek\b"
    bee_counter, geek_counter = 0, 0
    for line in sys.stdin.readlines():
        match1 = re.search(pattern=pattern1, string=line)
        match2 = re.search(pattern=pattern2, string=line)
        if match1:
            bee_counter += 1
        if match2:
            geek_counter += 1
    print(bee_counter)
    print(geek_counter)


def popularity():
    pattern1 = r"(^beegeek.*beegeek$)|(^beegeek$)"
    pattern2 = r"(^beegeek)|(beegeek$)"
    pattern3 = r".+beegeek.+"
    sum_popularity = 0
    for line in sys.stdin.readlines():
        line = line.rstrip("\n")
        if re.search(pattern=pattern1, string=line):
            sum_popularity += 3
            continue
        if re.search(pattern=pattern2, string=line):
            sum_popularity += 2
            continue
        if re.search(pattern=pattern3, string=line):
            sum_popularity += 1
    print(sum_popularity)


def respect():
    text = input()
    pattern = (
        r"(Здравствуйте\.*)|(Доброе утро\.*)"
        r"|(Добрый день\.*)|(Добрый вечер\.*)"
    )
    match = re.match(pattern=pattern, string=text, flags=re.IGNORECASE)
    if match:
        print("True")
    else:
        print("False")


def social_network():
    pattern = r".*beegeek.*"
    count_mes = 0
    for line in sys.stdin.readlines():
        if re.search(pattern=pattern, string=line, flags=re.I | re.M):
            count_mes += 1
    print(count_mes)


def under_the_words():
    text = input()
    pattern = input()
    regex = r"\B{}\B".format(pattern)
    print(len(re.findall(regex, text)))


def words():
    text = input()
    pattern = input()
    regex = r"\b{}\b".format(pattern)
    print(len(re.findall(regex, text)))


def the_same_and_different():
    pattern = input()
    text = input()
    regex = r"\b{}(se|ze)\b".format(pattern[:-2])
    print(len(re.findall(regex, text, re.IGNORECASE)))


def the_same_and_different_2():
    pattern = input()
    text = input()
    regex = r"\b{}(or|our)\b".format(
        pattern[:-2] if pattern.endswith("or") else pattern[:-3]
    )
    print(len(re.findall(regex, text, re.IGNORECASE)))


def abbreviate(phrase):
    result = []
    regex = r"(\w|[A-Z])[a-z]*"
    result.extend(re.findall(regex, phrase))
    return "".join(result).upper()


def html():
    input_text = sys.stdin.read()
    regex = r"<a.+?\"(.+?)\">(.+?)</a>"
    for http, text in re.findall(regex, input_text):
        print("{}, {}".format(http, text))


def html_2():
    input_text = sys.stdin.read()
    regex = r"<\w.*?>"

    def tag_a(data):
        name = re.search(r"<(\w*)", data).group(1)
        atr = re.findall(r" (\S*?)=", data)
        return name, atr

    result = {}
    for text in re.findall(regex, input_text):
        name, atr = tag_a(text)
        if result.get(name, False):
            result[name] = list(set(result[name]).union(atr))
            continue
        result[name] = atr
    sort_res = sorted(result.keys())
    for name in sort_res:
        print(name, end=": ")
        atr = result[name]
        if atr:
            atr.sort()
            print(*atr, sep=", ", end="")
        print()


def normalize_jpeg(filename):
    return re.sub(
        r"jpeg$|jpg$", r"jpg", filename, flags=re.IGNORECASE | re.MULTILINE
    )


def normalize_whitespace(string):
    return re.sub(r" {2,}", r" ", string=string)


def keywords():
    reg_kwlist: list = sorted(
        keyword.kwlist, key=lambda x: len(x), reverse=True
    )
    regex = "|".join(reg_kwlist)
    print(re.sub(regex, r"<kw>", input(), flags=re.IGNORECASE))


if __name__ == "__main__":
    social_network()
    # respect()
    # popularity()
    # beegeek()
    # identical_syllables()
    # beegeek_online_school()
    # phone_numbers()
    # im_in_hell()
