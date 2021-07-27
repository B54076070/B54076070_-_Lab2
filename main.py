import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"),(50,50))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"),(HP_WIDTH ,HP_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"),(HP_WIDTH ,HP_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"),(BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"),(BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"),(BTN_WIDTH, BTN_HEIGHT))
continue_image =  pygame.transform.scale(pygame.image.load("images/continue.png"),(BTN_WIDTH, BTN_HEIGHT))

# set the title
pygame.display.set_caption("My first game")


class Game:
    def __init__(self):
        # window
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # draw background
            self.window.blit((background_image),(0,0))

            # draw enemy and health bar
            self.window.blit((enemy_image), (50, 270))
            pygame.draw.rect(self.window,(255,0,0),[50,260,50,5])
            pygame.display.flip()

            # draw menu (and buttons)
            pygame.draw.rect(self.window, (0,0,0), [0,0,WIN_WIDTH,80])

            self.window.blit((muse_image), (600, 0))
            self.window.blit((sound_image), (700, 0))
            self.window.blit((continue_image), (800, 0))
            self.window.blit((pause_image), (900, 0))
            self.window.blit((hp_image), (300, 0))
            self.window.blit((hp_image), (350, 0))
            self.window.blit((hp_image), (400, 0))
            self.window.blit((hp_image), (450, 0))
            self.window.blit((hp_image), (500, 0))
            self.window.blit((hp_image), (300, 60))
            self.window.blit((hp_image), (350, 60))
            self.window.blit((hp_gray_image), (400, 60))
            self.window.blit((hp_gray_image), (450, 60))
            self.window.blit((hp_gray_image), (500, 60))
            # draw time
            clock = pygame.time.Clock()

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



