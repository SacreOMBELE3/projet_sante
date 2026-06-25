# =============================================================
# AKEINI ACADEMY -Projet Santé Publique
# Semaine 2 - Exercice 1 : Fiche Patient CHU Brazzaville
# Sacré OMBELE
# Date :Vendredi 19 juin 2026
# =============================================================

# section 1
nom_patient=input('Nom du patient: ')
age_patient=int(input('Age : '))
sexe_patient=input('Sexe : ')
departement_patient=input('Departement : ')
couverture_sociale=input('Couverture sociale : ')
type_consultation=input('Type consultation sociale : ')
diagnostic_principal=input('Diagnostic principal : ')

# section 2
cout_consultation_fcfa=15000.0
nb_consultation=1
remise_cnss_pct=30.0

# section 3
nom_hopital="CHU de Brazzaville"
ville_hopital="Brazzaville"
nb_lits_total=320
nb_lits_occupes=284
nb_medecins_actifs=47
nb_consultations_hopital = 120
cout_total_fcfa = cout_consultation_fcfa * nb_consultation * (1 - remise_cnss_pct / 100)
cout_occupation_pct=round((nb_lits_occupes/nb_lits_total)*100,1)
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)

print("=============================================================")
print(f"FICHE PATIENT - {nom_patient}")
print("=============================================================")
print(f"Age: {age_patient} ans")
print(f"Sexe: {sexe_patient}")
print(f"Département: {departement_patient}")
print(f"Couverture sociale: {couverture_sociale}")

print("---------------------------------------------------------------")
print("CONSULTATION")
print(f"Type: {type_consultation}")
print(f"Diagnostic : {diagnostic_principal}")
print(f"Cout unitaire : {cout_consultation_fcfa} FCFA")
print(f"Rémise CNSS : {remise_cnss_pct}%")
print(f"COUT TOTAL : {cout_total_fcfa} FCFA")
print("---------------------------------------------------------------")

print(f"HOPITAL : {nom_hopital}")
print(f"Ville  : {ville_hopital}")
print(f"Lits occupés : {nb_lits_occupes} / {nb_lits_total} ({cout_occupation_pct}%)")
print(f"Ratio consult : {ratio_consultations_medecin}")

print("=============================================================")
print("STATUT : Prise en charge validée")
print("=============================================================")
