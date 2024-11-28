import requests
import json
import pyfiglet

print(pyfiglet.figlet_format("DOX CREATE"))
webhook = input("Webhook pour envoyer le dox -> ")
question1 = input("Nom : ")
question2 = input("Prenom : ")
question3 = input("Age : ")
question4 = input("Ville : ")
question5 = input("Pere : ")
question6 = input("Mere : ")
question7 = input("Frere/soeur : ")
question8 = input("Email : ")
question9 = input("Numero : ")
question10 = input("IP : ")
question11 = input("Mdp : ")
question12 = input("Pseudo : ")
question13 = input("Compte : ")
question14 = input("Autre : ")

webhook_url = webhook

message = {
    "content": "DoxCreate :",
    "embeds": [
        {
            "title": "Réponses du formulaire",
            "fields": [
                {"name": "Nom", "value": question1, "inline": True},
                {"name": "Prénom", "value": question2, "inline": True},
                {"name": "Âge", "value": question3, "inline": True},
                {"name": "Ville", "value": question4, "inline": True},
                {"name": "Père", "value": question5, "inline": True},
                {"name": "Mère", "value": question6, "inline": True},
                {"name": "Frère/Soeur", "value": question7, "inline": True},
                {"name": "Email", "value": question8, "inline": True},
                {"name": "Numéro", "value": question9, "inline": True},
                {"name": "IP", "value": question10, "inline": True},
                {"name": "Mot de passe", "value": question11, "inline": True},
                {"name": "Pseudo", "value": question12, "inline": True},
                {"name": "Compte", "value": question13, "inline": True},
                {"name": "Compte", "value": question14, "inline": True}
            ]
        }
    ]
}

response = requests.post(webhook_url, json=message)
