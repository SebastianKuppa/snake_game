from snake import Snake
import pygame
import time

# game params
bounds = (300, 300)
block_size = 20
run = True
game_speed = 100  # in ms

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption('SNAKE')
    snake = Snake(block_size=block_size, bounds=bounds)
    clock = pygame.time.Clock()
    # gaming loop
    while run:
        pygame.time.delay(game_speed)
        # time.sleep(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        snake.move()
        window.fill(color=(0, 0, 0))
        snake.draw(pygame, window)
        pygame.display.update()
        clock.tick(40)
