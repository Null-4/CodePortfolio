'''
Nicholas perez
Badge C3-1(else/if)
Badge C3-2(Boolean)
Badge C3-3(comparisons)
'''
Password1 = 'pickle'
Password2 = 'class'
Password3 = 'elif'
Password4 = 'variable'
Password5 = 'function'
Password6 = 'block'
#The above code just defines my passwords before hand so I dont have to worry about it later

print('Door: Welcome, state the passwords for entry.')
Input1 = input('>').lower()
print('Door: Now enter your second password.')
Input2 = input('>').lower()
#This above code just takes the users input and stores that as a variable

if (Input1 == Password1 or Input1 == Password2) and ( Input2 == Password1 or Input2 == Password2) and (Input1 != Input2):# This if funtion is checking to see if the inputs are correct and to make sure they don't equal each other so they can't cheat (C3-1)
    print('Door: Welcome to the Pastafarians brother!')# this here is the result if the input1 and input2 are correct (c3-2)
elif (Input1 == Password3 or Input1 == Password4) and ( Input2 == Password3 or Input2 == Password4) and (Input1 != Input2):
    print('Door: Welcome brother to the Illuminati!')
elif (Input1 == Password5 or Input1 == Password6) and ( Input2 == Password5 or Input2 == Password6) and (Input1 != Input2):#this code similarly to the code above
    print('Door: Ahhh, a fellow appreciator of the arts, welcome to the Grand Wizard Acadamy!')
else:
    exit('Door: LEAVE AND NEVER RETURN!!!')

