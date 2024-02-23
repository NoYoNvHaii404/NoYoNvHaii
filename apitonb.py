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


a=str(input(bicyan+"[>] Enter Api Key: "+biyellow))

url="https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getNickname&msisdn=8801860852031"

import colorama,time,sys
from time import sleep
from colorama import init, Fore, Back,         Style

words = bipurple+"\n\n[♦] Circle ID From This Api Key: \n"  

   
for char in words:
            
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["x-api-key"] = a
try:
    
    resp = requests.get(url, headers=headers)

except:
    print(bired+"\n\n\t[!] Use Vpn")
    
if resp.json()["rdesc"]=="Unauthorized access":
                print(bired+"\n[!] Enter Vaild ID")
                      
else:
                print(bigreen+"\n[>] CIRCLE ID\t:\t"+bicyan+resp.json()["data"]["nickname"]+"\n")                        
            

xn=str(input(bigreen+" \n\tPress"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')