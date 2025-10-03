from random import randint

def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

# Niveau Découverte 2
def exercice2():
    print("Bonjour le monde !")

# Niveau Découverte 3
def exercice3():
    name = input("Quel est ton prénom")
    print("Bonjour", name, " ! ")

# Niveau Découverte 4
def exercice4():
    print("Première ligne \n Deuxième ligne \n Troisème ligne")

# Niveau Découverte 5
def exercice5():
    annee = int(input("Quelle est votre année de naissance : "))
    age = 2025 - annee
    print("Vous avez environ ", age, " ans")

# Niveau Découverte 6
def exercice6():
    a = int(input("Veuillez entrer un premier chiffre : "))
    b = int(input("Entrez un deuxième chiffre : "))
    c = a + b
    print(a, " + ", b, " = ", c)

# Niveau Découverte 7
def exercice7():
    a = int(input("Veuillez entrer un premier chiffre : "))
    b = int(input("Entrez un deuxième chiffre : "))
    c = a - b
    print(a, " - ", b, " = ", c)

# Niveau Découverte 8
def exercice8():
    a = int(input("Veuillez entrer un premier chiffre : "))
    b = int(input("Entrez un deuxième chiffre : "))
    c = a * b
    print(a, " x ", b, " = ", c)

# Niveau Découverte 9
def exercice9():
    a = int(input("Veuillez entrer un premier chiffre : "))
    b = int(input("Entrez un deuxième chiffre : "))
    c = a // b
    print(a, " / ", b, " = ", c)

# Niveau Découverte 10
def exercice10():
    nombre = int(input("Veuillez entrer un premier chiffre : "))
    resultat = nombre ** 2
    print(nombre, " au carré = ", resultat)

# Niveau Découverte 11
def exercice11():
    nombre = int(input("Quel est votre nombre"))
    moitie = nombre / 2
    print("Le moitié de : ", nombre, " est ", moitie)

# Niveau Découverte 12
def exercice12():
    message = int(input("Veuillez entrer votre message : "))
    for i in range(1, 6):
        print(message)

# Niveau Découverte 13
def exercice13():
    for i in range(1, 6):
        print(i)

# Niveau Découverte 14
def exercice14():
    for i in range(1, 6):
        print("2 x ", i, " = ", 2*i)

# Niveau Découverte 15
def exercice15():
    cote = int(input("Veuillez entrer la longueur de votre côté : "))
    perimetre = cote * 4
    print("La périmètre de votre carré de longueur", cote, "est de ", perimetre)

# Niveau Découverte 16
def exercice16():
    cote = int(input("Veuillez entrer la longueur de votre côté : "))
    air = cote ** 2
    print("L'air de votre carré de longueur", cote, "est de ", air)

# Niveau Découverte 17
def exercice17():
    nombre = int(input("Veuillez entrer votre prix en Euros : "))
    nombre_dollars = nombre * 1.1
    print("Votre prix", nombre, "en euros, fait ", nombre_dollars, "en dollars !")

# Niveau Découverte 18
def exercice18():
    minute_en_seconde = 60
    minute_donnee = int(input("Veuillez saisir votre nombre de minutes : "))
    minute_resultat = minute_donnee * minute_en_seconde
    print("En seconde, ", minute_donnee, "vaut ", minute_resultat, " secondes !")

# Niveau Découverte 19
def exercice19():
    TVA = 1.2
    prix_HT = int(input("Veuillez saisir votre prix horss taxe : "))
    prix_TTC = prix_HT * TVA
    print("Votre prix hors taxe, ", prix_HT, "vaudra ", prix_TTC, "après TVA")

# Niveau Basique 20
def exercice20():
    name = input("Quel est votre nom : ")
    age = int(input("Quel est votre âge : "))
    print("Bonjour, ", name, " comment allez  vous aujourd'hui ? Vous avez toujours ", age, " ? ")

