#coding:utf-8

# Il faut importer des modules pour communiquer avec le web
import csv
import datetime
import json
import requests 

# Pour ce script, j'utilise un API directement disponible sur le site du Ministète de la Culture en France
# API = INTERFACE DE PROGRAMMATION D'APPLICATION
# Création d'une variable URL
url = "http://data.culture.fr/entrepot/MERIMEE/merimee-MH.json"
fichier = "batiments.csv"

# Je me présente
entetes = {
    "User-Agent":"Clément Bargain - Requête envoyée dans le cadre d'un cours de journalisme de données à l'UQAM",
    "From":"clement_bargain@hotmail.fr"
}

# J'envoie ma requête au Ministère de la Culture
req = requests.get(url, headers=entetes)

#print(req)

# Je cherche à savoir combien de batiments sont classés au patrimoine historique
batiments = req.json()
#print(batiment)

# Je cherche à savoir combien il y a de batiments classés au patrimoine historique en Ile-de-France
idf = 0

for batiment in batiments:
#    print(len(batiment))
    if len(batiment) == 14:
#        print(batiment["REG"])
        if batiment["REG"] == "Ile-de-France":
            idf = idf+1
            
#print(idf)
# Je sais maintenant qu'il y a 3842 batiments classés en Ile de France

# Je cherche à savoir combien de batiments classés appartiennent à l'État Français
etat = 0
for batiment in batiments:
#    print(len(batiment))
    if len(batiment) == 14:
#        print(batiment["REG"])
        if batiment["STAT"] == "propri\u00e9t\u00e9 de l'Etat": 
            # Je reprend l'écriture qui est dans l'API 
            etat = etat+1
#print(etat)
# Je sais maintenant qu'il y a 1419 batiments classés qui appartiennent à l'État

#Je cherche à savoir combien il y a de batiments classés dans la commune où je suis né: Montreuil
Montreuil = 0

for batiment in batiments:
#    print(len(batiment))
    if len(batiment) == 14:
#        print(batiment["REG"])
        if batiment["COM"] == "Montreuil":
            Montreuil = Montreuil+1
#print(Montreuil)
#Je sais maintenant qu'il y a 22 batiments classés à Montreuil

# Je cherche à savoir combien de batiments sont classés dans la ville où j'étais au lycée
Verneuil = 0
for batiment in batiments:
#    print(len(batiment))
    if len(batiment) == 14:
#        print(batiment["REG"])
        if batiment["COM"] == "Verneuil-sur-Seine":
            Verneuil = Verneuil+1
#print(Verneuil)
# Je sais maintenant qu'il y a 2 batiments classés à Verneuil-sur-Seine

# J'ai cherché à établir une liste des monuments classés avec les informations qui m'intéressent, mais je n'y suis pas parvenu 
for batiment in batiments:
#    print(len(batiment))
    if len(batiment) == 14:
        bat = []
        bat.append(REG)
        bat.append(DPT)
        bat.append(COM)
        bat.append(ADRS)
print(bat)

# Je n'arrive vraiment pas à être autonome avec tous ces outils qui sont pour moi du chinois et ce n'est vraiment pas de la mauvaise volonté ! Je comprends les exercices lorsqu'on les effectue ensemble dans le cours, mais je ne parviens pas à travailler tout seul... J'ai passé la soirée à chercher des combinaisons, en vain!


