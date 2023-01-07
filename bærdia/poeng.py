
import time
from pygame.locals import *
import pygame as pg

pg.init()
pg.display.set_caption("Top-G pong")
font=pg.font.SysFont("Ariel", 35)
fontSmall=pg.font.SysFont("Ariel", 15)

blck = (0,0,0)
hvit = (255,255,255)

size = [700, 500]
S = pg.display.set_mode(size)

P=pg.Rect(200,(S.get_height()-120),162,20)
fart=1


clock = pg.time.Clock()
clock.tick(60)
point=0
carryOn1 = True
carryOn2=True
carryOn3=True
carryOn4 =True


class Ball:
    def __init__(self, radius, x_pos, y_pos, fart,mainScreen):
        self.r=radius
        self.x=x_pos
        self.y=y_pos
        self.f=fart
        self.fy=fart
        self.s= mainScreen


    def tegn(self):
        pg.draw.circle(self.s, hvit,(self.x,self.y), self.r)

    def move(self):
        if ((self.x+self.r) >= self.s.get_width()) or ((self.x-self.r) <= 0): 
            self.f=-self.f
        if ((self.y-self.r) <= 0)  or ((self.y+self.r) >= self.s.get_height()):
            self.fy=-self.fy

        self.y+=self.fy
        self.x+=self.f

class Button:  
    def __init__(self, text, x_pos, y_pos):
        self.txt=text
        self.x=x_pos
        self.y=y_pos
    
    def draw(self):
        HbuttonTxt= font.render(self.txt,True, "white" )
        buttonTxt= font.render(self.txt,True, "black" )
        buttonRect= pg.rect.Rect((self.x,self.y),(190,60))
        self.buttonRect=buttonRect

        if self.hover():
            pg.draw.rect(S, "green", buttonRect, 0,5)
            pg.draw.rect(S, "light grey", buttonRect, 2,5)
            S.blit(HbuttonTxt, (self.x+18, self.y+20))
        else:
            pg.draw.rect(S, "light grey", buttonRect, 0,5)
            pg.draw.rect(S, "green", buttonRect, 2,5)
            S.blit(buttonTxt, (self.x+18, self.y+20))

    def hover(self):
        musPos=pg.mouse.get_pos()
        if  self.buttonRect.collidepoint(musPos):
            return True
        else:
            return False

    def clickCheck(self):
        musPos=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()[0]
        if click and self.buttonRect.collidepoint(musPos):
            return True
        else:
            return False

B=Ball(15,150,100,0.4,S)
welcomeButton=Button("click to start!",265,250)

while carryOn1:      
    
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            carryOn1=False
            carryOn2=False
            carryOn3=False
            carryOn4=False

        if event.type == pg.MOUSEBUTTONDOWN:
            if welcomeButton.clickCheck():
                carryOn1=False      
    S.fill(blck) 
    welcomeButton.draw()
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
    pg.draw.rect(S,"green",P,2,5)
    playerTag=fontSmall.render("player", True,"black")
    S.blit(playerTag,(P.x+70,P.y+5))

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
    pg.draw.rect(S,"green",P,2,5)
    playerTag=fontSmall.render("player", True,"black")
    S.blit(playerTag,(P.x+70,P.y+5))
    
    key=pg.key.get_pressed()

    if key[pg.K_LEFT]:
        P.move_ip(-fart, 0)
    if key[pg.K_RIGHT]:
        P.move_ip(fart, 0)
 

    if P.collidepoint(B.x, B.y+ B.r):
        B.f = -B.f
        B.fy= -B.fy
        point+=1
        pg.time.wait(80)      # et små vent for å unngå mulige glitcher
   
    if (B.y+B.r) >= S.get_height():         
        game_over=font.render("Game Over!", True, (50,255,50))
        S.blit(game_over, (270,200)) 
        pg.display.flip()
        pg.time.wait(1500)
        S.fill(blck) 
        game_over=font.render("Game Over!", True, (50,255,50))
        S.blit(game_over, (270,200)) 
        pg.display.flip()
        pg.time.wait(1000)
        carryOn3=False 

    pg.display.flip()

if(carryOn4):
    size = [400, 200]
    S = pg.display.set_mode(size)

while carryOn4:

    S.fill(blck) 
    score=font.render(f"du fikk {point} mål!", True, (50,255,50))
    S.blit(score, (110,80))
    pg.display.flip()
    pg.time.wait(1000) #uansett noe gjort fra brukern vises poengene for et sek :)
    
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            carryOn4=False
        if event.type == pg.QUIT:
            carryOn4=False

pg.quit()

