#Imports 
import pygame

#Initialize
pygame.init()

#Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400
SCORE = 0

#Display Screen
DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption("CAM'S SUPER COOL GAME 1111!!!!")

#
clock = pygame.time.Clock()
letter_c = pygame.image.load('C.png')
mistake = False

def display_letter(letter_image, x, y):
    DISPLAY_SURF.blit(letter_image, (x, y))

x =  (SCREEN_WIDTH * 0.5)
y = (SCREEN_HEIGHT * 0.5)

while not mistake:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mistake = True

    display_letter(letter_c, x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

