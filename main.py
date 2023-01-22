from snake import Snake
import pygame


if __name__ == '__main__':
    bounds = (300, 300)
    pygame.init()
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption('SNAKE')
    player = Snake(block_size=20, bounds=bounds)