# Niveau Basique 21
def exercice21():
    nombre = int(input("Veuillez entrer votre nombre : "))
    if nombre == 0:
        print("Votre nombre est Nul")
    elif nombre > 0:
        print("Votre nombre est positif")
    elif nombre < 0:
        print("Votre nombre est négatif")
    else:
        print("Erreur, veuillez entrer un nombre valide")

# Niveau Basique 22
def exercice22():
    age = int(input("Veuillez entrer votre âge : "))
    if age >= 18:
        print("Vous êtes majeur")
    elif age < 18:
        print("Vous êtes mineur")
    else:
        print("Erreur, veuillez entrer un nombre valide")

# Niveau Basique 23
def exercice23():
    note = int(input("Veuillez entre votre note : "))
    if note >= 10:
        print("Validé")
    elif note < 10:
        print("Non validé")
    else:
        print("Erreur, veuillez entrer un nombre valide")

# Niveau Basique 24
def exercice24():
    nombreA = int(input("Veuillez entrer votre premier nombre : "))
    nombreB = int(input("Veuillez entrer votre deuxième nombre : "))
    if nombreA > nombreB:
        print("Votre premier nombre, ", nombreA, " est plus grand que votre deuxième nombre, ", nombreB)
    elif nombreB > nombreA:
        print("Votre deuxième nombre, ", nombreB, " est plus grand que votre premier nombre, ", nombreA)
    else:
        print("Nombres égaux")

# Niveau Basique 25
def exercice25():
    nombreA = int(input("Veuillez entrer votre premier nombre : "))
    nombreB = int(input("Veuillez entrer votre deuxième nombre : "))
    if nombreA < nombreB:
        print("Ordre croissant")
    elif nombreA > nombreB:
        print("Ordre non croissant ( décroissant )")
    else:
        print("Veuillez entrer des nombres valides")

# Niveau Basique 26
def exercice26():
    nombre = int(input("Veuillez entrer votre nombre : "))
    divisible = nombre % 5
    if divisible == 0:
        print("Le nombre ", nombre, " est divisible par 5")
    elif divisible != 0:
        print("Le nombre ", nombre, " n'est pas divisble par 5")
    else:
        print("Veuillez entrer un nombre valide")

# Niveau Basique 27
def exercice27():
    age = int(input("Veuillez entrer votre âge : "))
    if age  < 12:
        print("Enfant")
    elif 12 < age < 17:
        print("Ado")
    elif age >= 18:
        print("Adulte")
    else:
        print("Veuillez entrer un âge valide")

# Niveau Basique 28
def exercice28():
    temperature = int(input("Veuillez entrer la température : "))
    if temperature < -5:
        print("Glace")
    elif -5 < temperature < 105:
        print("Eau liquide")
    elif temperature > 105:
        print("Vapeur")
    else:
        print("Veuillez entrer une température valide")

# Niveau Basique 29
def exercice29():
    note = int(input("Veuillez entrer votre note du bac : "))
    if note <= 8:
        print("Recalé")
    elif 8 < note <= 11:
        print("Passable")
    elif 11 < note <= 14:
        print("Bien")
    elif 14 < note:
        print("Très bien")
    else:
        print("Veuillez entrer une note valide")

# Niveau Basique 30
def exercice30():
    n = int(input("Veuillez entre un nombre n : "))
    for element in range(1, n+1):
        print(element)

# Niveau Basique 31
def exercice31():
    n = int(input("Veuillez entrer un nombre n : "))
    for i in range(n+1):
        print(n)
        n -= 1

# Niveau Basique 32
def exercice32():
    resultat = 0
    n = int(input("Veuillez entrer un nombre n : "))
    for i in range(1, n+1):
        resultat += i
        print(resultat)
        
# Niveau Basique 33
def exercice33():
    table = int(input("Veuillez entrer la table que vous désirez : "))
    resultat = 0
    for i in range(1, 11):
        resultat = i*table
        print(table, " x ", i, " = ", resultat)

