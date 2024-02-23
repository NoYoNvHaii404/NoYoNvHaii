
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
import os
import requests
import json

from requests.structures import CaseInsensitiveDict





b=str(input(bicyan+"\n[>] Enter Api Key: "+biyellow))

url="https://circle.robi.com.bd/mylife/appapi/appcall.php?op=setUserMode&mode=stop"




headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["x-api-key"] = b

try:
	resp = requests.get(url, headers=headers)
except:
	print("use vpn")
if resp.json()["rdesc"]=="Unauthorized access":
                print(bired+"\n[!] Enter Vaild ID")
                      
else:
                print(bigreen+"\n[√] ID Stop Successful") 
                
                    	


xn=str(input(bigreen+" \n\n\tPress"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')                    	    	    	