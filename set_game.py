from random import randint

NUMBERS = [1, 2, 3]
SYMBOLS = ["DIAMOND", "SQUIGGLE", "OVAL"]
SHADINGS = ["STRIPPED", "SOLID", "OPEN"]
COLORS = ["RED", "GREEN", "PURPLE"]

no_error_args =  NUMBERS[randint(0, 2)], SYMBOLS[randint(0, 2)], SHADINGS[randint(0, 2)], COLORS[randint(0, 2)]
error_args_1 = 5, SYMBOLS[randint(0, 2)], SHADINGS[randint(0, 2)], COLORS[randint(0, 2)]
error_args_2 = NUMBERS[randint(0, 2)], 'ROUND', SHADINGS[randint(0, 2)], COLORS[randint(0, 2)]
error_args_3 = NUMBERS[randint(0, 2)], SYMBOLS[randint(0, 2)], SHADINGS[randint(0, 2)], 'BLUE'

set_1 = [(1, 2, 0, 1),
         (1, 2, 0, 1),
         (1, 2, 0, 1),
        ]
set_2 = [(1, 2, 0, 1),
         (0, 2, 1, 1),
         (2, 2, 2, 1),
        ]

set_3 = [(0, 2, 0, 1),
         (1, 2, 0, 0),
         (2, 2, 0, 2),
        ]
no_set_1 = [(1, 1, 2, 0),
            (2, 1, 2, 0),
            (1, 0, 0, 1),
           ]
no_set_2 = [(0, 2, 0, 1),
            (1, 1, 2, 2),
            (1, 2, 0, 1),
           ]
no_set_3 = [(1, 0, 0, 1),
            (0, 2, 0, 2),
            (1, 2, 1, 1),
           ]

class Card:
    def __init__(self, number, symbol, shading, color):
        if any([
            number not in NUMBERS,
            symbol not in SYMBOLS,
            shading not in SHADINGS,
            color not in COLORS
        ]):
            raise ValueError("Неправильные параметры карты")

        self.number = number
        self.symbol = symbol
        self.shading = shading
        self.color = color

    def __str__(self):
        return f'{self.number}, {self.symbol}, {self.shading}, {self.color}'

def get_three_cards_from_index(args):
    cards = [get_card_with_index_args(args[0]), get_card_with_index_args(args[1]), get_card_with_index_args(args[2])]
    return cards

def get_three_cards_random(args1, args2, args3):
    cards =  [get_random_card(*args1), get_random_card(*args2), get_random_card(*args3)]
    return cards

def get_card_with_index_args(args):
    return Card(NUMBERS[args[0]], SYMBOLS[args[1]], SHADINGS[args[2]], COLORS[args[3]])

def get_random_card(num, sym, shad, col):
    return Card(num, sym, shad, col)

def check_set(cards):
    if not cards:
        return False
    x, y, z = [[i.number, i.symbol, i.color, i.shading] for i in cards]
    return all([len(set((x[i], y[i], z[i])))!=2 for i in range(4)])
