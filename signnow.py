from signup import *
from data import *
def signnow():
    print('-----------------SignUp Now-----------------')
    f=input('Enter your First Name : ').lower()
    l=input('Enter your Last Name : ').lower()
    u=input('Enter your User Name : ').lower()
    p=input('Enter your Password : ').lower()
    insert(f,l,u,p)
    d.commit()
    print('You are Successfully Signed in.. \nRedirecting to Main Program')
