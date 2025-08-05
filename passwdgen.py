#!/usr/bin/env python3
import random
import string
import os

def mdp_dmd_user():
    os.system('clear')
    longueur = int(input("Password Length: "))
    os.system('clear')
    caracteres = string.ascii_letters + string.digits
    while True: 
        inclure_symbole = input("Include The Symbols ? y/n (Recommended !)").strip() 
        if inclure_symbole == "y":
          caracteres += string.punctuation
          break
        elif inclure_symbole == "n":
          caracteres
          break
        else:
          os.system('clear')
    mdp = "".join(random.choice(caracteres) for _ in range (longueur))
    os.system('clear')
    print("Password Generated :" , mdp)
    pause_menu()
    

def mdp_gen_16cara():
   os.system('clear')
   caracters = string.ascii_letters + string.digits + string.punctuation
   longueur = 16
   mdp = "".join(random.choice(caracters) for _ in range (longueur))
   print("\n Password (16 caracters) :", mdp)
   pause_menu()

def menu():
   while True:
     os.system('clear')
     print("""
_____                                   _   _____                           _             
| ___ \                                 | | |  __ \                         | |            
| |_/ /_ _ ___ _____      _____  _ __ __| | | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|      
                                                                                        
""")
     print("1.Generate Password Customizable.")
     print("2.Generate Password Secure.")
     print("3.Exit.")
     choix = input(":").strip().lower()
     if choix == "1":
      mdp_dmd_user()
     elif choix == "2":
      mdp_gen_16cara()
     elif choix == "3":
      os.system('clear')
      break
     else:
       os.system('clear')
def pause_menu():
  choix = input("\nContinue ? y/n :").strip().lower()
  if choix == 'y':
    os.system('clear')
    return
  else: 
    os.system('clear')
    exit()

if __name__ == "__main__":
 menu()
