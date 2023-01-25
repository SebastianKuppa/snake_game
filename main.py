from snake import Snake, Direction
from food import Food

import pygame


# game params
bounds = (500, 500)  # window size
block_size = 20  # size of each snake subpart
run = True
game_speed = 100  # loop delay in ms

if __name__ == '__main__':
    # start mygame instance
    pygame.init()
    # init game window
    window = pygame.display.set_mode(bounds)
    # set window name
    pygame.display.set_caption('SNAKE')
    # init Snake object
    snake = Snake(block_size=block_size, bounds=bounds)
    # init food object
    food = Food(block_size, bounds)
    # adding font object for game over message
    font = pygame.font.SysFont('comicsans', 60, True)
    # add clock object for window update
    clock = pygame.time.Clock()
    # start gaming loop
    while run:
        # how fast to update the game screen
        pygame.time.delay(game_speed)

        # closing the window in the top right corner will stop the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # check which keyboard keys were pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.steer(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            snake.steer(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            snake.steer(Direction.UP)
        elif keys[pygame.K_DOWN]:
            snake.steer(Direction.DOWN)
        # new snake position/length is calculated
        snake.move()
        # check for food collision
        snake.check_for_food(food)
        # check for head and body collision
        if snake.check_tail_collision() or snake.check_bounds():
            text = font.render('Game Over', True, (255, 255, 255))
            window.blit(text, (80, 200))
            pygame.display.update()
            pygame.time.delay(1000)
            snake.respawn()
            food.respawn()
        # clear game window to black
        window.fill(color=(0, 0, 0))
        # draw the new snake, after move() method was called
        snake.draw(pygame, window)
        # draw food block
        food.draw(pygame, window)
        # update window
        pygame.display.update()
        clock.tick(40)
