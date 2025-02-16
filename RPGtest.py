import random

class player:
    def __init__(self,):
        self.__HP = 10
        self.__Defence = 1
        self.__Attak_Power = 1
        self.KO = False
        self.XP = 0
        self.__xpg = 10
    
    
    def LVLUP(self):
        if self.XP >= self.__xpg:
            print("You've leveled up!! Attak power and Defense have improved!")
            self.__Attak_Power += 1
            self.__Defence += 1
            self.__xpg += 10
        else:
            print(f"Your current Xp amount is: {self.XP}. You need {self.__xpg} to lvl up")

    def Attack(self):
        mods = [1,1,1,1,1,1,1,2]
        mod = random.choice(mods)
        dmg = self.__Attak_Power * mod
        print(f"you swing your weapon and deal {dmg} points of damage!")

hero = player()


hero.Attack()
print('your attack killed the enemy, you gained 15 points of xp')
hero.XP = 15
hero.LVLUP()
hero.Attack()

