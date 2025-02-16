'''
Nicholas Perez
Dictionaries and Sets: Taste Journal
C9-1(Dictionary)
'''
import pickle

#defining the dictionary system.
my_Dict = {}

def FoodEntry():
    print('Please enter your food entry below.')
    entryF = input('>')
    try:
        with open('Journal.txt','ab') as Jfile:
            pickle.load(Jfile)
            if entryF in Jfile:
                print(f'you already have this entry, here\'s the entry: {my_Dict[entryF]}.')
            else:
                print('Now enter the discription of the taste below.')
                entryD = input('>')
                with open('Journal.txt','ab') as Jfile:
                    my_Dict[entryF] = entryD
                    pickle.dump(my_Dict, Jfile)
                    print('Entry added!')   
    except:
        print('test')

def FoodLookup():
    print('Please enter the Item you want to lookup below.')
    entryF = input('>')
    try:
        with open('journal.txt','rb') as Jfile:
            try:
                savedata = pickle.load(Jfile)
                print(savedata[entryF])
            except KeyError:
                print('Sorry that Food Wasn\'t found.')
    except FileNotFoundError:
        print('Sorry the Jounal you are attempting to look up doesnt exist.')


#Body of code
print('Welcome to your very own Taste Journal!')
start = input('Would you like to begin? (y/n)\n>').lower().strip()
while start == 'y':
    userinput = input('Please Enter 1:Enter a new entry 2:look up a previous entry 0:to end your entries.\n>')
    if userinput == '1':
        FoodEntry()
        start = input('Would you like to continue? (y/n)\n>')
    elif userinput == '2':
        FoodLookup()
        start = input('Would you like to continue? (y/n)\n>')
    elif userinput == '0':
        print('Please come back soon to use your Taste Journal!')
        start = False
    else:
        print('Sorry that wasnt a valid option please choose 1, 2, or 0')
        start = 'y'
    