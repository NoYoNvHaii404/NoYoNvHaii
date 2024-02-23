

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


import requests
from requests.structures import CaseInsensitiveDict

x=str(input(bicyan+"[>] Enter Api Key: "+biyellow))
base = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?'
url = base + 'op=getFollowerInfoList'


headers = CaseInsensitiveDict() 
headers["x-app-key"]="000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["x-api-key"]=x
resp = requests.post(url, headers=headers)


resp = requests.post(url, headers=headers)
if resp.json()["rdesc"] == "OK":
    
        print(biblue+"[>] Total Follower:"+bigreen+resp.json()["data"]["total"]+" \n")
        y= resp.json()["data"]["follower"]
    	
folNicks = []
bool = input(bigreen+"\n\n\t[!]"+bired+" If You Wonna To Clear Follower List Type Y"+biyellow+"\n")    	

urlx="https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&msisdn=8801875409158&message=Your Circle  Follower List Is Cleaning By Using RisHaD....!! &retry=false"

resp5 = requests.post(urlx, headers=headers)  

    	    
 

if bool:
    for user in y:
        print(bipurple+"[>]"+bigreen+" CIRCLE ID\t:\t " +bicyan+ user["nickname"])
        folNicks.append(user["nickname"])
    try:
        for nickname in folNicks:
            url = base+'op=blockUser&nickname='+nickname
            resp = requests.post(url, headers=headers)
            print(bired+resp.text)
    except:
        print('Error!')
        
        
         
xn=str(input(bigreen+" \n\n\tPress"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')                  
        
        