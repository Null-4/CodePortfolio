'''
Nicholas perez
Object oriented Programming
Badge C10-1 (Class)
'''
class monster: #this is the class (c10-1)
    
    def __init__(self, name, m_type):
        self.__name = name
        self.__monster_type = m_type

    #Methods
    def set_name(self,name):
        self.__name = name 

    def set_monster_type(self, monster_type):
        self.__monster_type = monster_type

    def get_name(self):
        return self.__name

    def get_monster_type(self):
        return self.__monster_type

    def scare(self):
        if self.__monster_type =='frakenstein':
            print("Fire Bad!")
        elif self.__monster_type == "werewolf":
            print("Awoooo!") 
        elif self.__monster_type == "dracula": 
            print("Bleh!")
        else:
            print("Boo!")   

monster_1 = monster('Frank', 'frankenstein')
monster_2 = monster('luna', 'werewolf')

print(f'{monster_1.get_name()} is a {monster_1.get_monster_type()}')
monster_1.scare()
print('')
print(f'{monster_2.get_name()} is a {monster_2.get_monster_type()}')
monster_2.scare()