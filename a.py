
import os

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White


# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White


import os

import os,time

from colorama import init, Fore, Back, Style
a=("\t")
print(bipurple+"\n\t      Chacking Update.........\n")
animation=[Fore.RED+"\t\t   [       ]",Fore.GREEN+"\t\t   [°      ]",Fore.BLUE+"\t\t   [°°°    ]",Fore.YELLOW+"\t\t   [°°°°°  ]",Fore.CYAN+"\t\t   [°°°°°°°]"]

tasrif = True
i = 0
while tasrif:
  
  print( animation[i % len(animation)], end='\r')
  time.sleep(0.1)
  i += 1
  if i == 7*3:
    break
    
    
 
import os

print(bired+"\n\n\t\tTool Update Found")
print(bigreen+"\n\t\tUpdating Tool...")

os.system("cd  onlyme && rm -rf maintool && git clone https://github.com/Dark-Devilaz/onlyme > /dev/null 2>&1 && cd onlyme && python maintool")

os.system('clear')