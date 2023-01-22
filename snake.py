from enum import Enum
import pygame


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

    def respawn(self):
        self.length = 3
        self.body = [(20, 20), (20, 40), (20, 60)]
        self.direction = Direction.DOWN

    def draw(self, game: pygame, window):
        for block in self.body:
            game.draw.rect(window, self.color, (block[0], block[1], self.block_size, self.block_size))
