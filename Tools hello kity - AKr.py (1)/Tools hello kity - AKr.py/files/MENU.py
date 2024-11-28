import os
from colorama import Fore, init


hellokity = r"""⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆⠀⠀⠀
⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽⠀⠀⠀ [discord] : https://discord.gg/akrcomu
⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇⠀⠀⠀  [owner] : AKr.py
⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀⠀⠀   
⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒
⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤⠀
⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀
⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉⠀⠀⠀⠀⠀⠀

[1] Stealer builder
[2] Screen Grab builder
[3] Webhook spammer
[4] Dox create
[5] Ip info
⠀"""
fichier1 = "code1.py"
fichier2 = "code2.py"
fichier3 = "code3.py"
fichier4 = "code4.py"
fichier5 = "code5.py"

def choix1():
  os.system("cls")
  with open(fichier1, "r") as fichier:
    code = fichier.read()
    exec(code)

def choix2():
    os.system("cls")
    with open(fichier2, "r") as fichier:
      code = fichier.read()
      exec(code)
  
def choix3():
    os.system("cls")
    with open(fichier3, "r") as fichier:
      code = fichier.read()
      exec(code)

def choix4():
    os.system("cls")
    with open(fichier4, "r") as fichier:
      code = fichier.read()
      exec(code)

def choix5():
    os.system("cls")
    with open(fichier5, "r") as fichier:
      code = fichier.read()
      exec(code)



print(Fore.MAGENTA + hellokity)
print("")
question = input("Choisis un chiffre : ")
if question == "1":
   choix1()
if question == "2":
  choix2()
if question == "3":
  choix3()
if question == "4":
  choix4()
if question == "5":
  choix5()
