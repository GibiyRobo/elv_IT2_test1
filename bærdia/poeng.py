
import time
from pygame.locals import *
import pygame as pg

pg.init()
pg.display.set_caption("Top-G pong")
font=pg.font.SysFont("Ariel", 35)

class Ball:
    def __init__(self, radius, x_pos, y_pos, fart,mainScreen):
        self.r=radius
        self.x=x_pos
        self.y=y_pos
        self.f=fart
        self.fy=fart
        self.s= mainScreen
        #super().__init__()

    def tegn(self):
        pg.draw.circle(self.s, hvit,(self.x,self.y), self.r)

    def move(self):
        if ((self.x+self.r) >= self.s.get_width()) or ((self.x-self.r) <= 0): 
            self.f=-self.f
        if ((self.y-self.r) <= 0)  or ((self.y+self.r) >= self.s.get_height()):
            self.fy=-self.fy

        self.y+=self.fy
        self.x+=self.f


# class Player:
#     def __init__(self, y_pos, x_pos, heigth ,width , fart,mainScreen):
#         self.h=heigth
#         self.w=width 
#         self.x=x_pos
#         self.y=y_pos
#         self.f=fart
#         self.fy=fart
#         self.s= mainScreen
#         #super().__init__()

#     def tegn(self):
#         pg.draw.rect(self.s, hvit,(self.x,self.y, self.h, self.w))

#     def move(self, key):
        
#         if self.x >= self.s.get_width()-(self.w*9): 
#             self.x-=20
#         if self.x-self.w <= 0:
#             self.x+=20
        
#         if key[K_RIGHT]:
#             self.x+=self.f
#         if key[K_LEFT]:
#             self.x-=self.f
        

blck = (0,0,0)
hvit = (255,255,255)

size = [700, 500]
S = pg.display.set_mode(size)


B=Ball(15,150,100,0.4,S)
P=pg.Rect(200,(S.get_height()-120),162,20)
fart=1


clock = pg.time.Clock()
clock.tick(60)
point=0
carryOn1 = True
carryOn2=True
carryOn3=True
carryOn4 =True

while carryOn1:
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            carryOn1=False
        if event.type == pg.QUIT:
            carryOn1=False
            carryOn2=False
            carryOn3=False
            carryOn4=False
    S.fill(blck) 
    velkommen=font.render("velkommen til min pong-spill!", True, (50,255,50))
    S.blit(velkommen, (180,200))
    pg.display.flip()

while carryOn2:
    key=pg.key.get_pressed() 
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT: # If user clicked close
            carryOn2 = False # Flag that we are done so we exit this loop
            carryOn3=False
            carryOn4=False
        if event.type== pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                carryOn2=False
            if event.key == pg.K_RIGHT:
                carryOn2=False

    S.fill(blck)
    ScoreBoard=font.render(str(point), True, (50,255,50))
    S.blit(ScoreBoard, (S.get_width()-60,60))
    starter=font.render("start med å trykk på høyre/venstre pillene på pc-en", True, (50,255,50))
    S.blit(starter, (50,250))

    B.tegn()
    pg.draw.rect(S,hvit,P)

    pg.display.flip()

while carryOn3:  
    # --- Main event loop
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT: # If user clicked close
            carryOn3 = False # Flag that we are done so we exit this loop
            carryOn4=False

    S.fill(blck)
    ScoreBoard=font.render(str(point), True, (50,255,50))
    S.blit(ScoreBoard, (S.get_width()-60,60))

    B.tegn()
    B.move()
    pg.draw.rect(S,hvit,P)
    
    key=pg.key.get_pressed()

    if key[pg.K_LEFT]:
        P.move_ip(-fart, 0)
    if key[pg.K_RIGHT]:
        P.move_ip(fart, 0)

    
    
    if P.collidepoint(B.x, B.y+ B.r):
        B.f = -B.f
        B.fy= -B.fy
        point+=1
        fix=0
        # ****************************  
        # fix-en på flere treff i et mål, hvor de gjenstandene bevegr fra hverandre basert på konstanten k
        k=7
        while P.collidepoint(B.x,B.y+ B.r+k):
            fix+=1
            P.move_ip(0,15)
        P.move_ip(0,fix*-15)
        #******************************

    if (B.y+B.r) >= S.get_height():    
        game_over=font.render("du tapte", True, (50,255,50))
        S.blit(game_over, (350,160))
        pg.display.flip()
        pg.time.wait(1000)
        carryOn3=False 

    pg.display.flip()



size = [400, 200]
S = pg.display.set_mode(size)

while carryOn4:
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            carryOn4=False
        if event.type == pg.QUIT:
            carryOn4=False
    S.fill(blck) 
    score=font.render(f"du fikk {point} mål!", True, (50,255,50))
    S.blit(score, (110,80))
    pg.display.flip()


pg.quit()

