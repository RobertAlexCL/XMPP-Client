import getpass
from client import Client
import logging

if __name__ == '__main__':

    mainMenu = 0
    while mainMenu != 3:
        try:
            mainMenu = int(input("""

Choose the number of the option you want to do:
1. Register 
3. Exit

>"""))
            if(mainMenu == 1):
                jid = str(input("Email: "))
                password = str(getpass.getpass("Password: "))
                xmpp = Client(jid, password, login=False)         
                xmpp.connect()
                xmpp.process(forever=False)

            elif(mainMenu == 3):
                print("You are always welcome !")
            else:
                print("Choose a valid option")
        except: 
            print("Choose a valid option")