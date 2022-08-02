import slixmpp
from slixmpp.xmlstream.asyncio import asyncio

class Client(slixmpp.ClientXMPP):
    
    def __init__(self, jid, password, login = True):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.is_logged = False
        self.nickName = ''
        self.use_recieved = set()
        self.use_recieved_presenses = asyncio.Event()

        if not login:
            self.add_event_handler("register", self.register)
        

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
