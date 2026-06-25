# =============================================================
# AKEINI ACADEMY -Projet Santé Publique
# Semaine 2 - Exercice 2 : Projet Santé Publique
# Nom :Sacré OMBELE
# Date :Vendredi 19 juin 2026
# =============================================================

# Variables
# données brutes
budget_total_depense=87450000
consultation_externes=4823
nb_hospitalier =1247
nb_deces_hospitalier=18
lits_totaux = 180
lits_occupes_moyenne=143
medecins_permanents=22
infirmies_permanents=58
population_depart_kouilou = 128000
taux_change_eur_fcfa=655.957
taux_change_usd_fcfa=600.0

# A completer
# 1. Convension devices
con_euro = round(budget_total_depense / taux_change_eur_fcfa, 2)
con_usd = round(budget_total_depense / taux_change_usd_fcfa, 2)
#2. Indicateurs OMS
densite_medicale = round((medecins_permanents / population_depart_kouilou) * 1000,1) # Indicateur OMS 1
taux_mortalite = round((nb_deces_hospitalier / nb_hospitalier) * 100,1)# Indicateur OMS2
taux_occupation=(lits_occupes_moyenne*100)/lits_totaux # Indicateur OMS 3

# 3. Division entiere et modulo
budget_medicament = int(budget_total_depense * 0.35)
cout_jrnalier_medicament=450000
jr_rupture_stock=int(budget_medicament//cout_jrnalier_medicament)
jour_restants = budget_medicament % cout_jrnalier_medicament

# 4. Puissance pour projection
budget_n_plus_2=budget_total_depense*(1.08**2)

# ---AFFICHAGE RAPPORT
print(f"===RAPPORT TRIMESTRIEL Q4 2025 - Hopial General Pointe-Noire ===")
print(f"\t\tDépenses Q4 : {budget_total_depense:,} FCFA")
print(f"\t\tEn euros : {con_euro} EUR")
print(f"\t\tEn dollars : {con_usd} USD")
print(f"INDICATEURS OMS")
print(f"\t\tDensite medicale : {densite_medicale} [Noorme OMS : >= 2.3] ")
print(f"\t\tTaux mortalité {taux_mortalite}% [Seuil alerte : > 2%]")
print(f"\t\tTaux occupation: {taux_occupation}% [Optiomal : 70-85%]")

print(f"ANALYSE PHARMACHIE")
print(f"\t\tBudget médicaments : {budget_medicament:,} FCFA")
print(f"\t\tJours de stock : {jr_rupture_stock} jours ")
print(f"\t\tJours dépassement : {jour_restants} jours ")

print(f"PROJECTION")
print(f"\t\tBudget N+2(8%/an) : {budget_n_plus_2:,} FCFA")
print(f"\t\tALERTE Densité CRITIQUE (0.2 pour 1000 hab - norme OMS :2.3)")

