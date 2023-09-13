import json
import sys
import zipfile
import datetime
import os
import csv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + "/files_topic_4/"


def the_three_socks_lemma():
    socks = list(int(line.strip("\n")) for line in sys.stdin.readlines())
    is_even = 1 if socks[-1] % 2 == 0 else 0
    if len(socks) % 2 == 0:
        name = ("Анри", "Дима")[is_even]
    else:
        name = ("Дима", "Анри")[is_even]
    print(name)


def statistics_lesson():
    lines = list(line.strip("\n") for line in sys.stdin.readlines())
    if not lines:
        print("нет учеников")
        return
    heights = list(map(int, lines))
    print(
        f"Рост самого низкого ученика: {min(heights)}\n"
        f"Рост самого высокого ученика: {max(heights)}\n"
        f"Средний рост: {sum(heights)/len(heights)}"
    )


def commentator():
    text = sys.stdin.read()
    lines = list(line.strip() for line in text.splitlines())
    count = 0
    for line in lines:
        if line.startswith("#"):
            count += 1
    print(count)


def no_comment():
    text = sys.stdin.read()
    lines = list(text.splitlines())
    for line in lines:
        if line.strip().startswith("#"):
            continue
        print(line)


def panoramic_agency():
    lines = list(line.strip("\n") for line in sys.stdin.readlines())
    news = list(line.split(" / ") for line in lines[:-1])
    filter_news = filter(lambda x: x[1] == lines[-1], news)
    for new in sorted(filter_news, key=lambda x: (float(x[2]), x[0])):
        print(new[0])


def its_definitely_python():
    lines = list(line.strip("\n") for line in sys.stdin.readlines())
    set_date = set(lines)
    if len(lines) != len(set_date):
        print("MIX")
        return
    pettern = "%d.%m.%Y"
    dates = list(datetime.datetime.strptime(line, pettern) for line in lines)
    sorted_dates_asc = sorted(dates)
    sorted_dates_desc = sorted(dates, reverse=True)
    if sorted_dates_asc == dates:
        print("ASC")
    elif sorted_dates_desc == dates:
        print("DESC")
    else:
        print("MIX")


def guru_of_progressions():
    nums = list(int(line.strip("\n")) for line in sys.stdin.readlines())
    firts_num = nums[0]
    two_num = nums[1]
    ratio = two_num - firts_num
    for index in range(1, len(nums)):
        if (nums[index] - nums[index - 1]) != ratio:
            break
    else:
        return f"Арифметическая прогрессия"
    ratio = two_num / firts_num
    for index in range(1, len(nums)):
        if (nums[index] / nums[index - 1]) != ratio:
            break
    else:
        return f"Геометрическая прогрессия"
    return f"Не прогрессия"


def discounts():
    with open(
        file=FILES_DIR + "sales.csv", mode="r", encoding="UTF-8"
    ) as csv_file:
        rows = csv.DictReader(csv_file, delimiter=";")
        for row in rows:
            if int(row["old_price"]) > int(row["new_price"]):
                print(row["name"])


def average_salary():
    with open(
        file=FILES_DIR + "salary_data.csv", mode="r", encoding="UTF-8"
    ) as csv_file:
        rows = list(csv.reader(csv_file, delimiter=";"))
    salary_company = {}
    for row in rows[1:]:
        name, salary = row
        if not name in salary_company:
            salary_company[name] = [0, 0]
        salary_company[name] = [
            salary_company[name][0] + int(salary),
            salary_company[name][1] + 1,
        ]
    average_salary = {}
    for key, val in salary_company.items():
        average_salary[key] = val[0] / val[1]
    sorted_avg_salary = sorted(average_salary, key=average_salary.get)
    print(*sorted_avg_salary, sep="\n")


def sorting_by_column():
    num_column = int(input()) - 1
    result = []
    with open(
        file=FILES_DIR + "deniro.csv", mode="r", encoding="UTF-8"
    ) as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        for row in rows:
            temp = []
            for word in row:
                if word.isdigit():
                    temp.append(int(word))
                else:
                    temp.append(word)
            result.append(temp)
    result = sorted(result, key=lambda x: x[num_column])
    for row in result:
        print(*row, sep=", ")


def csv_columns(filename: str):
    result = {}
    with open(file=filename, mode="r", encoding="UTF-8") as csv_file:
        rows = csv.DictReader(csv_file, delimiter=",")
        for row in rows:
            for key, val in row.items():
                if not key in result:
                    result[key] = []
                result[key].append(val)
    return result


def popular_domains():
    filename_out = "domain_usage.csv"
    result = {}
    with open(FILES_DIR + "data.csv", mode="r", encoding="UTF-8") as csv_file:
        rows = csv.DictReader(csv_file, delimiter=",")
        for row in rows:
            domain = row["email"].split("@")[1]
            result[domain] = result.get(domain, 0) + 1
    sorted_result = sorted(result)
    sorted_result = sorted(sorted_result, key=lambda x: result.get(x))
    rows = []
    for domain in sorted_result:
        rows.append({"domain": domain, "count": result[domain]})
    columns = ["domain", "count"]
    with open(
        FILES_DIR + filename_out, mode="w", encoding="UTF-8", newline=""
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns, delimiter=",")
        writer.writeheader()
        writer.writerows(rows)


