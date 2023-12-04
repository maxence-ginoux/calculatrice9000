num1 = input("veuillez taper le premier nombre : ")
operator = str(input("veuillez taper le type d'opération : "))
num2 = int(input("veuillez taper le deuxième nombre : "))

def calcule (num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)
    
    resultat_addition = num1 + num2
    resultat_soustraction = num1 - num2
    resultat_division = num1 / num2
    resultat_multiplication = num1 * num2
                                        
    if operator == "+":
        if num1 == int(input("veuillez taper le premier nombre : ")):
            print(f"est égale à {resultat_addition}")
        else:
            print("COUCOU SOSO")
    elif operator == "-":
        return f"est égale à {resultat_soustraction}"
    elif operator == "/":
        if num2 != 0:
            return f"est égale à {resultat_division}"
        else:
            return "erreur ! division par 0 impossible !"
    elif operator == "*":
        return f"est égale à {resultat_multiplication}"
    else:
        return "opération impossible !"
    
    
resultat = calcule(num1, operator, num2)
print(resultat)


#print(calcule(9, "+", 10))
#print(calcule(9, "-", 10))
#print(calcule(9, "/", 10))
#print(calcule(9, "*", 10))