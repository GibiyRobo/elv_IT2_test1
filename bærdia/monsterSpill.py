
import random as r

class Charater:
    def __init__(self,n, s, e1, e2, e3, h):
        self.name=n
        self.strength=s
        self.first_element=e1
        self.second_element=e2
        self.third_element=e3
        self.health=h

    def healthCheck(self):
        if(self.health<=0):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.strength}"


M=Charater("",0,0,0,0,30)
P=Charater("",0,0,0,0,0)

#names: 

print("in order to enter the game we must first know how u are!")
print("\n")
P.name=input("name: ")
M.name="the Big V"
print(f"heyyy {P.name}! u will be facing {M.name} the monster of the South! in the battlefield")
print(f"the monster has {M.health} points on his health bar!")
confirm=input("lets see if u can do sth abt it, are u ready!?! ")

# element 1. Round:
print(f"okay, welcome to the Battlefield {P.name}! now u get to choose 3 ability for ur battle against {M.name}")
print("each ability/element will be used in 2 rounds where it effects ur strength in the battle, choose wisley!")
print("\n")

print("1.Round ability/element:")

elementList=["fire","earth", "wind","water"]

for i in range(0,len(elementList)):
    print("for the element ", elementList[i],"enter number ", i)

P.first_element=int(input("enter ur choosen number: "))
print("\n")
print(f"well looks like u feelin the {elementList[P.first_element]} for 1.Round! ")
M.first_element=r.randint(0,3)
print(f"the monster has the element {elementList[M.first_element]}")

elementMultiplier=0.0
if P.first_element==M.first_element:
    elementMultiplier=0.7
elif abs(P.first_element-3)==M.first_element:
    elementMultiplier=1.5
else:
    elementMultiplier=1
print(f"that means u got {elementMultiplier}x multiplier for the 1.Round")
print("\n")

#******************
# strength: 

M.strength= r.randint(5,20)
print("Now off to ur Strength:") 
print(f"u will get ur strength depending on how close u guess {M.name}'s strength :))")
multi = int(input("guess how many strength points the monster has collected for the 1.Round(5-20): "))/M.strength


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
print("\n")
print(f"the monster has gathered {M.strength} strength points!", "\n", f"with ur guess u managed to have {P.strength} strength points! ")

M.health=int(M.health-(P.strength))

print("monsters health:",M.health)

if M.healthCheck():
    print(M.strength)
    print ("player won")
    print(M.first_element, P.first_element)
    print(" u got multiplier for", elementMultiplier)
    print(M.strength,P.strength)
    print(M.health)

else:   
    confirm=input("please enter nnext round by typing ready: ")
    
    print("round 2 begins! \n")
    print(" 2. Round ability/element:")
    elementList=["fire","earth", "wind","water"]

    for i in range(0,len(elementList)):
        print("for the element ", elementList[i],"enter number ", i)

    P.second_element=int(input("enter ur choosen number: "))
    print("\n")
    print(f"well looks like u feelin the {elementList[P.second_element]} for 1.Round! ")
    M.second_element=r.randint(0,3)
    print(f"the monster has the element {elementList[M.second_element]}")

    elementMultiplier=0.0
    if P.second_element==M.second_element:
        elementMultiplier=0.7
    elif abs(P.second_element-3)==M.second_element:
        elementMultiplier=1.5
    else:
        elementMultiplier=1
    print(f"that means u got {elementMultiplier}x multiplier for the 1.Round")
    print("\n")

    # strength: 
    M.strength=r.randint(5,20)
    multi = int(input( "guess the strength u will need to finish him in the 2.Round(5-20):"))/M.strength

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
    print("\n")
    print(f"the monster has gathered {M.strength} strength points! ", "\n", f"with ur guess u managed to have {P.strength} strength points! ")

        
    M.health=int(M.health-(P.strength))
    #print("\n")
    print("monsters health: ",int(M.health))

    if M.healthCheck():
        print ("player won")
        
    else:
        print("the monster still has", int(M.health))
        confirm=input("game over! try again -->")


# 0=fire  1=earth   2=wind   3=water


