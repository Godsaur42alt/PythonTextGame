from character import *
from Maze import *
from random import *


player = Player()
playinput = ""
enemyArr = []




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




def playerinput(text="", cap=False,strip=True):
   global playinput
   playinput = input(text)
   if cap == False:
       playinput = playinput.lower()
   if strip== True:
      playinput.strip()
   return (playinput)




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
       if playinput == "r":
           break
       print("Turn " + str(turnCount))
       print("Your health is "+str(player.get_health()))
       for l in range(len(enemyArr)):
           if enemyArr[l].get_health() <= 0:
               print(enemyArr[l].get_type() + " has died")
               enemyArr.pop(l)
           print(str(l+1) + ". Enemy: " + enemyArr[l].get_type() + "(" + str(enemyArr[l].get_health()) + "hp)")
       player.set_defence(player.get_base_defence())
       while True:
           playerinput(
               "what do you want to do \n A. attack        D. defend \n R. runaway       S. stats(keeps turn)\n")
           if playinput == "a":
               playerinput("type in the number of the enemy you want to attack\n")
               player.attack(enemyArr[int(playinput)-1])
               break
           elif playinput == "d":
               player.set_defence(player.get_base_defence() + 5)
               print("you've increased your defence by 5")
               break
           elif playinput == "s":
               break
           elif playinput == "d":
               playerinput(
                   "Type m for your stats, type i to get the enemy index, or type the number of the enemy you want info about\n")
               if playinput == "m":
                   print("Your name is " + player.get_name() + "\n  your health is " + str(
                       player.get_health()) + "\n  your damage is " + str(
                       player.get_damage()) + "\n  your defence is " + str(player.get_defence()))
               elif playinput == "i":
                   playerinput("Type the type of enemy you want to know about\n")
                   if playinput == "goblin":
                       r = Goblin()
                   elif playinput == "orc":
                       r = Orc()
                   print("a "+r.get_type()+"'s health is " + str(r.get_health()) + "\n a"+r.get_type()+"'s damage is " + str(r.get_damage()) + "\n a "+r.get_type()+"'s defence is " + str(r.get_defence()))
       for x in range(len(enemyArr)-1):
           enemyActions(enemyArr[x],x)
       turnCount += 1


# while playinput!="yes":
#   player.set_name(playerinput("Type in your name",True))
#   print(player.get_name()+" is this correct? Type yes or no")
#   playerinput()
# goblin=createEnemy("goblin")
# print(goblin.get_health())
# player.set_damage(20)
# player.attack(goblin)
# print(goblin.get_health())
# goblin.attack(player)
# print(player.get_health())
# player.attack(goblin)
# print(player.get_kills())
spawnEnemies(1,3)
combat()
