print('Welcom to Hondo\'s books \n feel free to look around and let me know when your ready to purchase!')
print('Ahh welcome back, did you find everything alright? \n How many books are we purchasing today? (0 if no books for you)')
PointTotal = 0
BookNum = int(input('Please enter a number: '))
while BookNum != 0:
    if BookNum == 1:
        print(f'Ahh you\'ve purchased {BookNum} book. You\'ll be reciving 5 Points.')
        points = 5
        BookNum = 0
    elif BookNum == 2:
        print(f'{BookNum} books for you? That will be 15 Points for you!')
        points = 15
        BookNum = 0
    elif BookNum == 3:
        print(f'Wow, {BookNum} books for you? Thats gonna be 30 points on your account')
        points = 30
        BookNum = 0
    elif BookNum >= 4:
        print(f'My My!? {BookNum} books? Thats 60 points for you!')
        points = 60
        BookNum = 0
    PointTotal += points
    print(f'Your current point total is: {PointTotal}')
    BookNum = int(input('Any more Books for you?:'))
else:
    print(f'Have a Great day! Your Current Point total is: {PointTotal}. Come Back soon!')