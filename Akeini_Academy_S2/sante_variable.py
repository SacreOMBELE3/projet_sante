# ============================================================
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metier
# ============================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ========
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0
SEUIL_OMS_DENSITE_MEDICALE = 2.3  # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0  # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30  # jours minimum de stock
DEPARTEMENTS_CONGO = [  # 12 departements officiels
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# === SECTION B : VARIABLES DES 5 HOPITAUX ===================
# Hopital 1 — CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1800000


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


# VARIABLES DES 5 MEDICAMENTS
med1_nom = "artemether-lumefantrine"
med1_quantite = 500
med1_seuil = 100
med1_cout = 250.0
med1_stock= med1_quantite * med1_cout


med2_nom = "amoxicilline"
med2_quantite = 300
med2_seuil = 100
med2_cout = 250.0
med2_stock= med2_quantite * med2_cout

med3_nom = "paracetamol"
med3_quantite = 570
med3_seuil = 100
med3_cout = 250.0
med3_stock=med3_quantite * med3_cout

med4_nom = "SRO"
med4_quantite = 80
med4_seuil = 100
med4_cout = 250.0
med4_stock=med4_quantite * med4_cout

med5_nom = "vaccin antipaludeen"
med5_quantite = 10
med5_seuil = 100
med5_cout = 250.0
med5_stock=med5_quantite * med5_cout


# CALCULS D'INITIALISATION
# Calcul de la densité médicale
# Formule : (nombre de médecins / population) × 1000
# # Calcul du taux d'occupation des lits


# Pour Hopital 1 — CHU de Brazzaville
h1_densite_medicale = (h1_nb_medecins / h1_population_zone) * 1000
h1_taux_occupation_moyen= (h1_nb_lits_occupes * 100) / h1_nb_lits

# Hopital General Pointe-Noire
h2_densite_medicale= (h2_nb_medecins / h2_population_zone) * 1000
h2_taux_occupation_moyen= (h2_nb_lits_occupes * 100) / h2_nb_lits

# Hopital Hopital de Dolisie
h3_densite_medicale= (h3_nb_medecins / h3_population_zone) * 1000
h3_taux_occupation_moyen= (h3_nb_lits_occupes * 100) / h3_nb_lits

# Owando
h4_densite_medicale= (h4_nb_medecins / h4_population_zone) * 1000
h4_taux_occupation_moyen= (h4_nb_lits_occupes * 100) / h4_nb_lits

#Imfondo
h5_densite_medicale= (h5_nb_medecins / h5_population_zone) * 1000
h5_taux_occupation_moyen= (h5_nb_lits_occupes * 100) / h5_nb_lits

#calcul valeur de stock et medecins total
valeur_stock = (med1_quantite * med1_cout + med2_quantite * med2_cout + med3_quantite * med3_cout + med4_quantite * med4_cout + med5_quantite * med5_cout)
total_medecins = (h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins)

total_population = ( h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone)

densite_nationale = (total_medecins / total_population) * 1000


# artemether-lumefantrine
if med1_stock <= med1_seuil:
    med1_statut = 'RUPTURE CRITIQUE'
    med1_couleur = '[ROUGE]'
    med1_action = 'Alerte immediate PNA — commande express sous 24h'

elif med1_stock <= med1_seuil * 1.5:
    med1_statut = 'ALERTE STOCK'
    med1_couleur = '[ORANGE]'
    med1_action = 'Commande urgente a declencher sous 72h'

elif med1_stock <= med1_seuil * 2.0:
    med1_statut = 'STOCK LIMITE'
    med1_couleur = '[JAUNE]'
    med1_action = 'Surveillance renforcee — planifier commande'

else:
    med1_statut = 'STOCK NORMAL'
    med1_couleur = '[VERT]'
    med1_action = 'Situation normale — suivi standard'


# amoxicilline
if med2_stock <= med2_seuil:
    med2_statut = 'RUPTURE CRITIQUE'
    med2_couleur = '[ROUGE]'
    med2_action = 'Alerte immediate PNA — commande express sous 24h'

elif med2_stock <= med2_seuil * 1.5:
    med2_statut = 'ALERTE STOCK'
    med2_couleur = '[ORANGE]'
    med2_action = 'Commande urgente a declencher sous 72h'

elif med2_stock <= med2_seuil * 2.0:
    med2_statut = 'STOCK LIMITE'
    med2_couleur = '[JAUNE]'
    med2_action = 'Surveillance renforcee — planifier commande'

else:
    med2_statut = 'STOCK NORMAL'
    med2_couleur = '[VERT]'
    med2_action = 'Situation normale — suivi standard'

# paracetamol

if med3_stock <= med3_seuil:
    med3_statut = 'RUPTURE CRITIQUE'
    med3_couleur = '[ROUGE]'
    med3_action = 'Alerte immediate PNA — commande express sous 24h'

elif med3_stock <= med3_seuil* 1.5:
    med3_statut = 'ALERTE STOCK'
    med3_couleur = '[ORANGE]'
    med3_action = 'Commande urgente a declencher sous 72h'

elif med3_stock <= med3_seuil * 2.0:
    med3_statut = 'STOCK LIMITE'
    med3_couleur = '[JAUNE]'
    med3_action = 'Surveillance renforcee — planifier commande'

else:
    med3_statut = 'STOCK NORMAL'
    med3_couleur = '[VERT]'
    med3_action = 'Situation normale — suivi standard'


# SPO
if med4_stock <= med4_seuil:
    med4_statut = 'RUPTURE CRITIQUE'
    med4_couleur = '[ROUGE]'
    med4_action = 'Alerte immediate PNA — commande express sous 24h'

elif med4_stock <= med4_seuil * 1.5:
    med4_statut = 'ALERTE STOCK'
    med4_couleur = '[ORANGE]'
    med4_action = 'Commande urgente a declencher sous 72h'

elif med4_stock <= med4_seuil * 2.0:
    med4_statut = 'STOCK LIMITE'
    med4_couleur = '[JAUNE]'
    med4_action = 'Surveillance renforcee — planifier commande'

else:
    med4_statut = 'STOCK NORMAL'
    med4_couleur = '[VERT]'
    med4_action = 'Situation normale — suivi standard'

# vaccin antipaludeen
if med5_stock <= med5_seuil:
    med5_statut = 'RUPTURE CRITIQUE'
    med5_couleur = '[ROUGE]'
    med5_action = 'Alerte immediate PNA — commande express sous 24h'

elif med5_stock <= med5_seuil * 1.5:
    med5_statut = 'ALERTE STOCK'
    med5_couleur = '[ORANGE]'
    med5_action = 'Commande urgente a declencher sous 72h'

elif med5_stock <= med5_seuil * 2.0:
    med5_statut = 'STOCK LIMITE'
    med5_couleur = '[JAUNE]'
    med5_action = 'Surveillance renforcee — planifier commande'

else:
    med5_statut = 'STOCK NORMAL'
    med5_couleur = '[VERT]'
    med5_action = 'Situation normale — suivi standard'

# Couverture vacinale
couverture_vacinale_bz=(418500/450000)*100
couverture_vacinale_pn=(229600/280000)*100
couverture_vacinale_pl=(54000/120000)*100
couverture_vacinale_sga=(35700/85000)*100

# RAPPORT D'INVENTAIRE =======================
print(f'='*35)
print(f"RAPPOORT D'INVENTAIRE PAR HOPITAL")
print(f'='*35)
print("")

print(f'-'*35)
print(f"L'Hopital de {h1_nom} dans la ville de {h1_ville}")
print(f"\t\tLa densite medicale est {h1_densite_medicale:.2f} medecins/1000 habitants")
print(f"\t\tLe taux d'occupation est {h1_taux_occupation_moyen}%")
print(f'-'*35)

print(f"L'Hopital de {h2_nom} dans la ville de {h2_ville}")
print(f"\t\tLa densite est {h2_densite_medicale:.2f} medecins/1000 habitants")
print(f"\t\tLe taux d'occupation est {h2_taux_occupation_moyen:.2f}%")
print(f'-'*35)


print(f"L'Hopital de {h3_nom} dans la ville de {h3_ville}")
print(f"\t\tLa densite de {h3_densite_medicale:.2f} medecins/1000 habitants")
print(f"\t\tle taux d'occupation de {h3_taux_occupation_moyen}%")

print(f'-'*35)


print(f"L'Hopital de {h4_nom} dans la ville de {h4_ville}")
print(f"\t\tLa densite est {h4_densite_medicale:.2f} medecins/1000 habitants")
print(f"\t\tLe taux d'occupation est {h4_taux_occupation_moyen:.2f}%")

print(f'-'*35)


print(f"L'Hopital de {h5_nom} dans la ville de {h5_ville}")
print(f"\t\tLa densite de {h5_densite_medicale:.2f} medecins/1000 habitants")
print(f"\t\tle taux d'occupation de {h5_taux_occupation_moyen}%")
print(f'-'*35)

# Alerte
print(f'{med1_couleur} {med1_nom}')
print(f'\t\tStock : {med1_stock} unites | Seuil : {med1_seuil}')
print(f'\t\tStatut : {med1_statut}')
print(f'\t\tAction : {med1_action}')
print(f'-'*35)

print(f'{med2_couleur} {med2_nom}')
print(f'\t\tStock : {med2_stock} unites | Seuil : {med2_seuil}')
print(f'\t\tStatut : {med2_statut}')
print(f'\t\tAction : {med2_action}')
print(f'-'*35)

print(f'{med3_couleur} {med3_nom}')
print(f'\t\tStock : {med3_stock} unites | Seuil : {med3_seuil}')
print(f'\t\tStatut : {med3_statut}')
print(f'\t\tAction : {med3_action}')
print(f'-'*35)

print(f'{med4_couleur} {med4_nom}')
print(f'\t\tStock : {med4_stock} unites | Seuil : {med4_seuil}')
print(f'\t\tStatut : {med4_statut}')
print(f'\t\tAction : {med4_action}')
print(f'-'*35)

print(f'{med5_couleur} {med5_nom}')
print(f'\t\tStock : {med5_stock} unites | Seuil : {med5_seuil}')
print(f'\t\tStatut : {med5_statut}')
print(f'\t\tAction : {med5_action}')
print(f'-'*35)


print("")
print(f"\n===== KPI GLOBAUX =====")
print(f"\t\tDensite medicale nationale : {densite_nationale:.2f} medecins/1000 habitants")
print(f"\t\tValeur totale du stock : {valeur_stock:,.0f} FCFA")

print(f'-'*35)
if couverture_vacinale_bz < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Brazzaville : ZONE INSUFFISANTE ")
elif couverture_vacinale_bz >= 80 and couverture_vacinale_bz < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Brazzaville : ZONE A RISQUE  ")
else :
    print(f"Brazzaville : ZONE CRITIQUE")

print(f'-'*35)
if couverture_vacinale_pn < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Pointe-Noire : ZONE INSUFFISANTE ")
elif couverture_vacinale_pn >= 80 and couverture_vacinale_pn < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Pointe-Noire : ZONE A RISQUE  ")
else :
    print(f"Pointe-Noire : ZONE CRITIQUE")

print(f'-'*35)
if couverture_vacinale_pl < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Pool : ZONE INSUFFISANTE ")
elif couverture_vacinale_pl  >= 80 and couverture_vacinale_pl < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Pool : ZONE A RISQUE  ")
else :
    print(f"Pool : ZONE CRITIQUE")

print(f'-'*35)
if couverture_vacinale_sga < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Sangha : ZONE INSUFFISANTE ")
elif couverture_vacinale_sga >= 80 and couverture_vacinale_sga < SEUIL_OMS_COUVERTURE_VACCIN:
    print(f"Sangha : ZONE A RISQUE  ")
else :
    print(f"Sangha : ZONE CRITIQUE")
