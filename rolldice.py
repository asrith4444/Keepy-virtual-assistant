#from data import *
from tqdm import tqdm
from time import sleep
import random
from playsound import playsound
def win(a,b):
    if a==b:
        print('You are the Winner!')
    elif a<b:
        print('Keepy wins the Game, Better Luck next time.')
    else:
        print('You are the Winner!')
def rolldice():
    a=0
    while a<1:
        for i in tqdm(range(0,100),desc='Loading'):
            sleep(.01)
        print('--------------Welcome to Rolling a dice-----------')
        c=input('''Do you want to roll the dice 1st-(y/n)\n
Or To Quit the Game Enter "q" : ''')
        if c=='y' or c=='Y':
            print('Rolling the dice for you....')
            playsound('roll.MP3')
            u=random.randint(1,6)
            print('Your value is : ',u)
            print('Rolling the dice for Keepy....')
            playsound('roll.MP3')
            k=random.randint(1,6)
            print('Keepy value is : ',k)
            win(u,k)
            q=input('Will you play again? (y/n) : ')
            if q=='y' or q=='Y':
                a=0
            else:
                a=10
        elif c=='n' or c=='N':
            print('Rolling the dice for Keepy....')
            playsound('roll.MP3')
            k=random.randint(1,6)
            print('Keepy value is : ',k)
            print('Rolling the dice for you....')
            playsound('roll.MP3')
            u=random.randint(1,6)
            print('Your value is : ',u)
            win(u,k)
            q=input('Will you play again? (y/n) : ')
            if q=='y' or q=='Y':
                a=0
            else:
                a=10
        elif c=='q' or c=="Q" :
            a=10

            
            
        
    
