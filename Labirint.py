#Connecting modules--------------------------------------------------
import pygame
from random import randint
#Creating Variables--------------------------------------------------
run = True
pause = False
ws = 700
hs = 500
walls = []
lrud = 99
playerlist = []
pygame.font.init()
score = 0
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 120)
text2 = f2.render('You die', True, (180, 0, 0))
#Create a window--------------------------------------------------
pygame.init()
scr = pygame.display.set_mode((ws, hs))
bg = pygame.transform.scale(pygame.image.load('bg.png'), (ws,hs))
pygame.display.set_caption('Maded by abik')
pygame.init()
#Classes and Functions--------------------------------------------------
class wall():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.r = (self.x, self.y, self.w, self.h)
    def show(self):
        self.wall = pygame.draw.rect(scr, (255,0,0), self.r)
class player():
    def __init__(self, x, y, bp):
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
            self.y -= 5
            if self.bp == 'player':
                self.p = pygame.transform.scale(pygame.image.load('player2up.png'), (self.w, self.w))
            if self.bp == 'bot':
                self.p = pygame.transform.scale(pygame.image.load('player1up.png'), (self.w, self.w))
            self.r = (self.x, self.y, self.w, self.w)
    def down(self):
        if self.y < hs - self.w:
            self.y += 5
            if self.bp == 'player':
                self.p = pygame.transform.scale(pygame.image.load('player2down.png'), (self.w, self.w))
            if self.bp == 'bot':
                self.p = pygame.transform.scale(pygame.image.load('player1down.png'), (self.w, self.w))
            self.r = (self.x, self.y, self.w, self.w)
    def right(self):
        if self.x < ws - self.w:
            self.x += 5
            if self.bp == 'player':
                self.p = pygame.transform.scale(pygame.image.load('player2right.png'), (self.w, self.w))
            if self.bp == 'bot':
                self.p = pygame.transform.scale(pygame.image.load('player1right.png'), (self.w, self.w))
            self.r = (self.x, self.y, self.w, self.w)
    def left(self):
        if self.x > 0:
            self.x -= 5
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
def CreateGame():
    #Map generation--------------------------------------------------
    levels = [[
        '@+=++++++==+++',
        '=+=+=+==+=++=+',
        '=++++=+=+=+==+',
        '==+=+=!=+=++=+',
        '+++=+++=+==+=+',
        '+=+=+==++=++=+',
        '+=++==+=+++==+',
        '++===++===+==+',
        '+==+++=+++=++!',
        '!+++=+++=+++=$']
        ,[
        '@+=+=+=+=+=+==',
        '++++++++++++!=',
        '=+=!=+=+=+=+==',
        '+++++++++++++=',
        '=+=+=+=+=+=+==',
        '+++++++++++++=',
        '=+=+=+=+=!=+==',
        '+++++++++++++=',
        '=!=+=+=+=+=+++',
        '============!$']
        ,[
        '@=+++==++=+++=',
        '+=+=++++=++=+!',
        '+=+=+=+++++++=',
        '+=+=++=!+===++',
        '+=+=++=++=++++',
        '+++=++==+=+=++',
        '+=+=+++==+++==',
        '+=++=++=++=+++',
        '+==+=++=+==+=+',
        '++++!++=+++!=$']
        ]
        
    q = levels[randint(0, len(levels)-1)]
    #q = levels[2]
    for j in range(10):
        for i in range(14):
            if q[j][i] == '=':
                walls.append(wall(50 * i, 50 * j))
            if q[j][i] == '@':
                playerlist.append(player(50 * i, 50 * j, 'player'))
            if q[j][i] == '$':
                playerlist.append(player(50 * i, 50 * j, 'coin'))
            if q[j][i] == '!':
                playerlist.append(player(50 * i, 50 * j, 'bot'))
#Game loop--------------------------------------------------
CreateGame()
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if pause == False:
        #Player Movement--------------------------------------------------
        for i in playerlist:
            if i.bp == 'player':
                if keys[pygame.K_a]:
                    c = coliding(i.hitbox, i.x, i.y, 'left')
                    if c == False:
                        i.left()
                if keys[pygame.K_d]:
                    c = coliding(i.hitbox, i.x, i.y, 'right')
                    if c == False:
                        i.right()
                if keys[pygame.K_w]:
                    c = coliding(i.hitbox, i.x, i.y, 'up')
                    if c == False:
                        i.up()
                if keys[pygame.K_s]:
                    c = coliding(i.hitbox, i.x, i.y, 'down')
                    if c == False:
                        i.down()
        #Bot movement--------------------------------------------------
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
        #Check for wining--------------------------------------------------
        for i in playerlist:
            for j in playerlist:
                if i.bp == 'player' and j.bp == 'bot' and i.hitbox.colliderect(j.hitbox):
                    print("Don't luck. You die.")
                    score = 0
                    pause = True
                elif i.bp == 'player' and j.bp == 'coin' and i.hitbox.colliderect(j.hitbox):
                    print("Congratulations! You passed this level.")
                    score += 1
                    pause = True
        #Hitboxes and map rendering--------------------------------------------------
        for i in playerlist:
            i.hitboxs()
            i.hitboxs()
        scr.blit(bg, (0,0))
        for i in walls:
            i.show()
        for i in playerlist:
            scr.blit(i.p, i.r)
    #Restart game--------------------------------------------------
    if pause == True:
        scr.blit(bg, (0,0))
        if score == 0:
            text1 = f1.render('Press space to restart', True, (180, 0, 0))
            scr.blit(text2, (ws/2-150, 150))
            scr.blit(text1, (ws/2-125, 450))
        if score > 0:
            text1 = f1.render('Press space to play', True, (180, 0, 0))
            text3 = f2.render('Score ' + str(score), True, (180, 0, 0))
            scr.blit(text3, (ws/2-150, 150))
            scr.blit(text1, (ws/2-125, 450))
        if keys[pygame.K_SPACE]:
            lrud = 99
            walls.clear()
            playerlist.clear()
            CreateGame()
            
            for i in playerlist:
                i.hitboxs()
                i.hitboxs()
            scr.blit(bg, (0,0))
            for i in walls:
                i.show()
            for i in playerlist:
                scr.blit(i.p, i.r)

            print("New Roud!")
            pause = False
    #Screen update--------------------------------------------------
    pygame.display.update()