import math
import random

print('Lets have some fun and roll some dice!')
print('If you roll higher you win!')
start = input('Are you up for the challenge?').lower()
'''
the above introduces the program and then asks if they want to play
if they dont want to play it should end the program
'''

#seting up the dice rolls early so i can just call back to the variables

while start == 'yes': 
    DR1 = random.randint(1,6)

    DR2 = random.randint(1,6)

    PR1 = random.randint(1,6)

    PR2 = random.randint(1,6)
    print('lets start!')
    print('lets roll your first die')
    print(PR1)
    print('Lets roll your second die')
    print(PR2)

    PRT = PR1+PR2

    print('Your total is', PRT)

    DRT = DR1+DR2

    print('my total was', DRT)
    #the above print functions are used to set up the dice totals

    if (PRT>DRT):
        print('You win!')
    elif (PRT < DRT):
        print('Sorry you lose!')
    elif (PRT == DRT):
        print('Wow we tied!')
    start = input('Wanna Play again?').lower()
else:
    quit('Aww, Too Bad!')

