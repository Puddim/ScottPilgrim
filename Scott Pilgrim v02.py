# -----------------------
#        Game Test
#   Using Scott Pilgrim
#       By Puddim
# https://github.com/Puddim
# -----------------------
#                                                       IMPORT
import pygame
import os
import time
import random
import math
#                                                       INIT
pygame.init()
pygame.display.set_caption("Scott Pilgrim")
w = 1200
h = 284
screensize = (w,h)
screen = pygame.display.set_mode(screensize)
running = True
black = (0, 0, 0)
clock = pygame.time.Clock()
#                                                      LOAD
icon = pygame.image.load(os.path.join("Images", "icon.jpg"))
backgroundsound = pygame.mixer.music.load(os.path.join("Sounds", "SBO.mp3"))
background = pygame.image.load(os.path.join("Images", "background.png"))
standl = []
for i in range(0,7):
    imglid = "stand" + str(i) + ".gif"
    standl.append(pygame.image.load(os.path.join("Images", "stand", imglid)))
runl = []
for i in range(0,7):
    imglid = "run" + str(i) + ".gif"
    runl.append(pygame.image.load(os.path.join("Images", "run", imglid)))

pygame.mixer.music.play(9999)
pygame.display.set_icon(icon)
#                                                     DEF
def updatescott():
    moving = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        scott.right()
        moving = True
    if pressed[pygame.K_a]:
        scott.left()
        moving = True
    if pressed[pygame.K_s]:
        scott.down()
        moving = True
    if pressed[pygame.K_w]:
        scott.up()
        moving = True
    if moving == False:
        scott.stand()
    elif moving == True:
        scott.run()
    scott.border()

#                                                   CLASSES
class player(object):
    def __init__(self):
        self.x = 400
        self.y = 160
        self.spr = "s"
        self.dir = 0

    def getpos(self):
        return (int(self.x), int(self.y))

    def getdir(self):
        return self.dir

    def right(self):
        self.x += 2
        self.dir = 0

    def left(self):
        self.x -= 2
        self.dir = 1

    def up(self):
        self.y -= 2
        self.dir = self.dir

    def down(self):
        self.y += 2
        self.dir = self.dir

    def stand(self):
        self.spr = "s"

    def run(self):
        self.spr = "r"

    def getstatus(self):
        return self.spr

    def border(self):
        if self.y < 116:
            self.y = 116
        if self.y > 212:
            self.y = 212
        if self.x > 1154:
            self.x = 1154
        if self.x < -14:
            self.x = -14
#                                                    BASIC
scott = player()
dit = 0
exst = "s"
lastcd = 0
print (len(standl))
#                                                    LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
    screen.blit(background, (-15, -30))
    updatescott()
    if scott.getstatus() == "r":
        if exst == "r":
            screen.blit(pygame.transform.flip(runl[int(dit)], scott.getdir(), 0), (scott.getpos()))
        else:
            exst = "r"
            dit = 0
            screen.blit(pygame.transform.flip(runl[int(dit)], scott.getdir(), 0), (scott.getpos()))
    else:
        if exst == "s":
            screen.blit(pygame.transform.flip(standl[int(dit)], scott.getdir(), 0), (scott.getpos()))
        else:
            exst = "s"
            dit = 0
            screen.blit(pygame.transform.flip(standl[int(dit)], scott.getdir(), 0), (scott.getpos()))
    # print (pygame.key.get_pressed())
    pygame.display.update()
    # time.sleep(0)

    if pygame.time.get_ticks() > lastcd + 200:
        lastcd = pygame.time.get_ticks()
        dit += 1
    if dit == 7 or dit > 6.9:
        dit = 0
    clock.tick(120)
    print (clock)
    print (scott.getpos())
    print (pygame.time.get_ticks())
    print (lastcd)