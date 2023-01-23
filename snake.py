from enum import Enum
import pygame


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    length = None
    direction = Direction.DOWN
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

    def draw(self, game, window):
        for block in self.body:
            game.draw.rect(window, self.color, (block[0], block[1], self.block_size, self.block_size))

    def move(self):
        curr_block = self.body[-1]
        if self.direction == Direction.DOWN:
            next_head = (curr_block[0], curr_block[1] + self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.UP:
            next_head = (curr_block[0], curr_block[1] - self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.RIGHT:
            next_head = (curr_block[0] + self.block_size, curr_block[1])
            self.body.append(next_head)
        elif self.direction == Direction.RIGHT:
            next_head = (curr_block[0] - self.block_size, curr_block[1])
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)
