from enum import Enum
from itertools import combinations
from typing import List


class Form(Enum):
    romb = 'р'
    oval = 'о'
    volna = 'в'


class Color(Enum):
    red = 'к'
    purple = 'ф'
    green = 'з'


class Filling(Enum):
    full = 'ц'
    empty = 'п'
    hatch = 'ш'


class Card:
    def __init__(self, form: Form, color: Color, count: int, filling: Filling):
        self.form = form
        self.color = color
        self.count = count
        self.filling = filling

    def format(self) -> str:
        return '{}{}{}{}'.format(self.form.value, self.color.value, self.count, self.filling.value)

    def __eq__(self, other: 'Card'):
        return self.form == other.form and self.color == other.color and self.count == other.count


def foo():
    card_list = _parse_input_card_list()
    comb = list(combinations(card_list, 3))
    for card1, card2, card3 in comb:
        if not (card1.form == card2.form == card3.form) \
                and not (card1.form != card2.form and card1.form != card3.form and card2.form != card3.form):
            continue

        if not (card1.color == card2.color == card3.color) \
                and not (card1.color != card2.color and card1.color != card3.color and card2.color != card3.color):
            continue

        if not (card1.count == card2.count == card3.count) \
                and not (card1.count != card2.count and card1.count != card3.count and card2.count != card3.count):
            continue

        if not (card1.filling == card2.filling == card3.filling) \
                and not (card1.filling != card2.filling and card1.filling != card3.filling and card2.filling != card3.filling):
            continue

        print('{} {} {}'.format(card1.format(), card2.format(), card3.format()))

    print('finish')
    a = input()


def _parse_input_card_list() -> List[Card]:
    count = int(input())
    card_list = []
    for _ in range(count):
        card = input()
        card_list.append(Card(form=Form(card[0]), color=Color(card[1]), count=int(card[2]), filling=Filling(card[3])))
    return card_list


foo()
