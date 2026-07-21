noms_eaux = []
volumes = []
prix_unitaires = []
quantites = []


while True:
    """Cette boucle permet de demander à l'utilisateur 
        combien de produits il souhaite enregistrer,
        en s'assurant que l'entrée est un nombre entier positif."""
    try:
        nombre = int(input("Combien de produits souhaitez-vous enregistrer ? : "))

        if nombre <= 0:
            print("Le nombre doit être supérieur à 0.\n")
            continue

        break

    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide.\n")


print("\n===== SAISIE DES DONNÉES =====\n")

for i in range(nombre):
    print(f"Produit n°{i+1}")

    nom = input("Nom de l'eau : ").lower()

    while True:
        """"Cette boucle permet de demander à l'utilisateur le volume de la bouteille,"""
        try:
            volume = float(input("Volume de la bouteille (L) : "))
            if volume <= 0:
                print("Le volume doit être positif.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un volume valide.")

    while True:
        """ Cette boucle permet de demander à l'utilisateur le prix unitaire de la bouteille,"""
        try:
            prix = float(input("Prix unitaire (FCFA) : "))
            if prix < 0:
                print("Le prix ne peut pas être négatif.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un prix valide.")

    while True:
        """ Cette boucle permet de demander à l'utilisateur la quantité vendue,"""
        try:
            quantite = int(input("Quantité vendue : "))
            if quantite < 0:
                print("La quantité ne peut pas être négative.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un entier valide.")

    noms_eaux.append(nom)
    volumes.append(volume)
    prix_unitaires.append(prix)
    quantites.append(quantite)

    print("-" * 40)



def volume_total():
    return sum(volumes)


def nombre_marques():
    return len(set(noms_eaux))


def nombre_bouteilles():
    return sum(quantites)


def chiffre_affaires():
    total = 0
    for qte, prix in zip(quantites, prix_unitaires):
        total += qte * prix
    return total


def statistics_eau():
    """"Affiche le rapport statistique des ventes d'eau. """

    print("\n")
    print("=" * 80)
    print("              RAPPORT STATISTIQUE DES VENTES D'EAU")
    print("=" * 80)

    print(f"Nombre de produits enregistrés : {len(noms_eaux)}")
    print(f"Nombre de marques différentes  : {nombre_marques()}")
    print(f"Volume total enregistré        : {volume_total():.2f} L")
    print(f"Nombre total de bouteilles     : {nombre_bouteilles()}")
    print(f"Chiffre d'affaires             : {chiffre_affaires():,.0f} FCFA")

    print("\n")
    print("-" * 80)
    print("{:<20}{:<12}{:<10}{:<12}{:<15}".format(
        "Marque",
        "Volume",
        "Qté",
        "Prix",
        "Vente"))

    print("-" * 80)

    for nom, volume, qte, prix in zip(
            noms_eaux,
            volumes,
            quantites,
            prix_unitaires):

        vente = qte * prix

        print("{:<20}{:<12}{:<10}{:<12}{:<15}".format(
            nom,
            f"{volume} L",
            qte,
            f"{prix:.0f}",
            f"{vente:.0f}"))

    print("-" * 80)
    print(f"CHIFFRE D'AFFAIRES TOTAL : {chiffre_affaires():,.0f} FCFA")
    print("=" * 80)



def classement_eaux():
    """ Cette fonction permet de classer les produits le plus vendue"""

    ventes = {}

    # Regroupement des quantités par marque
    for nom, qte in zip(noms_eaux, quantites):
        if nom in ventes:
            ventes[nom] += qte
        else:
            ventes[nom] = qte

    total = sum(ventes.values())

    classement = sorted(
        ventes.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n")
    print("=" * 80)
    print("           CLASSEMENT DES EAUX LES PLUS VENDUES")
    print("=" * 80)

    print("{:<6}{:<20}{:<15}{:<15}".format(
        "Rang",
        "Marque",
        "Quantité",
        "Pourcentage"))

    print("-" * 80)

    for rang, (nom, qte) in enumerate(classement, start=1):

        pourcentage = (qte / total) * 100

        print("{:<6}{:<20}{:<15}{:<14.2f}%".format(
            rang,
            nom,
            qte,
            pourcentage))

    print("=" * 80)


statistics_eau()
classement_eaux()