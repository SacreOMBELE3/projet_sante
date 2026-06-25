# === SECTION B : VARIABLES DES 5 HOPITAUX ===================
# Hopital 1 — CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 298
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1800000
h1_med_rupture = 2
h1_med_alerte=2
h1_taux_occupation_moyen=(h1_nb_lits_occupes*100)/h1_nb_lits


# Hopital 2 — Hopital General Pointe-Noire
h2_nom = "Hopital General Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Pointe-Noire"
h2_type = "Hopital General"
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 128000
h2_med_rupture = 0
h2_med_alerte = 1
h2_taux_occupation_moyen=(h2_nb_lits_occupes*100)/h2_nb_lits


# Hopital 3 — Hopital de Dolisie
h3_nom = "Hopital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hopital Regional"
h3_nb_lits = 120
h3_nb_lits_occupes = 95
h3_nb_medecins = 15
h3_nb_infirmiers = 40
h3_population_zone = 95000
h3_med_rupture = 1
h3_med_alerte = 2
h3_taux_occupation_moyen=(h3_nb_lits_occupes*100)/h3_nb_lits

# Hopital 4 — Hopital de District Owando
h4_nom = "Hopital de District Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "Hopital District"
h4_nb_lits = 80
h4_nb_lits_occupes = 60
h4_nb_medecins = 10
h4_nb_infirmiers = 25
h4_population_zone = 70000
h4_med_rupture = 3
h4_med_alerte = 0
h4_taux_occupation_moyen=(h4_nb_lits_occupes*100)/h4_nb_lits

# Hopital 5 — Centre de Sante Impfondo
h5_nom = "Centre de Sante Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de Sante"
h5_nb_lits = 40
h5_nb_lits_occupes = 25
h5_nb_medecins = 4
h5_nb_infirmiers = 12
h5_population_zone = 35000
h5_med_rupture = 2
h5_med_alerte = 1
h5_taux_occupation_moyen=(h5_nb_lits_occupes*100)/h5_nb_lits

nb_repture=h1_med_rupture+h2_med_rupture+h3_med_rupture+h4_med_rupture+h5_med_rupture

print(f" HOPITAL\t\t\tOCCUPATION   ALERTES    NIVEAU GLOBAL")


if h1_med_rupture >= 2 or h1_taux_occupation_moyen > 95:
    print(f" CHU Brazzaville            {h1_taux_occupation_moyen:.2f}% [ALT]  2R + 2A    [CRITIQUE]")
elif h1_med_rupture >= 1 or h1_taux_occupation_moyen > 85 or (h1_med_alerte >= 2 and h1_nb_medecins < 5):
    print(f"CHU Brazzaville            {h1_taux_occupation_moyen:.2f}% [ALT]  2R + 2A    [PREOCCUPANT]")
else:
    print(f"CHU Brazzaville\t\t\t{h1_taux_occupation_moyen:.2f}% [ALT]  2R + 2A    [SATISFAISANT]")


if h2_med_rupture >= 2 or h2_taux_occupation_moyen > 95:
    print(f" Hopital Pointe-Noire\t\t\t{h2_taux_occupation_moyen:.2f}% [ALT]  0R + 1A   [CRITIQUE]")
elif h2_med_rupture >= 1 or h2_taux_occupation_moyen > 85 or (h2_med_alerte >= 2 and h2_nb_medecins < 5):
    print(f"Hopital Pointe-Noire\t\t\t{h2_taux_occupation_moyen:.2f}% [ALT]  0R + 1A    [PREOCCUPANT]")
else:
    print(f"Hopital Pointe-Noire\t\t\t{h2_taux_occupation_moyen:.2f}% [ALT]  0R + 1A    [SATISFAISANT]")


if h3_med_rupture >= 2 or h3_taux_occupation_moyen > 95:
    print(f"  Hopital Dolisie\t\t\t{h3_taux_occupation_moyen:.2f}% [ALT]   1R + 2A   [CRITIQUE]")
elif h3_med_rupture >= 1 or h3_taux_occupation_moyen > 85 or (h3_med_alerte >= 2 and h3_nb_medecins < 5):
    print(f" Hopital Dolisie\t\t\t{h3_taux_occupation_moyen:.2f}% [ALT]   1R + 2A    [PREOCCUPANT]")
else:
    print(f" Hopital Dolisie\t\t\t{h3_taux_occupation_moyen:.2f}% [ALT]   1R + 2A    [SATISFAISANT]")


if h4_med_rupture >= 2 or h4_taux_occupation_moyen > 95:
    print(f" Hopital Owando\t\t\t{h4_taux_occupation_moyen:.2f}% [ALT]  3R + 0A   [CRITIQUE]")
elif h4_med_rupture >= 1 or h4_taux_occupation_moyen > 85 or (h4_med_alerte >= 2 and h4_nb_medecins < 5):
    print(f" Hopital Owando\t\t\t{h4_taux_occupation_moyen:.2f}% [ALT]  3R + 0A    [PREOCCUPANT]")
else:
    print(f" Hopital Owando\t\t\t{h4_taux_occupation_moyen:.2f}% [ALT]  3R + 0A   [SATISFAISANT]")


if h5_med_rupture >= 2 or h5_taux_occupation_moyen > 95:
    print(f" CMS Impfondo\t\t\t{h5_taux_occupation_moyen:.2f}% [ALT]  2R + 1A   [CRITIQUE]")
elif h5_med_rupture >= 1 or h5_taux_occupation_moyen > 85 or (h5_med_alerte >= 2 and h5_nb_medecins < 5):
    print(f"CMS Impfondo\t\t\t{h5_taux_occupation_moyen:.2f}% [ALT]  2R + 1A     [PREOCCUPANT]")
else:
    print(f"CMS Impfondo\t\t\t{h5_taux_occupation_moyen:.2f}% [ALT]  2R + 1A     [SATISFAISANT]")

print(f" 3 hopitaux sur 5 en situation CRITIQUE")
print(f"{nb_repture} ruptures de stock identifiees a l'echelle nationale")
print(f" RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA")