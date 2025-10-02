def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

# Niveau Découverte 2
def exercice2():
    print("Bonjour le monde !")

# Niveau Découverte 3
def exercice3():
    name = input("Quel est ton prénom")
    print("Bonjour", name)

# Niveau Découverte 4
def exercice4():
    print("Première ligne \n Deuxième ligne \n Troisème ligne")

# Niveau Découverte 5
def exercice5():
    annee = input("Quelle est votre année de naissance : ")
    age = 2025 - annee
    print(age)

# Niveau Découverte 6
def exercice6():
    a = input("Veuillez entrer un premier chiffre : ")
    b = input("Entrez un deuxième chiffre : ")
    c = a + b
    print("Le résultat est : ", c)

def main():
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix =="2":
        exercice2()
    elif choix =="3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":  
    main()