from aioconsole import ainput

class MessagesManager:

    async def dispatchMessage(self):
    
        foreign_contact = str(await ainput("Email of the user you want to send a message: "))
        
        option = 0
        try:
            option = int(await ainput(""" 

Choose the number of the option you want to do:
1. Send messsage
2. Send file

>"""))
        except: 
            print("Choose a valid option")
        
        if option == 1:
            print("Message:")
            message = str(await ainput(">")) 
            
            self.send_message(mto=foreign_contact,
                            mbody=message,
                            mtype='chat')

        elif option == 2:
            filename = str(await ainput("Source of the file you want to send: "))
            domain = str(await ainput("Domain to upload your file: "))
            
            try:
                print('Sending file...')
                url = await self['xep_0363'].upload_file(
                    filename, domain=domain, timeout=10
                )
                html = (
                    f'<body xmlns="http://www.w3.org/1999/xhtml">'
                    f'<a href="{url}">{url}</a></body>'
                )
                message = self.make_message(mto=foreign_contact, mbody=url, mhtml=html)
                message['oob']['url'] = message
                message.send() 
                print('File succesfully sent')
            except:
                print('Can not send file, please try again') 
               
    async def determineGroupMessage(self):

        self.group_email = str(await ainput("Group name: "))
      
        self.add_event_handler("muc::%s::got_online" % self.group_email, self.itsOnlineInGroup)

        self.plugin['xep_0045'].join_muc(self.group_email, self.nickName)

        option = 0
        try:
            option = int(await ainput(""" 

Choose the number of the option you want to do:
1. Send messsage
2. Send file

>"""))
        except: 
            print("Choose a valid option")
        
        if option == 1:
            print("Message:")
            message = str(await ainput(">"))
        
            self.send_message(mto=self.group_email,
                            mbody=message,
                            mtype='groupchat')

        elif option == 2:
            filename = str(await ainput("Source of the file you want to send: "))
            domain = str(await ainput("Domain to upload your file: "))
            
            try:
                print('Sending file...')
                url = await self['xep_0363'].upload_file(
                    filename, domain=domain, timeout=10
                )
                html = (
                    f'<body xmlns="http://www.w3.org/1999/xhtml">'
                    f'<a href="{url}">{url}</a></body>'
                )
                message = self.make_message(mto=self.group_email, mbody=url, mhtml=html, mtype='groupchat')
                message['oob']['url'] = message
                message.send() 
                print('File succesfully sent')
            except:
                print('Can not send file, please try again') 
    
    async def definePresenceMessage(self):

        self.use_status = str(await ainput("Status: "))
        
        self.send_presence(pstatus=self.use_status, pnick=self.nickName)
        await self.get_roster()

