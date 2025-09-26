#!/usr/bin/env python3
import random
import string
import os
from datetime import datetime

HISTORY_FILE = "mdp.txt"

def clear():
    os.system('clear')

def mdp_dmd_user():
    clear()
    longueur = int(input("Longueur du Mot De Passe: "))
    inclure_symbole = input("Inclure des Symboles ? o/n (Recommandé !)").strip()
    caracteres = string.ascii_letters + string.digits
    if inclure_symbole.lower() == "o":
      caracteres += string.punctuation
    mdp = "".join(random.choice(caracteres) for _ in range (longueur))
    clear()
    print("Mot De Passe Généré :" , mdp)
    historique(mdp, "Personnalisé", longueur)
    pause_menu()
    

def mdp_gen_16cara():
   clear()
   caracters = string.ascii_letters + string.digits + string.punctuation
   longueur = 16
   mdp = "".join(random.choice(caracters) for _ in range (longueur))
   clear()
   print("\n Mot de Passe (16 caractères) :", mdp)
   historique(mdp, "Automatique", longueur)
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
     print("3.Voir l'historique des mots de passes générés.")
     print("4.Effacer l'historique.")
     print("5.Quitter.")
     choix = input(":").strip().lower()
     if choix == "1":
      mdp_dmd_user()
     elif choix == "2":
      mdp_gen_16cara()
     elif choix == "3":
      voir_historique()
     elif choix == "4":
      effacer_historique()
     elif choix == "5":
      clear()
      break
     else:
      print("Choix invalide, Entre 1,2,3,4 ou 5.")

def pause_menu():
  choix = input("\nContinuer ? o/n :").strip().lower()
  if choix == 'o':
    clear()
    return
  else: exit()

def historique(mdp, type_label, longueur):
  """Ajoute une ligne d'historique au fichier HISTORY_FILE."""
  timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
  line = f"{timestamp} | {type_label} | {longueur} | {mdp}\n"
    # Mode 'a' pour append, création si n'existe pas
  with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    
def voir_historique():
    clear()
    if not os.path.exists(HISTORY_FILE):
        print("Aucun historique trouvé.")
        pause_menu()
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Historique vide.")
        pause_menu()
        return

    print("=== Historique des mots de passe générés ===\n")
    # Affichage numéroté
    for i, line in enumerate(lines, start=1):
        # ligne format: timestamp | type | longueur | mdp
        print(f"{i}. {line.strip()}")
    print("\n--- Fin de l'historique ---")
    pause_menu()

def effacer_historique():
    clear()
    if not os.path.exists(HISTORY_FILE):
        print("Aucun fichier d'historique à supprimer.")
        pause_menu()
        return

    confirm = input("Confirme la suppression de l'historique ? o/n : ").strip().lower()
    if confirm == 'o':
        os.remove(HISTORY_FILE)
        print("Historique supprimé.")
    else:
        print("Suppression annulée.")
    pause_menu()

     
if __name__ == "__main__":
 menu()
