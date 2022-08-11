import getpass
from client import Client
import logging

debugging = False

if __name__ == '__main__':
    if debugging:

        useLogin = logging.getLogger()
        useLogin.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        setting_logger_formatlogs = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        console_handler.setFormatter(setting_logger_formatlogs)
        useLogin.addHandler(console_handler)

    mainMenu = 0
    while mainMenu != 3:
        try:
            mainMenu = int(input("""

Choose the number of the option you want to do:
1. Register 
2. Login
3. Exit

>"""))
            if(mainMenu == 1):
                jid = str(input("Email: "))
                password = str(getpass.getpass("Password: "))
                xmpp = Client(jid, password, login=False)         
                xmpp.connect()
                xmpp.process(forever=False)

            elif(mainMenu == 2):
                jid = str(input("Email: "))
                password = str(getpass.getpass("Password: "))
                xmpp = Client(jid, password)
                xmpp.connect()
                xmpp.process(forever=False)
                if(not xmpp.logged):
                    print("Can't login, plese check your email")	
                    xmpp.disconnect()

            elif(mainMenu == 3):
                print("You are always welcome !")
            else:
                print("Choose a valid option")
        except: 
            print("Choose a valid option")