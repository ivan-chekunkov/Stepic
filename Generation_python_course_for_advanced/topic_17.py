import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_17/'


def a_gift_for_the_new_year():
    with open(FILES_DIR + 'class_scores.txt', 'r') as file:
        lines = file.readlines()
    with open(FILES_DIR + 'new_scores.txt', 'w') as file:
        for line in lines:
            name, score = line.split()
            score = int(score) + 5
            if score > 100:
                score = 100
            file.write(f'{name} {score}\n')
