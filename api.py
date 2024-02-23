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
biehite="\033[1;97m"      # White
import colorama,time,sys
from time import sleep
from colorama import init, Fore, Back,         Style
import requests 
from requests.structures import CaseInsensitiveDict 
import json
#Otp requests
number=str(input(biblue+"[>] Enter Number: "+biyellow)) 
url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=21799&app_version=78&msisdn=88"+number  
headers = CaseInsensitiveDict() 
headers["x-app-key"]="000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg" 
headers["User-Agent"] = "gzip"
num=number
headers["Content-Type"] = "application/x-www-form-urlencoded"    
print(bired)
resp = requests.post(url, headers=headers) 
#Chacking Connections 
if resp.json()["rdesc"]=="App installation not allowed because user account is strictly SMS ONLY.":
    words = bired+"\n\t[×] Make Sure Capp On"
    for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
    time.sleep(3)            
else:
    words = bigreen+" "
    for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
    time.sleep(0.1)
#Auto Shout...    
if resp.json()["rdesc"]=="OK":
    words = bigreen+"\n\t[√] Otp Has Been Sent Seccesful....\n"  
    for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
    c=str(input(bicyan+"\n\n[>] Enter Otp: "+biyellow)) 
    url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=validateOTC&pin=123456&otc="+c+"&app_version=79&msisdn=88"+num
    try:
    	resp = requests.get(url, headers=headers)
    except:
    	print(bired+"use vpn")
    if resp.json()["rdesc"] == "Not found":
    	print("\n\n\t [×] User Not Found")
#Get Api key...
    else:	
        try:
            words = bigreen+"\n[>] CIRCLE ID \t : \t"+bicyan+resp.json()["data"]["nickname"]+bigreen+"\n[>] X-API-KEY \t : \t"+bicyan+resp.json()["data"]["mkey"]+bigreen+"\n[>] SMS PIN  \t : \t"+bicyan+resp.json()["data"]["sms_pin"]
            for char in words:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.05)
            url="https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&msisdn=8801875409158&message=You Have Got Your Api From RisHaD...!! &retry=false"
            headers9 = CaseInsensitiveDict() 
            headers9["x-app-key"]="000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg" 
            headers9["x-api-key"]=resp.json()["data"]["mkey"]
            x = requests.post(url, headers=headers9)  
        except:
    	    words = bired+"\n\t [×] Something Went Wrong...Try Again/n"
        for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
else:
        words = bired+"\n\t[×] Otp Failed To Sent\n"  
        for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  
xn=str(input(bigreen+" \n\n\tPress"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')