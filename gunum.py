import random
from tqdm import tqdm
from time import sleep
def guess():
    for i in tqdm(range(0,100),desc='Loading'):
            sleep(.01)
    print('''----------Welcome to the GUESS A NUMBER Game----------''')
    print('''------------------------------------------------------
In this Game Keepy fix a number and you have
to guess the number. If your guess matches with
Keepy's number then you are the Winner!
------------------------------------------------------
REMEMBER ONLY 5 CHANCES

Enter 'S' to START the Game
            (Or)
Enter 'Q' to QUIT the Game''')
    c=input()
    if c=='s' or c=='S':
        a=random.randint(1,99)
        for i in range(5):
            n=int(input('GUESS the NUMBER in BETWEEN 1 AND 99 : '))
            print()
            print()
            if a==n:
                print('You WON the Game!!!')
                break
            elif n<a:
                print('Your GUESS is Smaller!\n')
                print()
                if 4-i==0:
                    print('You Loose the Game, Better luck next time!')
                    print('The number is : ',a)
                    print()
                    q=input('Will you play again? (y/n): ')
                    if q=='y' or q=='Y':
                        guess()
                else:
                    print('CHANCES LEFT : ',4-i)
            elif n>a:
                print('Your GUESS is Higher!\n')
                if 4-i==0:
                    print('You Loose the Game')
                    print('The number is : ',a)
                    q=input('Will you play again? (y/n): ') 
                    if q=='y' or q=='Y':
                        guess()
                else:
                    print('CHANCES LEFT : ',4-i)

                
    