# Niveau Basique 34
def exercice34():
    n = int(input("Veuillez entrer un nombre n : "))
    for i in range(0, n+1):
        if i % 2 == 0:
            print(i)

# Niveau Basique 35
def exercice35():
    n = int(input("Veuillez entrer un nombre n : "))
    carre_parfait = 1
    for i in range(1, n+1):
        carre_parfait = i**2
        if carre_parfait < n:
            print(carre_parfait)

# Niveau Basique 36
def exercice36():
    mot = input("Veuillez netrer un mot : ")
    nombre_de_fois = int(input("Veuillez entrer un nombre de fois que le mot sera répété : "))
    for i in range (nombre_de_fois):
        print(mot)

# Niveau Basique 37
def exercice37():
    taille = int(input("Chiffre : "))
    resultat = taille - (taille - 1)
    wi = taille - resultat
    for i in range(0, taille):
        print(" "*wi, "*"*resultat, " "* wi)
        wi -= 1
        resultat += 2
            
# Niveau Basique 38
def exercice38():
    numA = int(input("Numéro A : "))
    numB = int(input("Numéro B : "))
    print("1 - Addition\n" \
    "2 - Soustraction\n" \
    "3 - Multiplication\n" \
    "4 - Division")
    chiffre = input("Veuillez choisir une opération : ")
    if chiffre == "1":
        print(numA + numB)
    elif chiffre == "2":
        print(numA - numB)
    elif chiffre == "3":
        print(numA * numB)
    elif chiffre == "4":
        print(numA / numB)
    else:
        print("Veuillez entrer une nombre valide")
        
# Niveau Basique 39
def exercice39():
    num = randint(1, 100)
    message = input("Veuillez entrer une réponse ( pair / impair )")
    if message == "pair":
        if num % 2 == 0:
            print("gagné le nombre était : ", num)
        else:
            print("perdu le nombre était : ", num)
    elif message == "impair":
        if num % 2 != 0:
            print("gagné le nombre était : ", num)
        else:
            print("perdu le nombre était : ", num)
    else:
        print("Veuillez saisir pair ou impair")

# Niveau Basique 40
def exercice40():
    mdp = input("Veuillez saisir votre mot de passe : ")
    if len(mdp) > 6:
        print("Le mot de passe fait plus de 6 caractères")
    else:
        print("Mot de passe trop court ( + 6 caractères )")

# Niveau Basique 41
def exercice41():
    notes = []
    resultat = 0
    n = int(input("Combien de notes avez vous ?"))
    for i in range(1, n+1):
        note = int(input("Veuillez saisir vos notes : "))
        notes.append(note)
    for j in range(0, len(notes)):
        resultat = resultat + notes[j]
    resultat = resultat / n
    print("Moyennes des notes : ", resultat)

# Niveau Basique 42
def exercice42():
    n = int(input("Combien de nombres voulez vous ? "))
    list = []
    for i in range(1, n+1):
        v = int(input("Veuillez saisir les nombres : "))
        list.append(v)
    for j in range(1, len(list)):
        vmin = list[0]
        vmax = list[0]
        if list[j] < vmin:
            vmin = list[j]
        if list[j] > vmax:
            vmax = list[j]
    print("Le nombre le plus grand est : ", vmax, " et le plus petit est : ", vmin)

# Niveau Basique 43
def exercice43():
    compteur = 0
    mot = input("Veuillez saisir un mot : ")
    voyelles = ["a", "e", "i", "o", "u", "y"]
    for lettre in mot :
        for i in range(1, len(voyelles)):
            if lettre == voyelles[i]:
                compteur += 1
    print(compteur)

# Niveau Basique 44
def exercice44():
    mot = input("Veuillez saisir un mot : ")
    res = ""
    for lettre in mot :
        res = lettre + res
    print(res)

