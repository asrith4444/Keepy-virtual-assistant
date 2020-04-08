from plays import *
from signnow import signnow
from data import *
import sqlite3
d=sqlite3.connect("emp.db")
c=d.cursor()
def signup():
    signnow()
    head()
def login():
    print('---------------------LogIn Now---------------------')
    u=input('User name : ').lower()
    p=input('Password : ').lower()
    c.execute('''select * from sigdb1''')
    de=c.fetchall()
    #print(de)
    for i in de:
        if i[2]==u:
            if i[3]==p:
                print('You are Successfully Logged into your Keepy Account')
                print('---------------------------------------------------')
                head()
            else:
                print('The Entered Username or Password is Incorrect. \n1.Please Enter a valid Username or Password. \n2.If you are not SignUp then do it Now!')
                op=int(input("Enter your option(1/2) : "))
                if op==1:
                    login()
                elif op==2:
                    signnow()
                
print('''
********************************************************************************
                *     *    *******    *******    *******    *       *
                *    *     *          *          *     *     *     *
                *   *      *          *          *     *      *   *
                *  *       *          *          *     *       * *
                * *        *******    *******    *******        *
                * *        *          *          *              *
                *  *       *          *          *              *
                *   *      *          *          *              *
                *    *     *******    *******    *              *
********************************************************************************
-----------------------------------(Assistant)----------------------------------
             ***Are you new to Keepy? no problem SignUp Now***
                    ***Already Signed in? LogIn Now***
''')
def main():
    ch=int(input('Enter 1 to SignUp \nEnter 2 to LogIn \nEnter 3 to exit \n : '))
    if ch==1:
        signup()
    elif ch==2:
        login()
    elif ch==121433:
        c.execute('''select * from sigdb1''')
        dbase=c.fetchall()
        print('Hello Admin, Good to see you today!')
        print()
        print('Below is the details of your Users : \n')
        for i in range(len(dbase)):
            print('User Data : ',dbase[i])
        b=int(input('Enter 0 to back : '))
        if b==0:
            main()
        else:
            print('You entered an wrong operation the program exited.')

    else:
        print('You entered an wrong operation the program exited.')
main()



























    
        
    
