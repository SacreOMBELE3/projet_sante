from Akeini_Academy_S4.semaine4_exercice1_mpox import pourcentage

departements = []

def donnees():
    """ Cette fonction permet de saisir les données des départements.
    Elle demande à l'utilisateur d'entrer le nom du département,
    le nombre d'établissements, le nombre d'élèves garçons et filles,
    le nombre d'enseignants hommes et femmes, le nombre de personnel administratif,
    le nombre de salles en bon état,
    le nombre de salles en mauvais état et le nombre de salles en papaing.
    Les données sont ensuite stockées dans un dictionnaire et ajoutées à la liste des départements."""
    compteur = 0
    while compteur < 2:
        compteur += 1
        while True:
            try:
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
                break
            except ValueError:
                print("Erreur : Veuillez entrer des valeurs numériques valides.")

def afficher_departements():
    """ Cette fonction affiche les informations de tous les départements enregistrés."""

    if len(departements) == 0:
        print("Aucun département enregistré")
        return

    for departement in departements:
        print("--------------------")
        print("Département :", departement["nom"])
        print("Etablissements :", departement["etablissements"])
        print("Élèves garçons :", departement["garcons"])
        print("Élèves filles :", departement["filles"])
        print("Enseignants hommes :", departement["enseignants_hommes"])
        print("Enseignants femmes :", departement["enseignants_femmes"])
        print("Personnel administratif :", departement["personnel_admin"])
        print("Salles en bon état :", departement["salles_bonnes"])
        print("Salles en mauvais état :", departement["salles en mauvais etat "])
        print("Salles en papaing :", departement["salle en papaing"])



def statistiques_departement():
    """Cette fonction permet de calculer les statistiques d'un département."""

    if len(departements) == 0:
        print("Aucun département enregistré")
        return

    for departement in departements:
        total_apprenants = departement["garcons"] + departement["filles"]
        total_enseignants = (
            departement["enseignants_hommes"]
            + departement["enseignants_femmes"]
        )
        total_salles = (
            departement["salles_bonnes"]
            + departement["salles en mauvais etat "]
            + departement["salle en papaing"]
        )
        pourcentage_enseignants_hommes=(total_enseignants/departement["enseignants_hommes"])*100
        pourcentage_enseignants_femmes=(total_enseignants/departement["enseignants_femmes"])*100
        pourcentage_salles_bon_etat=(total_salles/departement["Salles_bonnes"])*100
        pourcentage_salles_mauvais_etat = (total_salles / departement["salles en mauvais etat "]) * 100
        pourcentage_salles_papaing = (total_salles / departement["salle en papaing"]) * 100

        print("--------------------")
        print("Département :", departement["nom"])
        print("Total d'apprenants :", total_apprenants)
        print("Total d'enseignants :", total_enseignants)
        print("Pourcentage d'enseignants hommes : {:.2f}%".format(pourcentage_enseignants_hommes))
        print("Pourcentage d'enseignants femmes : {:.2f}%".format(pourcentage_enseignants_femmes))
        print("Total de salles :", total_salles)
        print("Pourcentage de salles en bon état : {:.2f}%".format(pourcentage_salles_bon_etat))
        print("Pourcentage de salles en mauvais état : {:.2f}%".format(pourcentage_salles_mauvais_etat))
        print("Pourcentage de salles en papaing : {:.2f}%".format(pourcentage_salles_papaing))


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
                      +departement["salles en papaing"]
                      + departement["salles en mauvais etat"])
    print("Nombre total de salles :",total_sal)

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
                       + departement["salles en mauvais etat"]
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

def classement_par_departement():

    # Trier les départements par nombre d'apprenants
    departements_tries = sorted(departements, key=lambda x: x["garcons"] + x["filles"], reverse=True)

    print("\n========== CLASSEMENT PAR DÉPARTEMENT ==========")
    for i, departement in enumerate(departements_tries, start=1):
        total_apprenants = departement["garcons"] + departement["filles"]
        print("{}. {}: {} apprenants".format(i, departement["nom"], total_apprenants))



# Appel des fonctions
donnees()
afficher_departements()
statistiques_departement()
total_apprenants()
total_enseignants()
total_salles()
departement_plus_centres()
rapport()