# s for snake --    1
# g for gun --      0
# w for water --    -1

# Behind the scenes, we can take the dictionary and map the output. 

import random

yourChar = input('Enter your choice between\ns for SNAKE\ng for GUN\nw for WATER\nq to QUIT')
yourDict = {'s': 1, 'g': 0, 'w': -1}
revDict = {1: 'Snake', 0: 'Gun', -1: 'Water'}

ai = random.choice([-1, 1, 0])
you = yourDict[yourChar]

print(f'AI selected {revDict[ai]} while you selected {revDict[you]}')

if ai == you:
    print ('It is a draw')

else: 
    if(ai == -1 and you == 1):  # ai = water + you = snake : YOU WIN
        print('You WIN !!!') 
        
    elif ai == 1 and you == 0:  # ai = snake + you = gun: YOU WIN
        print('You WIN !!!')
        
    elif ai == 0 and you == -1: # ai = gun + you = water: YOU WIN 
        print('You WIN !!!')  
        
    elif ai == -1 and you == 0: # ai = water + you = gun: YOU LOSE 
        print('You LOSE !!!')
        
    elif ai == 0 and you == 1: # ai = gun + you = snake: YOU LOSE 
        print('You LOSE !!!')  
        
    else:
        print('something went wrong')   
        