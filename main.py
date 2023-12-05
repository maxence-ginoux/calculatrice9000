

def calcule (num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)
    
    resultat_addition = num1 + num2
    resultat_soustraction = num1 - num2
    resultat_division = num1 / num2
    resultat_multiplication = num1 * num2
                                        
    if operator == "+":
        return f"{num1} {operator} {num2} est égale à {resultat_addition}"
    elif operator == "-":
        return f"{num1} {operator} {num2} est égale à {resultat_soustraction}"
    elif operator == "/":
        return f"{num1} {operator} {num2} est égale à {resultat_division}"
    elif operator == "*":
        return f"{num1} {operator} {num2} est égale à {resultat_multiplication}"
    else:
        return "ERREUR opération impossible ! veuillez saisir un opérateur valide !"
    

while True:
    try:
        num1 = input("veuillez taper le premier nombre : ")
        operator = str(input("veuillez taper le type d'opération : "))
        num2 = int(input("veuillez taper le deuxième nombre : "))
        resultat = calcule(num1, operator, num2)
        print(resultat)
        break

    except ZeroDivisionError:
        print("La division par zéro n'est pas autorisée. Veuillez réessayer.")
    except Exception:
        print("Une erreur s'est produite. Veuillez réessayer.")