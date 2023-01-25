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
        elif self.direction == Direction.LEFT:
            next_head = (curr_block[0] - self.block_size, curr_block[1])
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, direction: Direction):
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction

    def eat(self):
        self.length += 1

    def check_for_food(self, food):
        head_block = self.body[-1]
        if head_block[0] == food.x and head_block[1] == food.y:
            self.eat()
            food.respawn()

    def check_tail_collision(self):
        head_block = self.body[-1]
        collision = False
        for i in range(len(self.body) - 1):
            curr_snake_block = self.body[i]
            if head_block[0] == curr_snake_block[0] and head_block[1] == curr_snake_block[1]:
                collision = True

        return collision
