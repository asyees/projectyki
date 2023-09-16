import random

class Enemy:
  eName = "Name"
  eHealth = 0
  eStrength = 0
  def __init__ (self, eName, eHealth, eStrength):
    self.eName = eName
    self.eHealth = eHealth
    self.eStrength = eStrength


  def attack (self):
    print("The enemy attacked you and dealt", self.eStrength, "damage!")
    Hero.health -= self.eStrength



  def __repr__(self):
    if self.eName == "Zombie":
      return "Zombie"
    elif self.eName == "Skeleton":
      return "Skeleton"
    else:
      return "Spider"

class Hero:
  name = "Name"
  health = 0
  strength = 0
  def __init__ (self, name, health, strength):
    self.name = name
    self.health = health
    self.strength = strength
  def attack(self, enemy):
    print("You attacked", enemy, "for", self.strength, "damage!\n")
    Enemy.eHealth -= self.strength
    print(enemy, "now has", enemy.eHealth, "health points left!\n")

print("Welcome to my fighting simulator!")
hName = input("Please input your character's name:\n")
hHealth = int(input("Please enter your hero's amount of health points (10-25):\n"))
hStrength = int(input("Please enter your hero's amount of strength points (2-4): \n"))
character = Hero(hName, hHealth, hStrength)

zombie = Enemy("Zombie", 25, 3)
skeleton = Enemy("Skeleton", 15, 4)
spider = Enemy("Spider", 20, 2)

randEnemy = random.randint(1, 3)

if randEnemy == 1:
  print("\nYour enemy will be a zombie!\n")
  chosenEnemy = zombie
elif randEnemy == 2:
  print("\nYour enemy will be a skeleton!\n")
  chosenEnemy = skeleton
else:
  print("\nYour enemy will be a spider!\n")
  chosenEnemy = spider

while True:
  if character.health == 0:
        print("You died!")
  elif chosenEnemy.eHealth == 0:
    print("You won!")
      action = input("What would you like to do? (h = heal, a = attack): ")
  if (action == 'a') or (action == 'A'):
    character.attack(chosenEnemy)