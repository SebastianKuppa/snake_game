import random


class Food:
    color = (0, 255, 0)
    x = 0
    y = 0

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
