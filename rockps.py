import random
from playsound import playsound
from tqdm import tqdm
from time import sleep
def rock():
    for i in tqdm(range(0,100),desc='Loading'):
            sleep(.01)
    print('-------------------Welcome to (Rock-Paper-Scissor) Game--------------------')
    print('''Things to know :
You are going to play with Keepy.
The thing is you have to fix
your option first.
Winning Criteria :
Rock vs Rock     :If result is same then, Both are Winners
Rock vs Paper    :Paper is Winner
Rock vs Scissor  :Rock is Winner
Paper vs Scissor :Scissor is Winner

For easy Gameplay, Select your option as a number :
1.Rock
2.Paper
3.scissor
''')
    k=0
    uc=0
    n=int(input('Enter how many times you want to Play with Keepy : '))
    for i in range(0,n):
        inp=int(input('''Enter your option : '''))
        a=random.randint(1,3)
        playsound('rockpa.MP3')
        if a==inp:
            if a==1:
                print('Keepy : Rock \nYou : Rock')
                print('The Match is Tied')
                #k=k+1
                #uc=uc+1
            elif a==2:
                print('Keepy : Paper \nYou : Paper')
                print('The Match is Tied')
                #k=k+1
                #uc=uc+1
            elif a==3:
                print('Keepy : Scissor \nYou : Scissor')
                print('The Match is Tied')
                #k=k+1
                #uc=uc+1
        elif a==2 and inp==1:
            print('Keepy : Paper \nYou : Rock')
            print('Keepy is WINNER')
            k=k+1
        elif a==2 and inp==3:
            print('Keepy : Paper \nYou : Scissor')
            print('You are the  WINNER')
            uc=uc+1
        elif a==3 and inp==1:
            print('Keepy : Scissor \nYou : Rock')
            print('You are the  WINNER')
            uc=uc+1
        elif a==3 and inp==2:
            print('Keepy : Scissor \nYou : Paper')
            print('Keepy is WINNER')
            k=k+1

    print()
    print('In %d Match Series :'%(n))
    print('Keepy won : %d times.\n''You won : %d times.'%(k,uc))
    if k<uc:
        print('You are The WINNER! OF %d MATCH SERIES, CONGRATULATIONS'%(n))
    elif k>uc:
        print('Keepy is The WINNER! OF %d MATCH SERIES, CONGRATULATIONS'%(n))
    else:
        print('Both are the Winners')

    print()
    q=input('Will you play again? (y/n): ') 
    if q=='y' or q=='Y':
        rock()











        
        
        
        
