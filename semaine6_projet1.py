
departements = []

def donnees():
    compteur = 0
    while compteur < 2:
        compteur += 1
        nom_departement = input("Nom du département : ").lower()

        nb_etablissement = int(input("Nombre d'établissements : "))

        nb_eleves_garcons = int(input("Nombre d'élèves garçons : "))
        nb_eleves_filles = int(input("Nombre d'élèves filles : "))

        nb_enseignant_hommes = int(input("Nombre d'enseignants hommes : "))
        nb_enseignant_femmes = int(input("Nombre d'enseignants femmes : "))

        nb_personnel_admin = int(input("Nombre de personnel administratif : "))


        nb_salle_bon_etat = int(input("Nombre de salles en bon état : "))
        nb_mauvais_etat = int(input("Nombre de mauvaises : "))
        nb_papaing=int(input("Nombre de papaing : "))

        departement = {
            "nom": nom_departement,
            "etablissements": nb_etablissement,
            "garcons": nb_eleves_garcons,
            "filles": nb_eleves_filles,
            "enseignants_hommes": nb_enseignant_hommes,
            "enseignants_femmes": nb_enseignant_femmes,
            "personnel_admin": nb_personnel_admin,
            "salles en mauvais etat ": nb_mauvais_etat,
            "salle en papaing": nb_papaing,
            "salles_bonnes": nb_salle_bon_etat
        }


        departements.append(departement)
        print("Département ajouté avec succès !")
def afficher_departements():

    if len(departements) == 0:
        print("Aucun département enregistré")
        return

    for dep in departements:
        print("--------------------")
        print("Département :", dep["nom"])
        print("Etablissements :", dep["etablissements"])
        print("Élèves garçons :", dep["garcons"])
        print("Élèves filles :", dep["filles"])
        print("Enseignants hommes :", dep["enseignants_hommes"])
        print("Enseignants femmes :", dep["enseignants_femmes"])
        print("Personnel administratif :", dep["personnel_admin"])
        print("Salles en bon état :", dep["salles_bonnes"])
        print("Salles en mauvais état :", dep["salles en mauvais etat "])
        print("Salles en papaing :", dep["salle en papaing"])



def statistiques_departement():

    nom_recherche = input("Entrer le nom du département : ").lower()

    trouve = False

    for departement in departements:

        if departement["nom"] == nom_recherche:
            print("===== STATISTIQUES DU DEPARTEMENT =====")
            print("Département :", departement["nom"])
            print("Nombre d'établissements :", departement["etablissements"])

            total_eleves = departement["garcons"] + departement["filles"]
            print("Nombre total d'apprenants :", total_eleves)

            total_enseignants = (
                    departement["enseignants_hommes"]
                    + departement["enseignants_femmes"]
            )

            print("Nombre total d'enseignants :", total_enseignants)
            print("Personnel administratif :", departement["personnel_admin"])

            total_salles = (departement["salles_bonnes"]
                           + departement["salles en mauvais etat "]
                           + departement["salle en paging"])
            print("Salles en bon état :", total_salles)


            trouve = True

    if trouve == False:
        print("Département introuvable")



def total_apprenants():

    total_App = 0

    for departement in departements:

        total_App += departement["garcons"] + departement["filles"]

    print("Nombre total d'apprenants :", total_App)
def total_enseignants():

    total_Ens = 0

    for departement in departements:

        total_Ens += (
            departement["enseignants_hommes"]
            + departement["enseignants_femmes"]
        )

    print("Nombre total d'enseignants :", total_Ens)

def total_salles():
    total_sal=0
    for departement in departements:
        total_sal += (departement["salles_bonnes"]
                      +departement["salles en paping"]
                      + departement["salles en mauvais etat"])
    print("Nombre total de salles :",total_sal)

def comparaison_public_prive():

    total_public = 0
    total_prive = 0

    for departement in departements:

        total_public += departement["public"]
        total_prive += departement["prive"]

    print("===== COMPARAISON PUBLIC / PRIVE =====")
    print("Total établissements publics :", total_public)
    print("Total établissements privés :", total_prive)

    if total_public > total_prive:
        print("Les établissements publics sont plus nombreux.")

    elif total_prive > total_public:
        print("Les établissements privés sont plus nombreux.")

    else:
        print("Le nombre d'établissements publics et privés est égal.")

def comparaison_urbain_rural():

    total_urbain = 0
    total_rural = 0

    for departement in departements:

        total_urbain += departement["urbain"]
        total_rural += departement["rural"]

    print("===== COMPARAISON URBAIN / RURAL =====")
    print("Total établissements urbains :", total_urbain)
    print("Total établissements ruraux :", total_rural)

    if total_urbain > total_rural:
        print("Les établissements urbains sont plus nombreux.")

    elif total_rural > total_urbain:
        print("Les établissements ruraux sont plus nombreux.")

    else:
        print("Le nombre d'établissements urbains et ruraux est égal.")

def departement_plus_apprenants():

    if len(departements) == 0:
        print("Aucun département enregistré")
        return

    meilleur_departement = departements[0]

    for departement in departements:

        total_apprenants = departement["garcons"] + departement["filles"]

        total_meilleur = (
            meilleur_departement["garcons"]
            + meilleur_departement["filles"]
        )

        if total_apprenants > total_meilleur:
            meilleur_departement = departement


    print("===== DEPARTEMENT AVEC LE PLUS D'APPRENANTS =====")
    print("Département :", meilleur_departement["nom"])

    print(
        "Nombre d'apprenants :",
        meilleur_departement["garcons"]
        + meilleur_departement["filles"]
    )

def departement_plus_centres():

    if len(departements) == 0:
        print("Aucun département enregistré")
        return

    meilleur_departement = departements[0]

    for departement in departements:

        if departement["etablissements"] > meilleur_departement["etablissements"]:
            meilleur_departement = departement


    print("===== DEPARTEMENT AVEC LE PLUS DE CENTRES =====")
    print("Département :", meilleur_departement["nom"])
    print("Nombre de centres :", meilleur_departement["etablissements"])

def rapport():

    if len(departements) == 0:
        print("Aucun département enregistré")
        return


    total_etab = 0
    total_eleves = 0
    total_enseignants = 0
    total_salles = 0


    for departement in departements:

        total_etab += departement["etablissements"]

        total_eleves += (
            departement["garcons"]
            + departement["filles"]
        )

        total_enseignants += (
            departement["enseignants_hommes"]
            + departement["enseignants_femmes"]
        )

        total_salles += (departement["salles_bonnes"]
                       + departement["salles_mauvaises"]
                      +departement["salle en papaing"])


    print("\n========== RAPPORT GENERAL ==========")

    print("Nombre de départements :", len(departements))

    print("Total établissements :", total_etab)

    print("Total apprenants :", total_eleves)

    print("Total enseignants :", total_enseignants)

    print("Total salles :", total_salles)


    print("\n===== DÉTAIL DES DÉPARTEMENTS =====")

    for departement in departements:

        print("-------------------------")
        print("Département :", departement["nom"])
        print("Établissements :", departement["etablissements"])

        print(
            "Apprenants :",
            departement["garcons"] + departement["filles"]
        )

        print(
            "Enseignants :",
            departement["enseignants_hommes"]
            + departement["enseignants_femmes"]
        )

        total_salles +=(departement["salles_bonnes"]
                       + departement["salles en mauvais etat "]
                      + departement["salles en paping"]
                      )
        print("Nombre total de salles :", total_salles)
donnees()
afficher_departements()
statistiques_departement()
total_apprenants()
total_enseignants()
total_salles()
departement_plus_centres()
rapport()