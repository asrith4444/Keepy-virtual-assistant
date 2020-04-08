from data import *
import shelve
#"\u26A0"
def head():
    progbar()
    d = shelve.open("dictionary")
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
    t=ti()
    u=input('Keepy : Enter your nickname : ')
    print('Keepy : Hello %s.'%(u))
    while (True):
        n=input('%s : '%(u)).lower()
        if n=='what can you do' or n=='games' or n=='i want to play a game':
            work()
        elif n=='what is my name':
            print('Keepy your name is : ',u)
        elif n in t:
            print('The current time is : ',str(time()))
        elif n in d:
            print('Keepy : ',d[n])
        elif n=='quit':
            break
        elif n=='':
            print('Keepy : You entered Nothing.')
        else:
            print('It seems like I am unable to Answer you.')
            print('You Know What, you can train me.. Sounds Good right!')
            choice=input("\u26A0"+'Do you want to Train me enter Yes/No : ').lower()
            if choice=='yes' or choice=='y':
                key=input('Enter Keepy Unanswered Question : ').lower()
                val=input('Enter the Answer you expect from the Keepy for this '+key+' question : ')
                d[key]=val
                print('Keepy is Updated.')
            continue

            


