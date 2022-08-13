# XMPP Client

## Goals
- Use well-established, open protocol standards
- Recognize the underlying principles of asynchronous programming needed to satisfy network development requirements.

## Features
##### Administration
- [x] Register a new account
- [x] Log in
- [x] Log out
- [x] Delete account
##### Comunication
- [x] Show all users/contacts and their status
- [x] Add user to roster
- [x] Show contact details
- [x] Send messages
- [x] Receive messages
- [x] Define presence message
- [x] Send/Recieve notifications
- [ ] Send/Recieve files

## Requirements
The tools used for development and use were:
```sh
Python 3.7+
Slixmpp
aioconsole
getpass
pandas
tabulate
```

You can install them by running
```sh
pip3.7 install slixmpp aioconsole getpass pandas tabulate
```

## Author
Roberto Castillo

## References 
Slixmpp. Retrieved from https://slixmpp.readthedocs.io/en/latest/
Python 3 Library Reference. Retrieved from https://docs.python.org/3/library/logging.html
XMPP. XEP-0054 vcard-temp. Retrieved from https://xmpp.org/extensions/xep-0054.html