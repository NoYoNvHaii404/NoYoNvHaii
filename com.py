

import os
os.system('clear')

import os
os.system("lolcat banner.py")
os.system("python x.py")
print("\n")
os.system("lolcat 01.py")


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



import time

import requests
import json
from requests.structures import CaseInsensitiveDict
a=str(input(bicyan+"\n[>] Enter Api Key:"+biyellow))


url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=78&nickname=coronavirus&action=kom&msgId=84&msisdn=8801860852031&message=Hi..kmn achen.&retry=false&operator=Robi"

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["x-api-key"] = a


for i in range(999999):
    try:
        resp = requests.get(url, headers=headers)
        time.sleep(2)

       
    except:
        print(bired+"\n\t Use Vpn!")    
    if resp.json()["rdesc"]=="Unauthorized access":
                print(bired+"\n\t[!] Enter Vaild ID")
                
                      
    else:
                 print(bigreen+"\n\t[√] Comment Succesfully Submited")                              
        
        
xn=str(input(bigreen+" \n Press"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')
import os
os.system('clear')