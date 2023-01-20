from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    length = None
    direction = None
    body = None
    color = (0, 0, 255)

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()
