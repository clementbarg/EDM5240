# coding:utf-8

# Tu as trouvé des données très originales qui pourront te servir pour le travail final.

import csv
import datetime
import json
import requests 

# url = "http://data.culture.fr/entrepot/MERIMEE/merimee-MH.json" # Voir ligne suivante pour savoir pourquoi j'ai mis cette ligne-ci en commentaire
donnees = "patrimoine.json" # Au lieu que le script aille chercher les données à chaque fois, je les ai téléchargées et le script les consulte localement
fichier = "batiments.csv"

entetes = {
    "User-Agent":"Clément Bargain - Requête envoyée dans le cadre d'un cours de journalisme de données à l'UQAM",
    "From":"clement_bargain@hotmail.fr"
}

# req = requests.get(url, headers=entetes) # Comme je ne vais plus chercher les données sur le web à chaque fois que j'exécute ce script, je n'ai plus besoin de cette ligne
# Voici la façon la plus optimale de lire un fichier json local; ça va beaucoup plus vite :)
data = open(donnees).read()
batiments = json.loads(data)

# Excellente exploration des données ci-dessous

# idf = 0

# for batiment in batiments:
#     if len(batiment) == 14:
#         if batiment["REG"] == "Ile-de-France":
#             idf = idf+1

# etat = 0
# for batiment in batiments:
#     if len(batiment) == 14:
#         if batiment["STAT"] == "propri\u00e9t\u00e9 de l'Etat": 
#             etat = etat+1

# montreuil = 0

# for batiment in batiments:
#     if len(batiment) == 14:
#         if batiment["COM"] == "Montreuil":
#             montreuil = montreuil+1

# merneuil = 0
# for batiment in batiments:
#     if len(batiment) == 14:
#         if batiment["COM"] == "Verneuil-sur-Seine":
#             verneuil = verneuil+1

for batiment in batiments:
    if len(batiment) == 14:
        bat = []
        bat.append(batiment["ADRS"]) #Voici la syntaxe pour obtenir l'adresse
        bat.append(batiment["COM"])
        bat.append(batiment["DPT"])
        bat.append(batiment["TICO"])

# Avec la variable SCLE, j'effectue un traitement spécialqui me permet de savoir combien de siècles ou de périodes différentes sont inscrites dans cette catégorie
        bat.append(batiment["SCLE"])
        if ";" in batiment["SCLE"]:
            siecle = batiment["SCLE"].split(";")
            # print(batiment["SCLE"],len(siecle))
            bat.append(len(siecle))
        elif batiment["SCLE"] == "":
            bat.append(0)
            # print(batiment["SCLE"],"0")
        else:
            bat.append(1)
            # print(batiment["SCLE"],"1")

# Toujours avec la variable SCLE, on vérifier si chaque lieu peut être situé dans différentes grandes périodes de l'histoire
# D'abord, la Préhistoire
        if "Préhistoire" in batiment["SCLE"]:
            bat.append("Préhistoire")
        elif "Protohistoire" in batiment["SCLE"]:
            bat.append("Préhistoire")
        elif "Paléolithique" in batiment["SCLE"]:
            bat.append("Préhistoire")
        elif "Néolithique" in batiment["SCLE"]:
            bat.append("Préhistoire")
        elif "Chalcolithique" in batiment["SCLE"]:
            bat.append("Préhistoire")
        elif "Mésolithique" in batiment["SCLE"]:
            bat.append("Préhistoire")
        elif "du fer" in batiment["SCLE"]:
            bat.append("Préhistoire")
        elif "du bronze" in batiment["SCLE"]:
            bat.append("Préhistoire")
        else:
            bat.append("")
# Ensuite l'Antiquité
        if "Antiquité" in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "Gallo-romain" in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "Haut-Empire" in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "Bas-Empire" in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "JC" in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "1er siècle" in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "2e siècle" in batiment["SCLE"] and "12e siècle" not in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "3e siècle" in batiment["SCLE"] and "13e siècle" not in batiment["SCLE"]:
            bat.append("Antiquité")
        elif "4e siècle" in batiment["SCLE"] and "14e siècle" not in batiment["SCLE"]:
            bat.append("Antiquité")
        else:
            bat.append("")
# Ensuite le Moyen-Âge
        if "Moyen Age" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "Moyen-Age" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "5e siècle" in batiment["SCLE"] and "15e siècle" not in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "6e siècle" in batiment["SCLE"] and "16e siècle" not in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "7e siècle" in batiment["SCLE"] and "17e siècle" not in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "8e siècle" in batiment["SCLE"] and "18e siècle" not in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "9e siècle" in batiment["SCLE"] and "19e siècle" not in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "10e siècle" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "11e siècle" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "12e siècle" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "13e siècle" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "14e siècle" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        elif "15e siècle" in batiment["SCLE"]:
            bat.append("Moyen Âge")
        else:
            bat.append("")
# Ensuite, je mettrais chaque siècle suivant dans une catégorie distincte
        if "16e siècle" in batiment["SCLE"]:
            bat.append("16e siècle")
        elif "16è siècle" in batiment["SCLE"]:
            bat.append("16e siècle")
        else:
            bat.append("")
        if "17e siècle" in batiment["SCLE"]:
            bat.append("17e siècle")
        else:
            bat.append("")
        if "18e siècle" in batiment["SCLE"]:
            bat.append("18e siècle")
        else:
            bat.append("")
        if "19e siècle" in batiment["SCLE"]:
            bat.append("19e siècle")
        else:
            bat.append("")
        if "20e siècle" in batiment["SCLE"]:
            bat.append("20e siècle")
        else:
            bat.append("")

        bat.append(batiment["PPRO"])
        bat.append(batiment["STAT"])
        bat.append(batiment["DPRO"])

# Un dernier traitement spécial, pour la variable DPRO, cette fois, qui contient la date à laquelle le bâtiment a été iscrit ou classé aux MH 
        if " : " in batiment["DPRO"]:
            dpro = batiment["DPRO"].split(":")
            premiereDate = dpro[0]
            annee = premiereDate[:4]
            # print(annee)
            bat.append(annee) # Cette nouvelle variable nous donne l'année de première inscription aux MH, variable qu'il pourrait être intéressante à placer sur un graphique à ligne ou un histogramme
        else:
            bat.append("")

        bat.append(batiment["REF"])

    print(bat)

    monsieur_ouille = open(fichier,"a")
    montmirail = csv.writer(monsieur_ouille)
    montmirail.writerow(bat)

# Dans le fichier CSV résultant, j'ai ajouté des entêtes de colonnes