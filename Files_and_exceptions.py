'''
Files & exceptions
c6-1 (try and except)
c6-2 (read and wite data)
'''

def sum_odd_lines(filename): #establishing the funtion
    try: #this is going to check to see if the file is a workable file, it trys the file and otherwise it should say file not found. (C6-1)
        with open(filename, 'r') as file:
            total = 0 #this establishes the base line total
            for line in file:
                try: #checks the value and if its not a correct value it will just say wong value and skip continue
                    file.readline()#this reads the file and the line so that the data can be addedd
                    total += int(line.strip())
                    print(line)
                except ValueError: #checks the value and if its not a correct value it will just say wong value and skip continue
                    print('Sorry the line was not a useable value.')
        print(f'The found total of the odd lines is: {total}.')
    except FileNotFoundError: #this is going to check to see if the file is a workable file, it trys the file and otherwise it should say file not found.(C6-1)
        print('Sorry file not found.')

#body of code, executes the sum odd lines function   
filename = input('Enter file name or file path.\n>')
sum_odd_lines(filename)
