from snake import Snake
import pygame

# game params
bounds = (300, 300)  # window size
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
        # new snake position/length is calculated
        snake.move()
        # clear game window to black
        window.fill(color=(0, 0, 0))
        # draw the new snake, after move() method was called
        snake.draw(pygame, window)
        # update window
        pygame.display.update()
        clock.tick(40)
