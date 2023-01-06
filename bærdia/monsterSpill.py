
"""
spill beskrivelse: 
spillet handler mellom en monster og en spiller og dreier seg over 2 runder. 
hver en er en objekt fra klassen Character som inneholder egenskaper og metodene deres

hver runde gjetter spillern sin element for å kombate monsteret
og prøver og gjette seg strengthen sin monsteret så nær så mulig
strengthen være et tall i forhold
spillern skal samle nok strength for å nullgjøre health-en til monsteret

hoveddeler:
1. name & setup
2. elements
3. strength

"""
import random as r

class Charater:
    """
    brukes som et slag framework for hver person i spiller nemlig monsteren og spillern 

    egenskaper:
    1. name
    2. element
    3. strength
    4. health 

    metode:
    __innit__()
    __str__()
    health_check()
    
    """
    def __init__(self,n, s, e1, e2, h):
        self.name=n
        self.strength=s
        self.first_element=e1
        self.second_element=e2
        self.health=h

    def healthCheck(self):
        if(self.health<=0):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.strength}"


M=Charater("",0,0,0,30)
P=Charater("",0,0,0,0)

#names: --> navnene blir henta inn og spille settes i gang 

print("in order to start the game we must first know who u are!")
P.name=input("name: ")
M.name="the Big V"
print("\n")
print(f"heyyy {P.name}, at last we meet our hero! ")
print(f"the one and only u which  will be facing {M.name} the monster of the Soutt, in the battlefield! ")

print(f"side note: the monster has {M.health} points on his health bar! a though one right? :)")

confirm=input("lets see if u can do sth abt it, u ready for the battlefeild!?! ") 

#start med intro
print("\n")
print(f"okay, before we get into it, welcome to the Battlefield {P.name}!")
print(f"now u get to choose 2 elemets for ur battle against {M.name} each ability/element will be used in 2 rounds where it effects ur strength in the battle, choose wisley!")
confirm=input("u ready to roll? ...")
print("\n")

# element 1.Round: --> spillern velger sin element og Monsteren sin blir Tilfeldigvis satt
print("1.Round ability/element:")

elementList=["fire","earth", "wind","water"]
format=False
while not(format):
    try:    #sjekker om spillern gir for det først en tall inni alternativene og at det skal være et tall
        for i in range(0,len(elementList)):
            print("for the element ", elementList[i],", enter number ", i)
        P.first_element=int(input("enter ur choosen number: "))
        print("\n")
        print(f"well looks like u feelin the {elementList[P.first_element]} for 1.Round! ")
        format=True
    except (IndexError, ValueError):
        print("hmm...seems like u not that good with numbers huh!")
        print( f"{P.name} try to choose ur element with the RIGHT NUMBER again :)")
        print("\n")
        
M.first_element=r.randint(0,3)
print(f"the monster has the element {elementList[M.first_element]}")

# Element mulitplier: 
elementMultiplier=0.0 # en metode brukt for å påvirke slutte strength til spiller basert på valg av element
if P.first_element==M.first_element:
    elementMultiplier=0.7
elif abs(P.first_element-3)==M.first_element:
    elementMultiplier=1.5
else:
    elementMultiplier=1
print(f"that means u got {elementMultiplier}x multiplier for the 1.Round")
confirm=input("lets check how strong u are!...press enter to continue")
print("\n")

#******************
# strength: --> momsteren får sin tilfeldig strength og spiller prøver og gjette det

M.strength= r.randint(5,20)
print("Now off to ur Strength...") 
print(f"u will get ur strength depending on how close u guess {M.name}'s strength :))")

# metoden brukt for å forholdet monsteren sin strength og spillern sin
format=False
while not(format):
    try:    #sjekker for riktig range og type til gjett variabelen
        gjett = int(input("guess how many strength points the monster has collected for the 1.Round(5-20): ")) 
        if(gjett<=20 and gjett>=5):
            format=True
        else:
            print("pls get ur guess in the given range :(")
            print("\n")
    except ValueError:
        confirm=input("ur guess shld be a number, press enter to try again...")
        print("\n")

