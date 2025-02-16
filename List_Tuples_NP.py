'''
Nicholas Perez
Lists and Tuples
C7-1 Random
'''

import random

Personalites = ['Normal','Lazy','Sisterly','Snooty','Cranky','Jock','Peppy','Smug']
Hobbies = ['Education','Fashion','Fitness','Music','Nature','Playing']

def AP(): #AP stands for Assign Personality 
    Personality = random.choice(Personalites) #chooses a random option out of the list (C7-1)
    return Personality

def AH(): #AH stands for Assign Hobby
    Hobby = random.choice(Hobbies) #chooses a random option out of the list (C7-1)
    return Hobby

#body of code
print('Welcome to your village!\nFirst we need to name your villager.')
name = input('Whats your villagers name?\n>')
print(f'Lovely to meet you {name}!')
print(f'Looks like {name} is {AP()} and they\'re into {AH()}.')