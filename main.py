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

# Niveau Découverte 7
def exercice7():
    a = input("Veuillez entrer un premier chiffre : ")
    b = input("Entrez un deuxième chiffre : ")
    c = a - b
    print("Le résultat est : ", c)

# Niveau Découverte 8
def exercice8():
    a = input("Veuillez entrer un premier chiffre : ")
    b = input("Entrez un deuxième chiffre : ")
    c = a * b
    print("Le résultat est : ", c)

# Niveau Découverte 9
def exercice9():
    a = input("Veuillez entrer un premier chiffre : ")
    b = input("Entrez un deuxième chiffre : ")
    c = a // b
    print("Le résultat est : ", c)

# Niveau Découverte 10
def exercice10():
    a = input("Veuillez entrer un premier chiffre : ")
    b = input("Entrez un deuxième chiffre : ")
    c = a ** b
    print("Le résultat est : ", c)

# Niveau Découverte 11
def exercice11():
    nombre = input("Quel est votre nombre")
    moitie = nombre // 2
    print("La moitié de votre nombre", moitie)

# Niveau Découverte 12
def exercice12():
    message = input("Veuillez entrer votre message : ")
    for i in range(1, 6):
        print(message)

# Niveau Découverte 13
def exercice13():
    for i in range(1, 6):
        print(i)











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
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":  
    main()