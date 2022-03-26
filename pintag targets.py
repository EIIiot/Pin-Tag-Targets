from tkinter.font import BOLD
from colorama import Fore, Style
import random
import time

BOLD = "\033[1m"
global name
global targets
global assigned

name = ["Name0", "Name1", "Name2", "Name3", "Name4", "Name5", "Name6", "Name7", "Name8", "Name9"]
targets = ["", "", "", "", "", "", "", "", "", ""]
assigned = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
def start():
   
   print(Fore.LIGHTBLUE_EX + BOLD +  "Welcome to Pintag!" + Style.RESET_ALL)
   GNT = input(Fore.RED + BOLD + "To generate new teams please enter (GNT)\n" + Style.RESET_ALL)
   if GNT == "GNT" or GNT == "gnt":
      time.sleep(0.5)
      print(Fore.RED +"⚙️ Processing ⚙️" + Style.RESET_ALL)
      time.sleep(0.5)
      loop()
      
   else:
      print(Fore.RED + BOLD + "Sorry I did not get that, please try again" + Style.RESET_ALL)
      start()

def loop():
   print(Fore.CYAN + BOLD + "----------------------" + Style.RESET_ALL) 
   print(Fore.RED + BOLD + "Name\t |\tTarget" + "\n" +  Style.RESET_ALL)
   for i in range(9):
      x = random.randint(0,9)
      if name[x] == name[i]:
         assigned[i] = "N"
         loop()
      print(Fore.MAGENTA + BOLD + name[i] + "\t" + Style.RESET_ALL + Fore.RED + " | " + Style.RESET_ALL + "\t" + Fore.MAGENTA + name[x] + "\n" + Fore.RED + "\t | " + Style.RESET_ALL)
      targets[i] = name[x]
      assigned[i] = "Y"
start()
print(assigned)
print(targets)
#1. Make a list of players
#2. Cycle through the list and assign each one a random target
#3. You generate a random number that is not you or the person that has you, only get one person