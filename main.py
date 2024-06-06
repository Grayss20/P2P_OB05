from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец выбрал меч")
        print("Боец наносит удар мечем - Монстр побежден")

class Bow(Weapon):
    def attack(self):
        print("Боец выбрал лук")
        print("Боец стреляет из лука - Монстр побежден")

class Fighter:
    def __init__(self):
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon


class Monster:
    def __init__(self):
        pass

fighter = Fighter()
monster = Monster()

sword = Sword()
bow = Bow()

fighter.changeWeapon(sword)

fighter.weapon.attack()


fighter.changeWeapon(bow)

fighter.weapon.attack()


changeWeapon = sword


