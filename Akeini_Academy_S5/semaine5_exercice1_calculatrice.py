def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def soustraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Erreur : division par 0 impossible"
    return a / b


while True:
    try:
        a = float(input("Entrer le premier  nombre : "))
        signe = input("Entrer un signe (+, -, *, /) : ")
        while signe not in ["+", "-", "*", "/"]:
            signe = input("Svp Veuillez saisir un operateur arithmetique (+, -, *, /) : ")
        b = float(input("Entrer le deuxième nombre : "))
        if signe == "+":
            resultat = addition(a, b)

        elif signe == "-":
            resultat = soustraction(a, b)

        elif signe == "*":
            resultat = multiplication(a, b)
        else:
            resultat = division(a, b)

        print("Résultat :", resultat)
        break
    except ValueError:
        print("Svp, veuillez entrer un nombre valide.")
