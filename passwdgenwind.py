#!/usr/bin/env python3
import random
import string
import os
import secrets
from datetime import datetime

HISTORY_FILE = "mdp.txt"
EXCLUDE_CHARS = "\"'\\ `;:/|&$ "   

def clear():
    os.system('cls')

def generate_password(length=16,
                      require_lower=True, require_upper=True,
                      require_digits=True, require_symbols=True,
                      exclude_chars=""):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    sets = []
    pool = ""

    if require_lower:
        sets.append(lower); pool += lower
    if require_upper:
        sets.append(upper); pool += upper
    if require_digits:
        sets.append(digits); pool += digits
    if require_symbols:
        sets.append(symbols); pool += symbols

    if not sets:
        pool = lower + upper + digits + symbols

    if exclude_chars:
        exclude_set = set(exclude_chars)
        pool = ''.join(ch for ch in pool if ch not in exclude_set)
        sets = [''.join(ch for ch in s if ch not in exclude_set) for s in sets]

    if not pool:
        raise ValueError("Pool vide après exclusion")

    min_required = len([s for s in sets if s])
    if length < min_required:
        raise ValueError(f"Longueur trop courte : minimum requis = {min_required}")

    password_chars = [secrets.choice(s) for s in sets if s]

    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

def mdp_dmd_user():
    clear()

    while True:
        try:
            nom_mdp = input("Nom du mot de passe (ex: YouTube, Gmail): ").strip()
            if any(char.isdigit() for char in nom_mdp):
                print("Erreur : le nom ne doit pas contenir de chiffres.")
                continue
            if not nom_mdp:
                print("Erreur : le nom ne doit pas être vide.")
                continue
            break

        except ValueError:
            print("Entrée invalide : entre un nom sans chiffre.")   
   
    
    while True:
        try:
            longueur = int(input("Longueur du Mot De Passe (entre 6 et 64): ").strip())
            if longueur < 6 or longueur > 64:
                print("Erreur : la longueur doit être entre 6 et 64 caractères.")
                continue  
            break  
        except ValueError:
            print("Entrée invalide : entre un nombre entier.")

    while True:
        inclure_symbole = input("Inclure des Symboles ? o/n (Recommandé !) : ").strip().lower()
        if inclure_symbole in ('o', 'n'):
            break
        print("Entrée invalide : entre 'o' ou 'n'.")
       

    try:
        mdp = generate_password(length=longueur,
                                require_lower=True,
                                require_upper=True,
                                require_digits=True,
                                require_symbols=(inclure_symbole == 'o'),
                                exclude_chars=EXCLUDE_CHARS)
    except ValueError as e:
        print("Erreur :", e)
        pause_menu()
        return

    clear()
    print(f"Mot De Passe Généré | {nom_mdp} => {mdp}")
    historique(mdp, nom_mdp, "Personnalisé", longueur)
    pause_menu()

def mdp_gen_16cara():
    clear()
    
    while True:
        try:
            nom_mdp = input("Nom du mot de passe (ex: YouTube, Gmail): ").strip()
            if any(char.isdigit() for char in nom_mdp):
                print("Erreur : le nom ne doit pas contenir de chiffres.")
                continue
            if not nom_mdp:
                print("Erreur : le nom ne doit pas être vide.")
                continue
            break
        
        except ValueError:
            print("Entrée invalide : entre un nom sans chiffre.")

    longueur = 16

    mdp = generate_password(length=longueur,
                            require_lower=True,
                            require_upper=True,
                            require_digits=True,
                            require_symbols=True,
                            exclude_chars=EXCLUDE_CHARS)
    clear()
    print(f"\n Mot de Passe (16 caractères) | {nom_mdp} => {mdp}")
    historique(mdp, nom_mdp, "Automatique", longueur)
    pause_menu()

def menu():
   while True:
     clear()
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

def pause_menu():
  while True:
    choix = input("\nContinuer ? o/n :").strip().lower()
    if choix == 'o':
        clear()
        return
    elif choix == 'n':
        clear()
        exit()
    else:
        print("Choix invalide, Entre o ou n.")

def historique(mdp, nom_mdp, type_label, longueur):
  """Ajoute une ligne d'historique au fichier HISTORY_FILE."""
  timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
  line = f"{timestamp} | {type_label} | Longueur = {longueur} |{nom_mdp} => {mdp}\n"
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
    
    while True:
        confirm = input("Confirme la suppression de l'historique ? o/n : ").strip().lower()
        if confirm == 'o':
            os.remove(HISTORY_FILE)
            print("Historique supprimé.")
        else:
            print("Suppression annulée.")
        pause_menu()

   
if __name__ == "__main__":
 menu()
