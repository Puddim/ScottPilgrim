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
screensize = (w, h)
screen = pygame.display.set_mode(screensize)
running = True
black = (0, 0, 0)
clock = pygame.time.Clock()
ei = 0
eit = 0
#                                                      LOAD
icon = pygame.image.load(os.path.join("Images", "icon.jpg"))
backgroundsound = pygame.mixer.music.load(os.path.join("Sounds", "SBO.mp3"))
background = pygame.image.load(os.path.join("Images", "background.png"))
standl = []
for i in range(0, 8):
    imglid = "stand" + str(i) + ".gif"
    standl.append(pygame.image.load(os.path.join("Images", "stand", imglid)))
runl = []
for i in range(0, 8):
    imglid = "run" + str(i) + ".gif"
    runl.append(pygame.image.load(os.path.join("Images", "run", imglid)))
attackl = []
for i in range(0,7):
    imglid = "attack" + str(i) + ".gif"
    attackl.append(pygame.image.load(os.path.join("Images", "attack", imglid)))
evill = []
for i in range(0,5):
    imglid = "evil" + str(i) + ".gif"
    evill.append(pygame.image.load(os.path.join("Images", "evil", imglid)))
pygame.mixer.music.play(9999)
pygame.display.set_icon(icon)


#                                                     DEF
def updatescott():
    global dit
    moving = False
    pressed = pygame.key.get_pressed()
    if scott.attck() == 0:
        if pressed[pygame.K_SPACE]:
            scott.attack()
            return None
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
        if scott.attck() == 0:
            if moving == False:
                scott.stand()
            elif moving == True:
                scott.run()
    else:
        if dit == 6:
            scott.stand()
    scott.border()
    renderscott()

def renderscott():
    global exst
    global dit
    if scott.getstatus() == "r":
        if exst == "r":
            screen.blit(pygame.transform.flip(runl[int(dit)], scott.getdir(), 0), (scott.getpos()))
        else:
            exst = "r"
            dit = 0
            screen.blit(pygame.transform.flip(runl[int(dit)], scott.getdir(), 0), (scott.getpos()))
    elif scott.getstatus() == "s":
        if exst == "s":
            screen.blit(pygame.transform.flip(standl[int(dit)], scott.getdir(), 0), (scott.getpos()))
        else:
            exst = "s"
            dit = 0
            screen.blit(pygame.transform.flip(standl[int(dit)], scott.getdir(), 0), (scott.getpos()))
    elif scott.getstatus() == "a":
        if exst == "a":
            screen.blit(pygame.transform.flip(attackl[int(dit)], scott.getdir(), 0), (scott.getpos()))
        else:
            exst = "a"
            dit = 0
            screen.blit(pygame.transform.flip(attackl[int(dit)], scott.getdir(), 0), (scott.getpos()))
def updateevil():
    global ei
    global eit
    if eit == 0:
        if ei == 4 or ei > 4:
            if eit == 0:
                eit = 1
                ei = 2
            else:
                eit = 0
        else:
            if eit == 0:
                ei += 0.1
            else:
                ei -= 0.1
    elif eit == 1:
        if ei == 0 or ei < 0:
            if eit == 0:
                eit = 1
                ei = 2
            else:
                eit = 0
        else:
            if eit == 0:
                ei += 0.1
            else:
                ei -= 0.1
    nega.detecthit()
    nega.detecthp()
    if nega.status == 0:
        if random.randint(0,500) == 2:
            nega.revive()

def rendernega():
    screen.blit(pygame.transform.flip(evill[int(ei)], 1, 0), (nega.x, nega.y))
#                                                       CLASSES
class player(object):
    def __init__(self):
        self.x = 400
        self.y = 160
        self.spr = "s"
        self.dir = 0

    def getpos(self):
        if scott.getdir() == 1 and self.spr == "a":
            return (int(self.x - 20), int(self.y))
        else:
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

    def attck(self):
        if self.spr == "a":
            return 1
        else:
            return 0

    def attack(self):
        scott.spr = "a"

class evil(object):
    def __init__(self):
        self.hp = 100
        self.x = 800
        self.y = 160
        self.status = 1
        self.at = 0

    def detecthit(self):
        if self.status == 1:
            sctp = scott.getpos()
            dist = math.sqrt((self.x - sctp[0])**2 + (self.y - sctp[1])**2)
            # print (dist)
            if scott.getstatus() == "a" and dist < 30 and self.at == 0:
                self.hp -= 10
                self.at = 1
            else:
                if not scott.getstatus() == "a":
                    self.at = 0
    def detecthp(self):
        if self.hp < 0:
            self.status = 0
        else:
            rendernega()
    def revive(self):
        self.status = 1
        self.hp = 100

# BASIC
nega = evil()
scott = player()
dit = 0
exst = "s"
lastcd = 0
print(len(standl))
#                                                    LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
    screen.blit(background, (-15, -30))
    if scott.y - 4 > nega.y:
        updateevil()
        updatescott()
    else:
        updatescott()
        updateevil()
    # print (pygame.key.get_pressed())
    pygame.display.update()
    # time.sleep(0)
    if scott.getstatus() == "s" or scott.getstatus() == "r":
        if pygame.time.get_ticks() > lastcd + 100:
            lastcd = pygame.time.get_ticks()
            dit += 1
        if dit == 8 or dit > 7.9:
            dit = 0
    elif scott.getstatus() == "a":
        if pygame.time.get_ticks() > lastcd + 100:
            lastcd = pygame.time.get_ticks()
            dit += 1
        if dit == 7 or dit > 6.9:
            dit = 0
    clock.tick(120)
    if pygame.time.get_ticks() > lastcd + 90:
        print(clock)
        print(scott.getpos())
        print(pygame.time.get_ticks())
        print(lastcd)
        print(scott.spr)
        print("evil hp: " + str(nega.hp))