def wi_fi_in_moscow():
    result = {}
    with open(FILES_DIR + "wifi.csv", mode="r", encoding="UTF-8") as csv_file:
        rows = csv.DictReader(csv_file, delimiter=";")
        for row in rows:
            result[row["district"]] = result.get(row["district"], 0) + int(
                row["number_of_access_points"]
            )
    sorted_result = sorted(result)
    sorted_result = sorted(
        sorted_result, key=lambda x: result.get(x), reverse=True
    )
    for row in sorted_result:
        print(f"{row}: {result[row]}")


def last_day_on_the_titanic():
    male_names = []
    female_names = []
    with open(
        file=FILES_DIR + "titanic.csv", mode="r", encoding="UTF-8"
    ) as csv_file:
        rows = csv.DictReader(csv_file, delimiter=";")
        for row in rows:
            if row["survived"] == "1" and float(row["age"]) < 18:
                if row["sex"] == "male":
                    male_names.append(row["name"])
                elif row["sex"] == "female":
                    female_names.append(row["name"])
    print(*male_names, sep="\n")
    print(*female_names, sep="\n")


def log_file():
    pattern = "%d/%m/%Y %H:%M"
    result = {}
    with open(
        file=FILES_DIR + "name_log.csv", mode="r", encoding="UTF-8"
    ) as csv_file:
        rows = csv.DictReader(csv_file, delimiter=",")
        for row in rows:
            email = row["email"]
            username = row["username"]
            dtime = datetime.datetime.strptime(row["dtime"], pattern)
            if not email in result:
                result[email] = []
            if result[email] == []:
                result[email] = (username, dtime)
            else:
                if dtime > result.get(email)[1]:
                    result[email] = (username, dtime)
    sorted_result = sorted(result)
    with open(
        file=FILES_DIR + "new_name_log.csv",
        mode="w",
        encoding="UTF-8",
        newline="",
    ) as csv_file:
        columns = ["username", "email", "dtime"]
        writer = csv.DictWriter(csv_file, fieldnames=columns, delimiter=",")
        writer.writeheader()
        for email in sorted_result:
            username = result[email][0]
            dtime = datetime.datetime.strftime(result[email][1], pattern)
            writer.writerow(
                {"username": username, "email": email, "dtime": dtime}
            )


def condense_csv(filename: str, id_name: str):
    result = []
    with open(file=filename, mode="r", encoding="UTF-8") as csv_file:
        lines = [line.strip("\n") for line in csv_file.readlines()]
    for line in lines:
        temp = {}
        o, t, p = line.split(",")
        temp[t] = p
        result.append((dict((id_name), (o)), temp))
    print(result)


def merging_objects():
    with open(
        file=FILES_DIR + "data1.json", mode="r", encoding="UTF-8"
    ) as file:
        data1: dict = json.load(file)
    with open(
        file=FILES_DIR + "data2.json", mode="r", encoding="UTF-8"
    ) as file:
        data2: dict = json.load(file)
    data1.update(data2)
    with open(
        file=FILES_DIR + "data_merge.json", mode="w", encoding="UTF-8"
    ) as file:
        json.dump(data1, file, indent=3)


def merging_objects2():
    with open(
        file=FILES_DIR + "data1.json", mode="r", encoding="UTF-8"
    ) as file:
        data1: dict = json.load(file)
    with open(
        file=FILES_DIR + "data2.json", mode="r", encoding="UTF-8"
    ) as file:
        data2: dict = json.load(file)
    data3: dict = data2.copy()
    for key, val in data1.items():
        if not data2.get(key):
            data3[key] = val
    with open(
        file=FILES_DIR + "data_merge.json", mode="w", encoding="UTF-8"
    ) as file:
        data_merge = json.dumps(data3)
        file.write(data_merge)


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


def count_files():
    name_file = FILES_DIR + "/workbook.zip"
    count = 0
    with zipfile.ZipFile(name_file, mode="r") as zip_file:
        info = zip_file.infolist()
        for name in info:
            if name.is_dir():
                continue
            count += 1
    print(count)


if __name__ == "__main__":
    merging_objects()
    # condense_csv('test.csv', 'ID')
    # sorting_by_column()
    # log_file()
    # last_day_on_the_titanic()
    # wi_fi_in_moscow()
    # popular_domains()
    # csv_columns()
    # average_salary()
    # discounts()
    # print(guru_of_progressions())
    # its_definitely_python()
    # panoramic_agency()
    # no_comment()
    # commentator()
    # statistics_lesson()
    # extract_this(FILES_DIR + 'workbook.zip', 'earth.jpg', 'exam.txt')
    # # formatted_output()
    # favorites()
    # the_best_indicator()
    # file_size()
    # count_files()
    # the_three_socks_lemma()
    pass
