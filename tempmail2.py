##################################
##Author: r0m305
##Email: r0m305cyb3r@protonmail.com
##Script: tempmail2.py
##Description: Script for accessing temporary emails via the commandline
#################################


import requests
import json
import sys
import optparse
import time
from colorama import *
from termcolor import colored
import os

class Engine:
    def __init__(self):
        self.parser = optparse.OptionParser()
        if len(sys.argv) < 2:
            print(colored("Syntax: python3 tempmail2.py --username=anyusername","red"))
            sys.exit()

        self.parser.add_option("--username", dest = "username", help = "Custom username to use as email e.g r0m305")
        (self.values, self.keys) = self.parser.parse_args()
        self.checkAPI(self.values.username)

    def checkAPI(self, username):
        headers = {"User-agent":"Mozilla/5.1"}
        print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Your temporary email: {Fore.YELLOW}{username}@1secmail.org\n")
        emailList = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain=1secmail.org".format(username), headers = headers)
        emails = json.loads(emailList.text)
        print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Number of emails in your inbox: {Fore.YELLOW}{len(emails)}")
        if len(emails) == 0:
            print(colored("NO EMAILS YET","green"))
        number = len(emails) - 1
        while number >= 0:
            individualEmail = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain=1secmail.org&id={}".format(username,emails[number]['id']), headers = headers)
            mailContent = json.loads(individualEmail.text)
            number-=1
            print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Mail id: {Fore.YELLOW}{mailContent['id']}")
            print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}From: {Fore.YELLOW}{mailContent['from']}")
            print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Date: {Fore.YELLOW}{mailContent['date']}")
            print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Subject: {Fore.YELLOW}{mailContent['subject']}")
            print(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Body: {Fore.YELLOW}{mailContent['textBody']}")
            print("\n\n")

if __name__ == '__main__':
    while True:
        banner = '''
   __                                             _ __
  / /____  ____ ___  ____        ____ ___  ____ _(_) /
 / __/ _ \/ __ `__ \/ __ \______/ __ `__ \/ __ `/ / /
/ /_/  __/ / / / / / /_/ /_____/ / / / / / /_/ / / /
\__/\___/_/ /_/ /_/ .___/     /_/ /_/ /_/\__,_/_/_/
                 /_/                               '''
        print(colored(banner,"green"))
        print(f"{Fore.GREEN}Written By {Fore.BLUE}r0m305{Fore.RESET}")
        print(f"{Fore.GREEN}The program refreshes every 5 seconds to get email updates\n")
        obj = Engine()
        time.sleep(5)
        os.system('clear')
