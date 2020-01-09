#!/usr/bin/python
#Coded By DKVIZOWNA

import os

try:
    from colorama import *
except:
    exit()
try:
    import requests
except:
    exit()

os.system('clear||cls')


name = raw_input(Fore.GREEN + Style.BRIGHT + 'Nome : ' + Fore.RESET + Style.RESET_ALL)
print ''

with open('sites.txt', 'r') as pwnd:
    test = site.readlines()
    for es in test:
        req = requests.post("https://mirror-h.org/site-send", data={'attacker': name, 'web site url '})
        ware = 'ERROR'
        if ware in req.text:
            print (Fore.GREEN + Style.BRIGHT + 'Domain Failed Not Sent On Server: ' + es + Fore.RESET + Style.RESET_ALL)
        else:
            print (Fore.GREEN + Style.BRIGHT + 'Successfully domain name added to database. : ' + es + Fore.RESET + Style.RESET_ALL)