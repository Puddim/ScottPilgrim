import pygame
import os
pygame.init()
pygame.display.set_caption("TEST")
w = 700
h = 600
screensize = (w,h)
screen = pygame.display.set_mode(screensize)
black = (0, 0, 0)
xa = 0
ya = 0
while True:
    player = pygame.image.load(os.path.join("Images", "run", "run0.gif"))
    playern = pygame.transform.flip(player, xa, ya)
    screen.fill(black)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        xa += 1
    if pressed[pygame.K_d]:
        xa -= 1
    if xa > 1:
        xa = 1
    if xa < 0:
        xa = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
            pygame.display.quit()
    screen.blit(playern, (0,0))
    pygame.display.update()