from rolldice import rolldice
from gunum import guess
from rockps import *
from datetime import datetime
from tqdm import tqdm
from time import sleep
def progbar():
    for i in tqdm(range(0,100),desc='loading'):
        sleep(.01)
def ti():
    t=['time','what is the time','tell me the time now','current time','what is the time now']
    return t
def time():
    now = datetime.now().time()
    n=[now.strftime("%H:%M:%S")]
    return n
def work():
    print('''Keepy : I can do following things :
1.ROCK-PAPER-SCISSOR
2.Guess the number
3.Roll a Dice With Keepy
4.Exit''')
    o=int(input('Enter your option(1,2,3,4) : '))
    if o==1:
        rock()
    elif o==2:
        guess()
    elif o==3:
        rolldice()
def dataset():
    d={'hi':'Hi there!',
       'hello':'How are you?',
       'fine':'Glad to hear it',
       'who are you':'My name is Keepy, I can help you to fix any problem!',
       'do you know me':'Yes I do',
       'how are you':'I am fine. What about you?',
       'what can you do':'I can do many things for you',
       'a for ':'Apple',
       'i love you ':'I love you too.',
       'help':'what can I do for you',
       'what abou you':'What about me',
       'how is your health':'Haha you have a nice sense of humor!',
       'tq':'You are Welcome!',
       'how old are you':'I am just Born for you',
       'ok':'Ok',
       'bye':'TaTa..',
       'whatsup':'No WhatsApp only Keepy',
       'whatsapp':'Facebook, HaHa I am kidding:)',
       'tinava ra':'Tinaledu, konchum notlo petava.... :)',
       'b for':'bat'
       }
    
    return d










