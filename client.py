import slixmpp
from slixmpp.xmlstream.asyncio import asyncio 
from aioconsole import ainput
from messages_manager import MessagesManager

class Client(slixmpp.ClientXMPP): 
    
    def __init__(self, jid, password, login = True):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.is_logged = False
        self.nickName = ''
        self.use_status = 'Active'
        self.use_recieved = set()
        self.use_recieved_presenses = asyncio.Event()
        self.group_email = ''

        if not login:
            self.add_event_handler("register", self.register)
            self.add_event_handler("session_start", self.start)
            self.add_event_handler("changed_status", self.presensesWaiting)
        
        self.register_plugin('xep_0030') 
        self.register_plugin('xep_0004') 
        self.register_plugin('xep_0066') 
        self.register_plugin('xep_0077') 
        self.register_plugin('xep_0199') 
        self.register_plugin('xep_0045') 
        self.register_plugin('xep_0085') 
        self.register_plugin('xep_0096') 
        self.register_plugin('xep_0059')
        self.register_plugin('xep_0060')
        self.register_plugin('xep_0071')
        self.register_plugin('xep_0128')
        self.register_plugin('xep_0363')

    async def removeUser(self):

        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['remove'] = True

        try:
            await resp.send()
            print("User succesfuly deleted!")
        except:
            print("User may not be deleted, try again")

    async def start(self, event):
        self.send_presence(pstatus=self.use_status)
        await self.get_roster()
        
        self.nickName = str(await ainput("Write a nickname: "))        
        self.is_logged = True
        second_menu = 0
        
        while second_menu != 7 and second_menu != 8:
            try:
                second_menu = int(await ainput(""" 

Choose the number of the option you want to do:

1. Delete my account
2. Send message to a user
3. Send message to a group

>"""))
            except: 
                second_menu = 0
                print("Choose a valid option")                
      
            self.send_presence(pstatus=self.use_status)
            await self.get_roster()
            
            if(second_menu == 1):
                await self.removeUser()

            elif(second_menu == 2):
                await MessagesManager.dispatchMessage(self)
            
            elif(second_menu == 3):
                await MessagesManager.determineGroupMessage(self)
            
            elif(second_menu != 0):
                print("Choose a valid option")
        
        self.disconnect()

    async def register(self, iq):
        note = self.Iq()
        note['type'] = 'set'
        note['register']['username'] = self.boundjid.user
        note['register']['password'] = self.password

        try:
            await note.send()
            print("You have created your account!")
        except:
            print("Something happened creating your account, try changing your email")
            self.disconnect()

    def presensesWaiting(self, pres):

        self.use_recieved.add(pres['from'].bare)
        if len(self.use_recieved) >= len(self.client_roster.keys()):
            self.use_recieved_presenses.set()
        else:
            self.use_recieved_presenses.clear()

    def message(self, note):
        if note['type']  in ('normal', 'chat'):
            print("----------------New Notification----------------------")
            print(f"{note['from'].username}: {note['body']}")
        
        elif note['type'] == 'groupchat':
            print("----------------New Notification----------------------")
            print(f"Grupo ({note['from'].username}): {note['body']}")
        else :
            print(note)
    
    def groupMessage(self, note):
        if(note['mucnick'] != self.nickName and self.nickName in note['body']):
            print(f"Someone mentioned you in a group ({note['from'].username})")

    def itsOnlineInGroup(self, presence):
        if presence['muc']['nick'] != self.nickName:
            print(f"{presence['muc']['nick']} it is online in group ({presence['from'].bare})")

