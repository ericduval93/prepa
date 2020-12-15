#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# Create dict
mydic = {}

# Create et/ou Init dict
mydic = {"voiture": "véhicule à quatre roues", "velo": "véhicule à deux roues"}

# Display one item
print(mydic['voiture'])

# Add one item
mydic["tricycle"] = "véhicule à trois roues"

# Display all dict
print(mydic)

# Type dict
print(type(mydic))

# Read only keys
for i in mydic.keys():
    print("key = {}".format(i))

# Read only values
for i in mydic.values():
    print("values = {}".format(i))

# Read all entry
for i in mydic.items():
    print("Key + value = {}".format(i))

for cle, valeur in mydic.items():
    print("l'élément de clé", cle, "vaut", valeur)

# Use tuple as key
echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# ... Seconde ligne des blancs

print(echiquier)
print(echiquier['a',1])

# del / pop
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
print("Before del: {}".format(placard))
del placard["chemise"]
print("After del: {}".format(placard))

placard = {"chemise":3, "pantalon":6, "tee shirt":7}
print("Before pop: {}".format(placard))
foo = placard.pop("chemise")
print("After pop: {} et index return = {}".format(placard,foo))

# Dict de fonction
def fete():
    print("C'est la fête.")
def oiseau():
    print("Fais comme l'oiseau...")

fonctions = {}
fonctions["fete"] = fete # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"]()

exit(0)