multi = gjett/M.strength
if 1.7>multi>0.7:
    if multi>=1:
        P.strength=multi*M.strength*elementMultiplier
    if multi< 1:
        P.strength= ((1-multi)+1)*M.strength*elementMultiplier
else:
    if multi>1:
        P.strength= abs((multi-1))* M.strength*elementMultiplier
    if multi <=1:
        P.strength= multi*1.2*M.strength*elementMultiplier
P.strength=round(P.strength,0)

print("\n")
print(f"the monster has gathered {M.strength} strength points!")
print(f"with ur guess u managed to have {P.strength} strength points! ")

# health: --> trekker strength fra healthen og neste runde start
print("\n")
M.health=int(M.health-(P.strength))
if M.health>=0:
    print("monsters health:",M.health)
else:
    print("monsters health:",0)

if M.healthCheck():
    print ("congrats! u managed to defeat the monster with one round :)")
    print(M.health)

else:   # second round
    confirm=input("please enter next round by typing ready: ")
    
    print("round 2 begins! \n")
    print(" 2. Round ability/element:")
    elementList=["fire","earth", "wind","water"]

    format=False
    while not(format):
        try:  #sjekker om spillern gir for det først en tall inni alternativene og at det skal være et tall
            for i in range(0,len(elementList)):
                print("for the element ", elementList[i],", enter number ", i)
            P.second_element=int(input("enter ur choosen number: "))
            print("\n")
            print(f"well looks like u feelin the {elementList[P.second_element]} for 2.Round! ")
            format=True
        except (ValueError, IndexError):
            print("\n")
            print("hmm...seems like u not that good with numbers huh!")
            print( f"{P.name} try to choose ur element with the RIGHT number again :)")
        
    M.second_element=r.randint(0,3)
    print(f"the monster has the element {elementList[M.second_element]} this time!")
    confirm=input("feelin as strong? ...press enter to continue")
    print("\n")

    elementMultiplier=0.0
    if P.second_element==M.second_element:
        elementMultiplier=0.7
    elif abs(P.second_element-3)==M.second_element:
        elementMultiplier=1.5
    else:
        elementMultiplier=1
    print(f"that means u got {elementMultiplier}x multiplier for the 2.Round")
    print("\n")

    # strength: 
    M.strength=r.randint(5,20)
    format=False
    while not(format):
        try: #sjekker for riktig range og type til gjett variabelen
            gjett = int(input("guess how many strength points the monster has collected for the 2.Round(5-20): ")) 
            if(gjett<=20 and gjett>=5):
                format=True
            else:
                print("pls get ur guess in the given range :(")
                print("\n")
        except ValueError:
            confirm=input("ur guess shld be a number, press enter to try again...")
            print("\n")

    multi = gjett/M.strength  
    if 1.7>multi>0.7:
        if multi>1:
            P.strength=multi*M.strength*elementMultiplier
        if multi<= 1:
            P.strength= ((1-multi)+1)*M.strength*elementMultiplier
    else:
        if multi>1:
            P.strength= abs((multi-1))* M.strength*elementMultiplier
        if multi <=1:
            P.strength= multi*1.2*M.strength*elementMultiplier
    P.strength=round(P.strength,0)

    print("\n")
    print(f"the monster has gathered {M.strength} strength points!")
    print (f"with ur guess u managed to have {P.strength} strength points! ")

        
    M.health=int(M.health-(P.strength))
    print("\n")
    if M.health>=0:
        print("monsters health:",M.health)
    else:
        print("monsters health:",0)

    if M.healthCheck():
        print ("congrats! u managed to defeat the monster :)")
        
    else:
        print("the monster still has", int(M.health), " points on his health bar")
        print("game over! nice effort, maybe next time :)")


# 0=fire  1=earth   2=wind   3=water


