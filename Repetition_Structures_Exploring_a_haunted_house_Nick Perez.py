'''
Nicholas Perez
Repetition Structures: Exploring a Haunted House
Badges
C4-1 (While Loops)
C4-2 (For Loops )
'''
Rooms = ['1:The Basement', '2:The Bedroom', '3:The Kitchen', '0:leave']
Hour_Total = 0

print('Welcome to the Haunted Mansion, Many dangers may find you here.')

print('Do you dare to enter? (y/n)')
Enter = input('>').lower()#this input is used to start the loop and to see if the user wants to enter the house

while Enter == 'y': #using a while loop to run the exploration of the haunted house. (C4-1)
    print('You have a choice presented before you. Which room do you choose?')
    for room in Rooms:# for loop to list the rooms in the list. (C4-2)
        print(room)
    print('Please enter the number of the room you want to explore.')
    choice = int(input('>'))#this input checks to see what room the user wants to explore
    if choice == 1 :
        print(f'You walk down the stairs and enter {Rooms[0]}.\nThough there is no light down here, yet you swear you can see a faint glow at the end of the basement.')
        Hour_Total +=1
        print('Would you like to keep exploring? (y/n)')
        Enter = input('>').lower()
    elif choice == 2:
        print(f'You are greeted by a grand room {Rooms[1]}.\nThis room is home to a large Bed in the middle, You can almost make out a shape rising and falling in the bed.\nThe room is filled with paintings that seem to stare at you as you walk.')
        Hour_Total +=1
        print('Would you like to keep exploring? (y/n)')
        Enter = input('>').lower()
    elif choice == 3:
        print(f'You walk down the hall and find {Rooms[2]}. This kitchen is coverd in what looks to be blood and vicera.\nThe smell is unbareable and nauseating.')
        Hour_Total +=1
        print('Would you like to keep exploring? (y/n)')
        Enter = input('>').lower()
    elif choice == 0:
        print('You find your way to the exit.')#this elif here is the sentinel to get out of te while loop.
        Enter = False
    else:
        print('Sorry that isnt a valid option try again.') #this is the variable validation, if you dont enter the correct option it restarts the loop for you to go again
        Enter = 'y'
else:
    if Hour_Total <1:
        print('You leave this place having not been subjected to it horrors within.')
    else:
        print(f'You leave The house after many trials, you Spent {Hour_Total} hours in there!')
