#!/usr/bin/env python3
import random
import string
import os

def mdp_dmd_user():
    os.system('clear')
    longueur = int(input("Longueur du Mot De Passe: "))
    inclure_symbole = input("Inclure des Symboles ? o/n (Recommandé !)").strip()
    caracteres = string.ascii_letters + string.digits
    if inclure_symbole.lower() == "o":
      caracteres += string.punctuation
    mdp = "".join(random.choice(caracteres) for _ in range (longueur))
    os.system('clear')
    print("Mot De Passe Généré :" , mdp)
    pause_menu()
    

def mdp_gen_16cara():
   os.system('clear')
   caracters = string.ascii_letters + string.digits + string.punctuation
   longueur = 16
   mdp = "".join(random.choice(caracters) for _ in range (longueur))
   os.system('clear')
   print("\n Mot de Passe (16 caractères) :", mdp)
   pause_menu()

def menu():
   while True:
     print("""
_____                                   _   _____                           _             
| ___ \                                 | | |  __ \                         | |            
| |_/ /_ _ ___ _____      _____  _ __ __| | | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|      
                                                                                        
""")
     print("1.Générer Mot de Passe Personnalisé.")
     print("2.Générer un Mot de Passe sécurisé.")
     print("3.Quitter.")
     choix = input(":").strip().lower()
     if choix == "1":
      mdp_dmd_user()
     elif choix == "2":
      mdp_gen_16cara()
     elif choix == "3":
      break
     else:
      print("Choix invalide, Entre 1,2 ou 3 ")

def pause_menu():
  choix = input("\nContinuer ? o/n :").strip().lower()
  if choix == 'o':
    os.system('clear')
    return
  else: exit()

     
  

if __name__ == "__main__":
 menu()
