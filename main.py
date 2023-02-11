from random import randint
class Unit:
    name="Unit"
    health=10
    damage=3
    def __init__(self,n,h,d):
        self.name=n
        self.health=h
        self.damage=d
    
    def show_stats(self):
        print(f"___ {self.name} ___")
        print(f"| health --> {self.health}\t|")
        print(f"| damage --> {self.damage}\t|")

    def is_alive(self):
        if self.health < 0:
            return False
        
        else:
            return True

class Enemy(Unit):
    armor = 3

    def __init__(self, n, h, d,a):
        super().__init__(n, h, d)
        self.armor = a
    
    def show_stats(self):
        super().show_stats()
        print(f"| armor --> {self.armor}\t|")
    
    def atack_hero(self,hero):
        if hero.is_alive():
            hero.health -= self.damage
            if hero.is_alive():
                print(f"{self.name}, dealt {self.damage} damage to {hero.name}")
            
            else:
                print(f"{self.name} killed {hero.name}")
        
        else:
            print(f"Ican't atack, {hero.name} is dead")
        
    def defend(self):
        def_chance = randint(1, 2)
        if def_chance == 1:
            return True
        else:
            return False

class Hero(Unit):
    strength = 1
    armor = 0

    def __init__(self, n, h, d,a):
        super().__init__(n, h, d)
        self.armor = a

    def show_stats(self):
        super().show_stats()
        print(f"| armor {self.armor}\t  |")
        print(f"| strength {self.strength}\t  |")
    
    def atack_enemy(self,enemy):
        if enemy.is_alive():
            enemy.health = ((enemy.health + enemy.armor) - (self.damage + (self.strength * 2)))
            if enemy.is_alive():
                print(f"{self.name}, dealt {self.damage} damage to {enemy.name}")
            
            else:
                print(f"{self.name} killed {enemy.name}")
        else:
            print(f"Ican't atack, {enemy.name} is dead")
    
    def defend(self):
        def_chace = randint(1, 3)
        if def_chace == 2:
            return False
        else:
            return True

    def heal(self):
        self.health += 10
        print(f"{self.name} healed by 10 points")
