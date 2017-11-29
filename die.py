from random import randint


class Die():
    '''掷骰子'''

    def __init__(self, num_sides=6):
        # 面数，默认6面
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
