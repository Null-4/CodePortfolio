'''
Nicholas Perez
Funtions: Math Quiz
C5-1(Return Function)
C5-2(Using Function)
C5-3(Module)
C5-4(Scope)
'''
import random #this here is me importing the random module so that i can use it to give random math problems (C5-3)

#global variable (C5-4)
problem = None
Answer = None

#This function will make the problems for the quiz. (C5-2)
def give_problem():
    print('Generating Problem(s)...')
    n1 = random.randint(1,50) # Number 1 
    n2 = random.randint(1,50) # Number 2
    aos = random.randint(1,2) # aos stands for Add or Subtract
    #These variables here are going to determin the question and if the question is addition or subtraction
    global problem , Answer 
    if aos == 1:
        problem= n1 + n2
        print(n1, "+",n2)
        Answer = int(input('Solve the problem and enter your answer here:'))
        print(f'You entered {Answer}.')
    elif aos == 2:
        problem = n1 - n2
        print(n1,"-",n2)
        Answer = int(input('Solve the problem and enter your answer here:'))
        print(f'You entered {Answer}.')
    return n1 , n2, aos #this here returns the variables n1, n2, and aos so that I can use them later (C5-1)
        

def check_answer(n1,n2,aos):
    if problem == Answer: 
        print('Congrats you got the question right!')
    else:
        if aos == 1:
            print(f'Sorry it looks like you got your answer wrong, The correct answer to {n1} + {n2} should be {problem}')
        else:
            print(f'Sorry it looks like you got your answer wrong, The correct answer to {n1} - {n2} should be {problem}')


#body of code
print('Hi, welcome to your math quiz. Hope you\'re ready for the test.')
Nop = int(input('How many questions would you like?\n>')) #Nop stands for Number of problems, Nop is only used here so this could be an example of local scope (C5-4)
for i in range(Nop):
    n1, n2, aos = give_problem()
    print('You have entered your answer to the question, now to see if you where right!')
    check_answer(n1, n2, aos)
