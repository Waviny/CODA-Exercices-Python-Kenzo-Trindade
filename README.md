# 🐍 Python Algorithmic Journey

![Python](https://img.shields.io/badge/Language-Python_3-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Exercises](https://img.shields.io/badge/Exercises-60-orange?style=for-the-badge)

> **A progressive journey of 60 exercises: From basic syntax to complex algorithmic logic.**

---

## 📋 Overview

This repository gathers a structured collection of Python scripts. The goal of this project was not only to write code but to build a solid **programming logic**.

The project is designed in a **modular** way: a main script centralizes execution via an interactive menu, allowing each concept to be tested independently.

### 🛠️ Key Skills
* **Software Architecture:** Use of functions and the `if __name__ == "__main__":` entry point.
* **Data Manipulation:** Arrays (Lists), strings, type conversions.
* **Algorithmic Logic:** Sorting, searching, simulated recursion, and mathematical sequences.

---

## 🗂️ Exercise Catalog

The exercises are categorized by complexity level and technical concepts.

### 🔹 Level 1: Fundamentals & Interactions
<details>
<summary>👀 <em>View details (Exercises 1 to 19)</em></summary>
<br>

| Ex. | Key Concept | Quick Description |
|:---:|:---|:---|
| **01-05** | Standard I/O | `print`, `input`, variables, and string formatting. |
| **06-11** | Arithmetic | Basic operations (+, -, *, /, //, **). |
| **12-14** | Simple Loops | First `for` iterations and repetitions. |
| **15-16** | Geometry | Perimeter and Area calculations. |
| **17-19** | Conversions | Currency, Time (Minutes -> Seconds), VAT. |

</details>

### 🔹 Level 2: Conditional Logic
<details>
<summary>⚡ <em>View details (Exercises 20 to 29 & 38-40)</em></summary>
<br>

| Ex. | Key Concept | Quick Description |
|:---:|:---|:---|
| **20-23** | Conditions | `if`, `elif`, `else` structures. Validation and age checks. |
| **24-25** | Comparisons | Comparing values and sorting orders (ascending). |
| **26** | Modulo | Divisibility test (by 5). |
| **27-29** | Categorization | Classification by ranges (Age, Water states, Grades). |
| **38** | Calculator | Basic operations selection menu. |
| **40** | Security | Password length verification. |

</details>

### 🔹 Level 3: Advanced Loops & Iterations
<details>
<summary>🔄 <em>View details (Exercises 30 to 37 & 53, 60)</em></summary>
<br>

| Ex. | Key Concept | Quick Description |
|:---:|:---|:---|
| **30-32** | Accumulators | Sum of consecutive integers (1 to N). |
| **33** | Tables | Multiplication table generator. |
| **35** | Math | Finding perfect squares smaller than N. |
| **37** | Patterns | Drawing algorithm (star pyramid). |
| **53** | Binary | Decimal to Binary conversion. |
| **60** | Drawing | Generating hollow rectangles in the console. |

</details>

### 🔹 Level 4: Data Structures (Lists)
<details>
<summary>📊 <em>View details (Exercises 41 to 49)</em></summary>
<br>

| Ex. | Key Concept | Quick Description |
|:---:|:---|:---|
| **41** | Average | Calculating the average of a dynamic list. |
| **42** | Min/Max | Finding extreme values without native functions. |
| **43-44** | String Parsing | Counting vowels, Reversing strings. |
| **46-47** | Search | Linear search for an element and counting occurrences. |
| **48-49** | Divisors | List of divisors and **Prime Number** check. |

</details>

### 🔹 Level 5: Advanced Algorithms
<details>
<summary>🧠 <em>View details (Exercises 50 to 59)</em></summary>
<br>

This section contains the most interesting logical challenges.

| Ex. | Algorithm Name | Description |
|:---:|:---|:---|
| **50** | **Fibonacci Sequence** | Generating the first N terms (u_n = u_n-1 + u_n-2). |
| **51** | **Pascal's Triangle** | Line-by-line construction based on the previous one. |
| **52** | **Magic Square** | Matrix verification (rows/columns/diagonals sums). |
| **55** | **Logical Sequence** | Calculating sums based on the formula `n*(n-1)`. |
| **57** | **Longest Word** | Sentence parsing algorithm to find the longest string. |
| **58** | **Armstrong Number** | Mathematical check (Sum of cubes of digits). |

</details>

---

## 💻 Code Overview

The project uses a menu system to keep the code clean and navigable. Here is how the main program orchestrates function calls:

```python
def main():
    choix = input("Enter the exercise number to run: ")
    
    # Dynamic Dispatching
    if choix == "50":
        exercice50() # Fibonacci
    elif choix == "52":
        exercice52(carre1) # Magic Square
    # ... handling other cases
    else:
        print("Exercise not recognized.")

if __name__ == "__main__":  
    main()
