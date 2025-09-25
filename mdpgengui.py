import os

def c():
    os.system('clear')

def menu():
    while True:
        c()
        print("Calculatrice")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")
        choix = input("Choisissez une option (1-5): ")
    
        try:
            if choix == '1':
                c()
                addition()
            elif choix == '2':
                c()
                soustraction()
            elif choix == '3':
                c()
                multiplication()
            elif choix == '4':
                c()
                division()
            elif choix == '5':
                c()
                break
            else:
                c()
                print("Option invalide. Veuillez choisir une option entre 1 et 5.")
        
        except ValueError:
            c()
            print("Une erreur est survenue. Veuillez entrer un nombre entre 1 et 5.")

def pause_menu():
    while True:
        print('Veut-tu continuer? (o/n)')
        a = input(':')
        if a == 'o':
            menu()
        elif a == 'n':
            c()
            exit()

def addition():
    while True:
        try:
            n1 = float(input("Entrez le premier nombre: "))
            c()
            n2 = float(input("Entrez le deuxième nombre: "))
            c()
            resultat = n1 + n2
            print(f"Le résultat de {n1} + {n2} = {resultat}")
            pause_menu()
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres valides.")

def soustraction():
    while True:
        try:
            n1 = float(input("Entrez le premier nombre: "))
            c()
            n2 = float(input("Entrez le deuxième nombre: "))
            c()
            resultat = n1 - n2
            print(f"Le résultat de {n1} - {n2} = {resultat}")
            pause_menu()
        except ValueError:
            c()
            print("Entrée invalide. Veuillez entrer des nombres valides.")

def multiplication():
    while True:
        try:
            n1 = float(input("Entrez le premier nombre: "))
            c()
            n2 = float(input("Entrez le deuxième nombre: "))
            c()
            resultat = n1 * n2
            print(f"Le résultat de {n1} x {n2} = {resultat}")
            pause_menu()
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres valides.")

def division():
    while True:
        try:
            n1 = float(input("Entrez le premier nombre: "))
            c()
            n2 = float(input("Entrez le deuxième nombre: "))
            c()
            resultat = n1 / n2
            print(f"Le résultat de {n1} / {n2} = {resultat}")
            pause_menu()
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres valides.")
    

if __name__ == "__main__":
    menu()