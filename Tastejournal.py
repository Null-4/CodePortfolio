'''
Nicholas Perez
Dictionaries and Sets: Taste Journal
C9-1(Dictionary)
'''
import pickle

#defining the dictionary system. (C9-1)
my_Dict = {}

#this function allows the user to enter a item and it will add it to my_dict
def FoodEntry():
    print('Please enter your food entry below.')
    entryF = input('>')           
    print('Now enter the discription of the taste below.')
    entryD = input('>')
    my_Dict[entryF] = entryD #this assigns the entries to the dictionary
    print('Entry Added!')              

#this funtion looks up the item that the user is looking for and then prints that entry and the value for it
def FoodLookup():
    print('Please enter the Item you want to lookup below.')
    entryF = input('>')
    try:
        print(my_Dict[entryF]) #this prints the item if its in the dictionary
    except KeyError: #this checks if the item is there at all and tells you to restart
        print('Sorry that Item wasn\'t found. Try again!')

#Body of code
print('Welcome to your very own Taste Journal!')
start = input('Would you like to begin? (y/n)\n>').lower().strip() #to initialize the while loop
while start == 'y':
    userinput = input('Please Enter 1:Enter a new entry 2:look up a previous entry 0:to end your entries.\n>') #this is your basic menu and its options
    if userinput == '1': #data entry
        FoodEntry()
        start = 'y'
    elif userinput == '2': #data lookup
        FoodLookup()
        start = 'y'
    elif userinput == '0': #Loop escape
        print('Please come back soon to use your Taste Journal!')
        start = False
    else: #validation
        print('Sorry that wasnt a valid option please choose 1, 2, or 0')
        start = 'y'


# P.S. Im working on the read and write data version just for fun, having a bit of an issue with that code so im going to submit this instead