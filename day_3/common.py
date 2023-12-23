from itertools import product


DOT = '.'

CARDINAL_POINTS = set(product([-1,0,1], repeat=2)) - {(0,0)}

def surrounding_points(x, y):
    for poss_x, poss_y in CARDINAL_POINTS:
        yield poss_x + x, poss_y + y

def is_symbol(c: str):
    return c != DOT and not c.isdigit() and not c.isspace()