import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = BASE_DIR + '/files_topic_2/'


def hide_card(card_number: str) -> str:
    card_number = card_number.replace(' ', '')
    return '*'*12+card_number[12:]
