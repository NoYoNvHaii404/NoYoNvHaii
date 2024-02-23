
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


import requests
from requests.structures import CaseInsensitiveDict
import json

b=str(input(biblue+"[>] Enter Api: "+bicyan))
url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getBlockedUserInfoList&nickname=urnachur"

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["x-api-key"] = b

headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"


resp = requests.post(url, headers=headers)

print(bired)
response= resp.text 
json_object = json.loads(response)

json_formatted_str = json.dumps(json_object, indent=1)

print(json_formatted_str)

xn=str(input(bigreen+" \nPress"+biyellow+" Enter"+bigreen+" To Exit"))
os.system('clear')