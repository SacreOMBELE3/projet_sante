# Variable CMS de Kinkala
budget_tri_Ki=12500000
consultation_ex_ki=1847
hopitalisations_ki=312
deces_hopi_ki=8
lits_totaux_ki=45
lits_occupe_ki=41
medecins_permanents_ki=3
population_dessive_ki=85000
patient_ki=consultation_ex_ki+hopitalisations_ki
moyenne_ki=budget_tri_Ki/patient_ki
taux_occupation_ki=(lits_occupe_ki*100)/lits_totaux_ki
lits_totaux_ki=(lits_totaux_ki*100)/lits_totaux_ki
taux_mortalite_ki=(deces_hopi_ki*100)/hopitalisations_ki
densite_medicale_ki = round((medecins_permanents_ki / population_dessive_ki) * 1000,2)

# Variable CMS de Vindza
budget_tri_Vi=6800000
consultation_ex_Vi=923
hopitalisations_Vi=87
deces_hopi_Vi=2
lits_totaux_Vi=20
lits_occupe_Vi=14
medecins_permanents_Vi=1
population_dessive_Vi=42000
patient_Vi=consultation_ex_Vi+hopitalisations_Vi
moyenne_Vi=budget_tri_Vi/patient_Vi
taux_occupation_Vi=(lits_occupe_Vi*100)/lits_totaux_Vi
taux_mortalite_Vi=(deces_hopi_Vi*100)/hopitalisations_Vi
densite_medicale_Vi = round((medecins_permanents_Vi / population_dessive_Vi) * 1000,2)

# Variable Kindamba
budget_tri_Kin=9200000
consultation_ex_kin=1234
hopitalisations_kin=201
deces_hopi_kin=11
lits_totaux_kin=35
lits_occupe_kin=33
medecins_permanents_kin=2
population_dessive_kin=67000
patient_kin=consultation_ex_kin+hopitalisations_kin
moyenne_kin=budget_tri_Kin/patient_kin
taux_occupation_Kin=(lits_occupe_kin*100)/lits_totaux_kin
taux_mortalite_kin=(deces_hopi_kin*100)/hopitalisations_kin
densite_medicale_kin = round((medecins_permanents_kin / population_dessive_kin) * 1000,2)

#Affichage le titre du rapport
print()
print()
print("======================================================================================================")
print(f"\t\t\t\t\t===RAPPORT COMPARATIF URGENT DES HOPITAUX - KINKALA - CMS de Vindza - KINDAMBA===")
print("======================================================================================================")
print("")

#Affichage le rapport de Kinkala
print("======================================================================================================")
print(f"\t\t\t\t\t===RAPPORT D'HOPITAL KINKALA===")
print("======================================================================================================")
print("")
print(f"\t\t\t\tBUDGET TRIMESTRIEL: {budget_tri_Ki:,} FCFA")
print(f"\t\tINDICATEUR OMS")
print(f"\t\t\t\tDensité medicale : {densite_medicale_ki:.2f}%")
print(f"\t\t\t\tTaux mortalité : {taux_mortalite_ki:.2f}%")
print(f"\t\t\t\tTaux occupation {taux_occupation_ki:.2f}%")
print(f"\t\t\t\tMoyenne medicale : {moyenne_ki:.2f}%")
print("-------------------------------------------")
print("")

# Affichage le rapport de cms de Vindza
print("======================================================================================================")
print(f"\t\t\t\t\t===RAPPORT DE CMS de VINDZA===")
print("======================================================================================================")
print("")
print(f"\t\t\t\tBUDGET TRIMESTRIEL: {budget_tri_Vi:,} FCFA")
print(f"\t\tINDICATEUR OMS")
print(f"\t\t\t\tDensité medicale : {densite_medicale_Vi:.2f}%")
print(f"\t\t\t\tTaux mortalité : {taux_mortalite_Vi:.2f}%")
print(f"\t\t\t\tTaux occupation {taux_occupation_Vi:.2f}%")
print(f"\t\t\t\tMoyenne medicale : {moyenne_Vi:.2f}%")
print("-------------------------------------------")
print("")

# Affichage le rapport de cms de kindamba
print("======================================================================================================")
print(f"\t\t\t\t\t===RAPPORT DE CMS de KINDAMBA===")
print("======================================================================================================")
print("")
print(f"\t\t\t\tBUDGET TRIMESTRIEL: {budget_tri_Kin:,} FCFA")
print(f"\t\tINDICATEUR OMS")
print(f"\t\t\t\tDensité medicale : {densite_medicale_kin:.2f}%")
print(f"\t\t\t\tTaux mortalité : {taux_mortalite_kin:.2f}%")
print(f"\t\t\t\tTaux occupation {taux_occupation_Kin:.2f}%")
print(f"\t\t\t\tMoyenne medicale : {moyenne_kin:.2f}%")
print("-------------------------------------------")
print("")

# Verification d'hopital en critique
if taux_mortalite_ki > 2 or densite_medicale_ki < 0.05:
    print("Kinkala : CRITIQUE")

if taux_mortalite_Vi > 2 or densite_medicale_Vi < 0.05:
    print("Vindza : CRITIQUE")

if taux_mortalite_kin > 2 or densite_medicale_kin < 0.05:
    print("Kindamba : CRITIQUE")