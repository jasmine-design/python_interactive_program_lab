import pygame
import time
pygame.init()

# images size

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
MENU_HEIGHT = 80
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))

# set the title
pygame.display.set_caption("My first game")

# set the font
my_font = pygame.font.SysFont("my_font.ttf", 24)


class Game:

    def __init__(self):
        global window
        # window
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # hp
        self.hp = 7
        self.max_hp = 10

    def game_run(self):
        sum_time = 0.0
        # game loop
        run = True
        while run:
            # when game start, start to count time
            time_start = time.time()
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # draw background
            window.blit(background_image, (0, 0))

            # draw enemy and health bar
            window.blit(enemy_image, (100, 400))  # enemy
            pygame.draw.rect(window, RED, [100, 380, 80, 8])  # health bar

            # draw menu
            pygame.draw.rect(window, BLACK, [0, 0, WIN_WIDTH, MENU_HEIGHT])
            # draw hp
            window.blit(hp_image, (WIN_WIDTH / 2 - 80, 6))
            window.blit(hp_image, (WIN_WIDTH / 2 - 40, 6))
            window.blit(hp_image, (WIN_WIDTH / 2, 6))
            window.blit(hp_image, (WIN_WIDTH / 2 + 40, 6))
            window.blit(hp_image, (WIN_WIDTH / 2 + 80, 6))
            window.blit(hp_image, (WIN_WIDTH / 2 - 80, 40))
            window.blit(hp_image, (WIN_WIDTH / 2 - 40, 40))
            window.blit(hp_gray_image, (WIN_WIDTH / 2, 40))
            window.blit(hp_gray_image, (WIN_WIDTH / 2 + 40, 40))
            window.blit(hp_gray_image, (WIN_WIDTH / 2 + 80, 40))
            # draw button
            window.blit(muse_image, (WIN_WIDTH - 310, 0))
            window.blit(sound_image, (WIN_WIDTH - 240, 0))
            window.blit(continue_image, (WIN_WIDTH - 170, 0))
            window.blit(pause_image, (WIN_WIDTH - 100, 0))
            # draw time
            time_end = time.time()
            sum_time = (time_end - time_start) + sum_time
            display_time = time.strftime("%M:%S", time.gmtime(sum_time))
            pygame.draw.rect(window, BLACK, [0, WIN_HEIGHT - 40, 80, 40])
            window.blit(my_font.render(display_time, True, WHITE), (20, WIN_HEIGHT - 30))

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