# Niveau Basique 45
def exercice45():
    list = []
    nb = int(input("Combien voulez vous de nombres ? "))
    resultat = 0
    for i in range(1, nb+1):
        add = input("Veuillez saisir les nombres : ")
        list.append(add)
    for j in range(0, len(list)):
        resultat = resultat + int(list[j])
    print(resultat)

# Niveau Basique 46
def exercice46():
    list = []
    nb = int(input("Combien voulez vous de nombres ? "))
    find = int(input("Veuillez saisir le nombre chercher : "))
    resultat = 0
    for i in range(1, nb+1):
        add = input("Veuillez saisir les nombres : ")
        list.append(add)
    for j in range(0, len(list)):
        if find == int(list[j]):
            print("Trouvé, à la position : ", j)
    
# Niveau Basique 47
def exercice47():
    list = []
    nb = int(input("Combien voulez vous de nombres ? "))
    find = int(input("Veuillez saisir le nombre chercher : "))
    compteur = 0
    resultat = 0
    for i in range(1, nb+1):
        add = input("Veuillez saisir les nombres : ")
        list.append(add)
    for j in range(0, len(list)):
        if find == int(list[j]):
            compteur += 1
    print("Votre nombre : ", find, " apparraît : ", compteur, " fois ")

# Niveau Basique 48
def exercice48():
    nombre = int(input("Veuillez saisir un nombre : "))
    diviseurs = []
    for i in range(1, nombre+1):
        if nombre % i == 0:
            diviseurs.append(i)
    print("Les diviseurs de ce nombre sont : ", diviseurs)

# Niveau Basique 49
def exercice49():
    list = []
    nombre = int(input("Veuillez saisir un nombre : "))
    for i in range(1, nombre+1):
        if nombre % i == 0:
            list.append(i)
    if len(list) == 2:
        print("Le nombre est premier")
    else:
        print("Le nombre n'est pas premier")

# Niveau Basique 50
def exercice50():
    N = int(input("Veuillez entrez un nombre : "))
    a, b = 0, 1
    list = []
    for i in range(0, N):
        list.append(a)
        a, b = b, a + b
    print(list)


# Niveau Basique 51
def exercice51():
    list = [1]
    n = 3
    for i in range(1, n+1):
        list2 = list + [1]
        for j in range(len(list) - 1):
            list2[j+1] = list[j] + list2[j+1]
        list = list2
        print(list2)

# Niveau Basique 52
def exercice52(carre):
    cible = sum(carre[0])
    
    for ligne in carre:
        if sum(ligne) != cible:
            return False
    
    for j in range(3):
        if carre[0][j] + carre[1][j] + carre[2][j] != cible:
            return False
    
    if carre[0][0] + carre[1][1] + carre[2][2] != cible:
        return False
    if carre[0][2] + carre[1][1] + carre[2][0] != cible:
        return False
    
    return True
        
carre1 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]


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
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    elif choix == "31":
        exercice31()
    elif choix == "32":
        exercice32()
    elif choix == "33":
        exercice33()
    elif choix == "34":
        exercice34()
    elif choix == "35":
        exercice35()
    elif choix == "36":
        exercice36()
    elif choix == "37":
        exercice37()
    elif choix == "38":
        exercice38()
    elif choix == "39":
        exercice39()
    elif choix == "40":
        exercice40()
    elif choix == "41":
        exercice41()
    elif choix == "42":
        exercice42()
    elif choix == "43":
        exercice43()
    elif choix == "44":
        exercice44()
    elif choix == "45":
        exercice45()
    elif choix == "46":
        exercice46()
    elif choix == "47":
        exercice47()
    elif choix == "48":
        exercice48()
    elif choix == "49":
        exercice49()
    elif choix == "50":
        exercice50()
    elif choix == "51":
        exercice51()
    elif choix == "52":
        exercice52(carre1)
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":  
    main()