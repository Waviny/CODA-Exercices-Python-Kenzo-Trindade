🐍 Python Algorithmic Journey
60 Exercices progressifs : De la syntaxe de base à la logique algorithmique complexe.

Bienvenue sur ce dépôt ! Ce projet regroupe une collection structurée de 60 exercices en Python, conçus pour développer et consolider mes compétences en programmation. Il ne s'agit pas simplement de scripts isolés, mais d'une suite logique couvrant les fondamentaux du langage, la manipulation de structures de données et la résolution de problèmes mathématiques classiques.

🎯 Objectifs du Projet
L'objectif de ce dépôt est de démontrer ma capacité à :

Maîtriser la syntaxe Python (variables, boucles, conditions, fonctions).

Manipuler les données (listes, chaînes de caractères, entiers).

Implémenter des algorithmes (tris, recherches, suites mathématiques).

Structurer un programme via un menu interactif permettant de tester chaque exercice individuellement.

🛠️ Compétences Techniques Abordées
Ce projet traverse plusieurs niveaux de difficulté, illustrant une montée en compétence progressive :

1. Entrées / Sorties & Opérations de base (Niveau Découverte)
Interaction utilisateur via input() et formatage de print().

Calculs arithmétiques, conversions d'unités (Temps, Monnaie) et calculs de TVA.

Géométrie simple (Périmètre, Aire).

2. Logique Conditionnelle (Niveau Basique)
Utilisation avancée des structures if, elif, else.

Comparaisons logiques, vérification de parité, classification (Majeur/Mineur, Notes).

3. Boucles & Itérations
Maîtrise des boucles for et while.

Tables de multiplication, cumuls, répétitions contrôlées.

Dessin de formes géométriques en console (patterns d'étoiles).

4. Structures de Données & Algorithmique
Listes (Arrays) : Création, parcours, recherche de maximum/minimum, moyennes.

Recherche : Algorithmes de recherche d'occurrence dans une liste.

Mathématiques appliquées :

Nombres Premiers.

Suite de Fibonacci.

Triangle de Pascal.

Nombres d'Armstrong.

Vérification de Carrés Magiques.

💻 Structure du Code
Le projet est contenu dans un script principal modulaire. Chaque exercice est encapsulé dans sa propre fonction (exercice1() à exercice60()), garantissant la lisibilité et la maintenance du code.

Le point d'entrée est la fonction main(), qui agit comme un dispatcheur.

Aperçu du fonctionnement :
Python

def main():
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    # Le programme redirige vers la fonction correspondante
    if choix == "1":
        exercice1()
    # ...
🚀 Comment utiliser ce projet
Pour tester les exercices sur votre machine locale :

Cloner le dépôt :

Bash

git clone https://github.com/votre-nom-utilisateur/nom-du-repo.git
Accéder au dossier :

Bash

cd nom-du-repo
Lancer le script :

Bash

python main.py
Interagir : Entrez simplement le numéro de l'exercice (de 1 à 60) lorsque l'invite de commande apparaît.

🔍 Exemples d'Algorithmes Notables
Voici quelques exercices clés présents dans ce dépôt :

Exercice 50 (Fibonacci) : Génération de la suite de Fibonacci jusqu'à N termes.

Exercice 52 (Carré Magique) : Algorithme vérifiant si une matrice 3x3 donnée est un carré magique (sommes des lignes, colonnes et diagonales identiques).

Exercice 58 (Nombre d'Armstrong) : Vérification si un entier est égal à la somme de ses chiffres élevés à la puissance 3.

