import time
from pygame.locals import *
import pygame as pg

pg.init()
pg.display.set_caption("Top-G pong")
font=pg.font.SysFont("Ariel", 25)
moveNum=10

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

B=Ball(15,150,100,0.3,S)
P=pg.Rect(200,(S.get_height()-120),162,20)
fart=1

carryOn = True
clock = pg.time.Clock()
clock.tick(60)


# -------- Main Program Loop -----------
while carryOn:

    key=pg.key.get_pressed()
    # --- Main event loop
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT or (key[K_LEFT]) or (key[K_RIGHT]): # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        
    velkommen=font.render("velkommen til min pong-spill!", True, (50,255,50))
    S.blit(velkommen, (235,50))
    pg.display.flip()
        

carryOn=True
point=0

while carryOn:
    
    # --- Main event loop
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
    S.fill(blck)   
    

    ScoreBoard=font.render(str(point), True, (50,255,50))
    S.blit(ScoreBoard, (S.get_width()-60,60))

    B.tegn()
    B.move()
    pg.draw.rect(S,hvit,P)

    key = pg.key.get_pressed()
    
    if key[pg.K_LEFT]:
        P.move_ip(-fart, 0)
    if key[pg.K_RIGHT]:
        P.move_ip(fart, 0)

    
    if P.collidepoint(B.x, B.y+ B.r):
        B.f = -B.f
        B.fy= -B.fy
        point+=1
        fix=0
        while True:
            if P.collidepoint(B.x,B.y+ B.r):
                fix+=1
                P.move_ip(0,10)
            else:
                P.move_ip(0,-fix*10)
                break
    if (B.y+B.r) >= S.get_height():    
        print("kom hit")
        carryOn=False 
        break
         

    pg.display.flip()
    

pg.quit()

