from character import *
from random import *


player = Player()
pcplayinput=""
Cplayinput = ""
enemyArr = []
player.add_powers("poison",3,2)
player.add_powers("curse",2,3)
player.add_powers("burn", 4,5)


def enemyActions(taker, pos=0, target=player):
   m = randint(1, 100)
   if taker.get_nature() == "craven" and ((taker.get_health() / taker.get_base_health()) * 100) < 30-m/30:
       taker.set_health(0)
       print(taker.get_type() + " Ran away")
       if pos > -1:
           enemyArr.pop(pos)
   elif m > 30:
       taker.attack(target)
   if taker.get_nature == "aggressive" and m > 90:
       taker.attack(target)






def createEnemy(type="null"):
   if type == "null":
       s = randint(1, 100)
       if s >= 1 and s <= 69:  # goblin
           enemy = Goblin()
       elif s >= 70 and s <= 100:  # orc
           enemy = Orc()
   else:
       if type == "orc":
           enemy = Orc()
       elif type == "goblin":
           enemy = Goblin()
   return (enemy)




def Cplayerinput(text="", cap=False,strip=True):
   global Cplayinput, pcplayinput
   pcplayinput=Cplayinput
   Cplayinput = input(text)
   if cap == False:
       Cplayinput = Cplayinput.lower()
   if strip== True:
      Cplayinput.strip()
   return (Cplayinput)




def spawnEnemies(num1=1, num2=10, clear=True):
   global enemyArr
   if clear == True:
       enemyArr = []
   numE = randint(num1, num2)
   for r in range(numE):
       enemyArr.append(createEnemy())




def combat():
   global enemyArr
   turnCount = 1
   while len(enemyArr) > 0:
       if Cplayinput == "r":
           print("you ran away")
           break
       print("Turn " + str(turnCount))
       print("Your health is "+str(player.get_health()))
       for l in range(len(enemyArr)):
           if len(enemyArr)<l:
               kj=len(enemyArr)-l
               l+=kj
           for e in enemyArr[l].get_effects():
               if e=="poison":
                   poison(enemyArr[l])
               if e=="curse":
                   curse(enemyArr[l])
               if e=="burn":
                   burn(enemyArr[l])

           if enemyArr[l].get_health() <= 0 and len(enemyArr)!=0:
               print(enemyArr[l].get_type() + " has died")
               enemyArr.pop(l)
               if len(enemyArr)==0:
                   print("You killed them All")
                   break
           if len(enemyArr)<l:
               kj=len(enemyArr)-l
               l+=kj
           print(str(l+1) + ". Enemy: " + enemyArr[l].get_type() + "(" + str(enemyArr[l].get_health()) + "hp)")
       player.set_defence(player.get_base_defence())
       if len(enemyArr) == 0:
           break
       while True:
           Cplayerinput(
               "what do you want to do \n A. attack        D. defend \n R. runaway       S. stats(keeps turn)\n")
           if Cplayinput == "a":
               Cplayerinput("type in the number of the enemy you want to attack\n")
               try:
                   while int(Cplayinput)>len(enemyArr):
                       print("That wasn't an enemy")
                       Cplayerinput()
               except ValueError:
                   print("That wasn't a number")
                   Cplayerinput()
               player.attack(enemyArr[int(Cplayinput)-1])
               break
           elif Cplayinput == "d":
               player.set_defence(player.get_base_defence() + 5)
               print("you've increased your defence by 5")
               break
           elif Cplayinput == "r":
               break
           elif Cplayinput == "s":
               Cplayerinput(
                   "Type m for your stats, type i to get the enemy index, or type the number of the enemy you want info about\n")
               if Cplayinput == "m":
                   print("Your name is " + player.get_name() + "\n  your health is " + str(
                       player.get_health()) + "\n  your damage is " + str(
                       player.get_damage()) + "\n  your defence is " + str(player.get_defence()))
               elif Cplayinput == "i":
                   Cplayerinput("Type the type of enemy you want to know about\n")
                   if Cplayinput == "goblin":
                       r = Goblin()
                   elif Cplayinput == "orc":
                       r = Orc()
                   print("a "+r.get_type()+"'s health is " + str(r.get_health()) + "\n a"+r.get_type()+"'s damage is " + str(r.get_damage()) + "\n a "+r.get_type()+"'s defence is " + str(r.get_defence()))
               else:
                   r=enemyArr[int(Cplayinput)-1]
                   print("a " + r.get_type() + "'s health is " + str(r.get_health()) + "\n a" + r.get_type() + "'s damage is " + str(r.get_damage()) + "\n a " + r.get_type() + "'s defence is " + str(r.get_defence()))
       for x in range(len(enemyArr)-1):
           enemyActions(enemyArr[x],x)
       turnCount += 1


# while Cplayinput!="yes":
#   player.set_name(Cplayerinput("Type in your name",True))
#   print(player.get_name()+" is this correct? Type yes or no")
#   Cplayerinput()
# goblin=createEnemy("goblin")
# print(goblin.get_health())
# player.set_damage(20)
# player.attack(goblin)
# print(goblin.get_health())
# goblin.attack(player)
# print(player.get_health())
# player.attack(goblin)
# print(player.get_kills())
# while Cplayinput!="quit":
#     spawnEnemies(1,3)
#     combat()
