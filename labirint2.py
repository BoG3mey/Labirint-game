#Подключение модулей--------------------------------------------------
from cmath import rect
import pygame
from random import randint
#Стат переменные--------------------------------------------------
run = True
ws = 700
hs = 500
walls = []
lrud = 99
playerlist = []
ghd = 0
#Создание окна--------------------------------------------------
pygame.init()
scr = pygame.display.set_mode((ws, hs))
bg = pygame.transform.scale(pygame.image.load('bg.png'), (ws,hs))
pygame.display.set_caption('Maded by abik')
pygame.init()

pygame.mixer.music.load('fone.mp3')
pygame.mixer.music.play()
#Класы--------------------------------------------------
class wall():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 25
        self.h = 25
        self.r = (self.x, self.y, self.w, self.h)
    def show(self):
        self.wall = pygame.draw.rect(scr, (255,0,0), self.r)
class player():
    def __init__(self, x, y, bp):
        self.speed = 1
        self.bp = bp
        self.lr = 3
        self.ud = 3
        self.x = x
        self.y = y
        self.w = 50
        self.r = (self.x, self.y, self.w, self.w)
        self.hitbox = pygame.draw.rect(scr, (255,0,0), self.r)
        if self.bp == 'player':
            self.p = pygame.transform.scale(pygame.image.load('player2up.png'), (self.w, self.w))
        if self.bp == 'coin':
            self.p = pygame.transform.scale(pygame.image.load('coin.png'), (50, 50))
        if self.bp == 'bot':
            self.p = pygame.transform.scale(pygame.image.load('player1up.png'), (self.w, self.w))
    def up(self):
        if self.y > 0:
            self.y -= self.speed
            if self.bp == 'player':
                self.p = pygame.transform.scale(pygame.image.load('player2up.png'), (self.w, self.w))
            if self.bp == 'bot':
                self.p = pygame.transform.scale(pygame.image.load('player1up.png'), (self.w, self.w))
            self.r = (self.x, self.y, self.w, self.w)
    def down(self):
        if self.y < hs - self.w:
            self.y += self.speed
            if self.bp == 'player':
                self.p = pygame.transform.scale(pygame.image.load('player2down.png'), (self.w, self.w))
            if self.bp == 'bot':
                self.p = pygame.transform.scale(pygame.image.load('player1down.png'), (self.w, self.w))
            self.r = (self.x, self.y, self.w, self.w)
    def right(self):
        if self.x < ws - self.w:
            self.x += self.speed
            if self.bp == 'player':
                self.p = pygame.transform.scale(pygame.image.load('player2right.png'), (self.w, self.w))
            if self.bp == 'bot':
                self.p = pygame.transform.scale(pygame.image.load('player1right.png'), (self.w, self.w))
            self.r = (self.x, self.y, self.w, self.w)
    def left(self):
        if self.x > 0:
            self.x -= self.speed
            if self.bp == 'player':
                self.p = pygame.transform.scale(pygame.image.load('player2left.png'), (self.w, self.w))
            if self.bp == 'bot':
                self.p = pygame.transform.scale(pygame.image.load('player1left.png'), (self.w, self.w))
            self.r = (self.x, self.y, self.w, self.w)
    def show(self):
        scr.blit(self.p, self.r)
    def hitboxs(self):
        self.hitbox = pygame.draw.rect(scr, (255,0,0), self.r)
def coliding(hitbox1, x1, y1, f):
    c = []
    for i in walls:
        if hitbox1.colliderect(i.wall):
            print('you die!')
            c.append(True) 
        else:
            if f == 'left':
                newx = x1 - 5
                newy = y1
                newhitbox = pygame.draw.rect(scr, (255,0,0) ,(newx, newy, 50, 50))
                if newhitbox.colliderect(i.wall):
                    c.append(True) 
                else:
                    c.append(False)
            if f == 'right':
                newx = x1 + 5
                newy = y1
                newhitbox = pygame.draw.rect(scr, (255,0,0) ,(newx, newy, 50, 50))
                if newhitbox.colliderect(i.wall):
                    c.append(True) 
                else:
                    c.append(False)
            if f == 'up':
                newx = x1
                newy = y1 - 5
                newhitbox = pygame.draw.rect(scr, (255,0,0) ,(newx, newy, 50, 50))
                if newhitbox.colliderect(i.wall):
                    c.append(True) 
                else:
                    c.append(False)
            if f == 'down':
                newx = x1
                newy = y1 + 5
                newhitbox = pygame.draw.rect(scr, (255,0,0) ,(newx, newy, 50, 50))
                if newhitbox.colliderect(i.wall):
                    c.append(True) 
                else:
                    c.append(False) 
    if True in c:
        return True
    else:
        return False
#Создание карты и игроков--------------------------------------------------
q = ['++=++++++==+++',
     '=+=+=+==+=++=+',
     '=++++=+=+=+==+',
     '==+=+=+=+=++=+',
     '+++=+++=+==+=+',
     '+=+=+==++=++=+',
     '+=++==+=+++==+',
     '++===++===+==+',
     '+==+++=+++=+++',
     '++++=+++=+++=+']
for j in range(10):
    for i in range(14):
        if q[j][i] == '=':
            walls.append(wall(50 * i, 50 * j))
playerlist.append(player(0, 0, 'player'))
playerlist.append(player(650, 450, 'coin'))
playerlist.append(player(300, 150, 'bot'))
playerlist.append(player(0, 450, 'bot'))
playerlist.append(player(650, 450, 'bot'))
#Цикл игры--------------------------------------------------
while run:
    #pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #Движение игрока--------------------------------------------------
    for i in playerlist:
        if i.bp == 'player':
            if keys[pygame.K_a]:
                i.left()
            if keys[pygame.K_d]:
                i.right()
            if keys[pygame.K_w]:
                i.up()
            if keys[pygame.K_s]:
                i.down()
    #Движение бота--------------------------------------------------
    for i in playerlist:
        if lrud > 100:
            i.lr = randint(1, 3)
            i.ud = randint(1, 3)
        if i.bp == 'bot':
            if i.lr == 1:
                c = coliding(i.hitbox, i.x, i.y, 'left')
                if c == False:
                    i.left()
            if i.lr == 2:
                c = coliding(i.hitbox, i.x, i.y, 'right')
                if c == False:
                    i.right()
            if i.ud == 1:
                c = coliding(i.hitbox, i.x, i.y, 'up')
                if c == False:
                    i.up()
            if i.ud == 2:
                c = coliding(i.hitbox, i.x, i.y, 'down')
                if c == False:
                    i.down()
    if lrud > 100:
        lrud = 0
    lrud += 1
    for i in playerlist:
        for j in playerlist:
            if i.bp == 'player' and j.bp == 'bot' and i.hitbox.colliderect(j.hitbox):
                run = False
            if i.bp == 'player' and j.bp == 'coin' and i.hitbox.colliderect(j.hitbox):
                print('You are Winner!!!')
        if ghd > 0:
            for g in walls:
                if i.bp == 'player' and i.hitbox.colliderect(g.wall):
                    run = False
        ghd = 1
    #Хитбоксы и отрисовка на карте--------------------------------------------------
    for i in playerlist:
        i.hitboxs()
        i.hitboxs()
    scr.blit(bg, (0,0))
    for i in walls:
        i.show()
    for i in playerlist:
        scr.blit(i.p, i.r)
    #--------------------------------------------------
    #Обновление екрана--------------------------------------------------
    pygame.display.update()