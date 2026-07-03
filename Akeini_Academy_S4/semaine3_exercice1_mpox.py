# Variables

total_suspects=0
total_confirmes=0
total_deces=0
total_actifs=0
total_vertes=0
total_jaunes=0
total_oranges=0
total_rouges=0
nb_districts=9

# Variables sur la fonction de plus, déterminer le département le plus touché
cas_cuvette = 0
cas_likouala = 0
cas_plateaux = 0
cas_pointe_noire = 0
cas_brazzaville = 0

# Utilisation de la boucle for  pour inserer les information sur les districts
for i in range(1,nb_districts+1):
    print(f"---District {i} ---")
    nom_district=input(f"Nom du district {i}: ")
    nom_department=input(f"Nom du department {i}: ")
    suspects=int(input(f"Suspects du district {i}: "))
    confirmes=int(input(f"Confirmes du district {i}: "))
    deces=int(input(f"Deces du district {i}: "))

    cas_actifs=confirmes-deces

    # # Détermination du taux de létalité
    if confirmes > 0:
        letalite = (deces / confirmes) * 100
    else:
        letalite = 0
    # # Détermination du niveau d'alerte du district
    if confirmes >= 10:
        alerte="Rouge"
        total_rouges += 1
    elif confirmes >=5:
        alerte="Orange"
        total_oranges += 1
    elif confirmes >=2:
        alerte="Jaune"
        total_jaunes += 1
    else:
        alerte="Vert"
        total_vertes += 1


    # # Accumulation des cas confirmés par départements
    if nom_department == "Cuvette":
        cas_cuvette += confirmes
    elif nom_department == "Likouala":
        cas_likouala += confirmes
    elif nom_department == "Plateaux":
        cas_plateaux += confirmes
    elif nom_department == "Pointe-Noire":
        cas_pointe_noire += confirmes
    elif nom_department == "Brazzaville":
        cas_brazzaville += confirmes

    departement_touche = "Cuvette"
    max_cas = cas_cuvette

    # Utilisation de structure conditionnelle pour trouver  les département le plus touchés
    if cas_likouala > max_cas:
        max_cas = cas_likouala
        departement_plus_touche = "Likouala"

    if cas_plateaux > max_cas:
        max_cas = cas_plateaux
        departement_plus_touche = "Plateaux"

    if cas_pointe_noire > max_cas:
        max_cas = cas_pointe_noire
        departement_plus_touche = "Pointe-Noire"

    if cas_brazzaville > max_cas:
        max_cas = cas_brazzaville
        departement_plus_touche = "Brazzaville"


    total_suspects+=suspects
    total_confirmes+=confirmes
    total_deces=total_deces+deces
    total_actifs += cas_actifs
    pourcentage = (max_cas / total_confirmes) * 100


    print(f"Alerte : {alerte}")
    print(f"Actifs : {cas_actifs}")
    print(f"letalités : {round(letalite,1)} % ")
    print()


print(f"="*50)
print(f"   RAPPORT NATIONNAL MPOX 2025   ")
print(f"="*50)
print(f"Districcts anlyses:{nb_districts}")
print(f"Total suspects : {total_suspects}")
print(f"Total confirmes : {total_confirmes}")
print(f"Total deces : {total_deces}")
print(f"Total actifs : {total_actifs}")
print(f"Zones Vertes : {total_vertes}")
print(f"Zones jaunes : {total_jaunes}")
print(f"Zones oranges : {total_oranges}")
print(f"Zones rouges : {total_rouges}")
print(f"="*50)

print()
print("=" * 50)
print(f"    Département le plus touché")
print(f"Département : {departement_touche}")
print(f"Cas confirmés : {max_cas}")
print(f"Pourcentage : {round(pourcentage, 2)} %")

