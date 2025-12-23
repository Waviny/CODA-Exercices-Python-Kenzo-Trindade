
# Project Title

A brief description of what this project does and who it's for

# 🐍 Python Algorithmic Progression

![Python](https://img.shields.io/badge/Language-Python_3-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Exercises](https://img.shields.io/badge/Exercises-60-orange?style=for-the-badge)

> **Un parcours progressif de 60 exercices : De la syntaxe élémentaire à la logique algorithmique complexe.**

---

## 📋 Présentation

Ce dépôt regroupe une collection structurée de scripts Python. L'objectif n'était pas seulement d'écrire du code, mais de construire une logique de programmation solide.

Le projet est conçu de manière **modulaire** : un script principal centralise l'exécution via un menu interactif, permettant de tester chaque concept indépendamment.

### 🛠️ Compétences démontrées
* **Architecture logicielle :** Utilisation de fonctions et point d'entrée `if __name__ == "__main__":`.
* **Manipulation de données :** Tableaux, chaînes de caractères, conversions de types.
* **Logique algorithmique :** Tris, recherches, récursivité simulée, suites mathématiques.

---

## 🗂️ Catalogue des Exercices

Les exercices sont classés par niveau de complexité et par concepts techniques.

### 🔹 Niveau 1 : Fondamentaux & Interactions
<details>
<summary>👀 <em>Voir le détail (Exercices 1 à 19)</em></summary>
<br>

| Ex. | Concept Clé | Description Rapide |
|:---:|:---|:---|
| **01-05** | E/S Standard | `print`, `input`, variables et concaténation. |
| **06-11** | Arithmétique | Opérations de base (+, -, *, /, //, **). |
| **12-14** | Boucles simples | Premières itérations `for` et répétitions. |
| **15-16** | Géométrie | Calculs de périmètres et d'aires. |
| **17-19** | Conversions | Devises, Temps (Minutes -> Secondes), TVA. |

</details>

### 🔹 Niveau 2 : Logique Conditionnelle
<details>
<summary>⚡ <em>Voir le détail (Exercices 20 à 29 & 38-40)</em></summary>
<br>

| Ex. | Concept Clé | Description Rapide |
|:---:|:---|:---|
| **20-23** | Conditions | Structures `if`, `elif`, `else`. Majorité, validation. |
| **24-25** | Comparaisons | Comparaison de grandeurs et ordres (croissant). |
| **26** | Modulo | Test de divisibilité par 5. |
| **27-29** | Catégorisation | Classification par tranches (Âge, États de l'eau, Mentions Bac). |
| **38** | Calculatrice | Menu de sélection d'opérations basiques. |
| **40** | Sécurité | Vérification de longueur de mot de passe. |

</details>

### 🔹 Niveau 3 : Boucles Avancées & Itérations
<details>
<summary>🔄 <em>Voir le détail (Exercices 30 à 37 & 53, 60)</em></summary>
<br>

| Ex. | Concept Clé | Description Rapide |
|:---:|:---|:---|
| **30-32** | Cumuls | Somme d'entiers consécutifs (1 à N). |
| **33** | Tables | Générateur de tables de multiplication. |
| **35** | Math | Recherche de carrés parfaits inférieurs à N. |
| **37** | Patterns | Algorithme de dessin (pyramide d'étoiles). |
| **53** | Binaire | Conversion Décimal vers Binaire. |
| **60** | Dessin | Génération de rectangles creux en console. |

</details>

### 🔹 Niveau 4 : Structures de Données (Listes)
<details>
<summary>📊 <em>Voir le détail (Exercices 41 à 49)</em></summary>
<br>

| Ex. | Concept Clé | Description Rapide |
|:---:|:---|:---|
| **41** | Moyenne | Calcul de moyenne sur une liste dynamique. |
| **42** | Min/Max | Recherche de valeurs extrêmes sans fonctions natives. |
| **43-44** | String Parsing | Comptage de voyelles, Inversion de chaînes. |
| **46-47** | Recherche | Recherche linéaire d'un élément et comptage d'occurrences. |
| **48-49** | Diviseurs | Liste des diviseurs et test de **Nombre Premier**. |

</details>

### 🔹 Niveau 5 : Algorithmique Avancée
<details>
<summary>🧠 <em>Voir le détail (Exercices 50 à 59)</em></summary>
<br>

C'est ici que se trouvent les défis logiques les plus intéressants.

| Ex. | Nom de l'algorithme | Description |
|:---:|:---|:---|
| **50** | **Suite de Fibonacci** | Génération des N premiers termes (u_n = u_n-1 + u_n-2). |
| **51** | **Triangle de Pascal** | Construction ligne par ligne basée sur la précédente. |
| **52** | **Carré Magique** | Vérification matricielle (sommes lignes/colonnes/diagonales). |
| **55** | **Suite Logique** | Calcul de sommes basées sur une formule `n*(n-1)`. |
| **57** | **Le mot le plus long** | Algorithme de parcours de phrase et détection de longueur. |
| **58** | **Nombre Armstrong** | Vérification mathématique (Somme des cubes des chiffres). |

</details>

---

## 💻 Aperçu du Code

Le projet utilise un système de menu pour garder le code propre et navigable. Voici comment le programme principal orchestre les appels de fonctions :

```python
def main():
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    
    # Dispatching dynamique
    if choix == "50":
        exercice50() # Fibonacci
    elif choix == "52":
        exercice52(carre1) # Carré Magique
    # ... gestion des autres cas
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":  
    main()
