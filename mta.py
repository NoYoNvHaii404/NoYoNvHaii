import os
os.system('clear')

import os
os.system("lolcat banner.py")
os.system("python x.py")
print("\n")
os.system("lolcat 01.py")





import os
import json
import requests
from requests.structures import CaseInsensitiveDict

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
# Bold High Intensty


# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
# Bold High Intensty
import json
import requests
from requests.structures import CaseInsensitiveDict
url="https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getMatchbyNickname&nickname=BLooDyLoVeR"


import colorama,time,sys
from time import sleep
from colorama import init, Fore, Back,         Style

words = bicyan+"\n[♦] MATCH AGAIN: \n"  

   
for char in words:
            
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
time.sleep(3.0)            
headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["x-api-key"] = "bb4a666f9051c3bd37a6ad07a2e9e440"

try:
    resp = requests.get(url, headers=headers)
    
except:
    print(bired+"\n\n\t Use Vpn")


allShout=resp.json()["data"] 
for i in range(len(allShout)): 			
    shout=bigreen+"\n[>] NUMBER\t:\t"+bicyan+resp.json()["data"][i]["msisdn"]+bigreen+"\n[>] NICKNAME\t:\t"+bicyan+resp.json()["data"][i]["nickname"]+bigreen+"\n[>] GENDER\t:\t"+bicyan+resp.json()["data"][i]["gender"]+bigreen+"\n[>] BIRTHDAY\t:\t"+bicyan+resp.json()["data"][i]["birthday"]+bigreen+"\n[>] NAME\t:\t"+bicyan+resp.json()["data"][i]["timestamp"]+bigreen+"\n[>] SHOUT\t:\t"+bicyan+resp.json()["data"][i]["mlstatus"]+"\n" 			
    words = biyellow+shout

   
    for char in words:
            
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)

      

xn=str(input(bigreen+" \n\tPress"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')    