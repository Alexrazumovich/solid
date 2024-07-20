from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def __init__(self,power):
        self.power = power
    def attack(self):
         print("I swing my sword!")
class Bow(Weapon):
     def __init__(self, power):
         self.power = power
     def attack(self):

         print("I shoot an arrow!")
class Fighter():
     def __init__(self, weapon: Weapon):
         self.weapon = weapon
     def changeWeapon(self,weapon):
         self.weapon = weapon
     def fight(self):
         self.weapon.attack()
class Monster():
     def __init__(self, weapon: Weapon):
         self.weapon = weapon
def result(a,b):
    if a == b:
        c="Draw"
        return c
    elif a>b:
        c="Monster died"
        return c
    else:
        c="Fighter died"
        return c


sword = Sword(20)
bow = Bow(15)
fighter = Fighter(bow)
monster = Monster(bow)
fighter.fight()
res=result(fighter.weapon.power,monster.weapon.power)
if res=="Draw":
    print("It's a draw! Try change weapon!")
    fighter.changeWeapon(sword)
    fighter.fight()
    res=result(fighter.weapon.power,monster.weapon.power)
    print(res)
else:
    print(res)

