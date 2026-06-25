# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# ============================================================
print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()
#
nom_patient   = input('Nom du patient : ')
age_patient   = int(input('Age (annees) : '))
temperature   = float(input('Temperature (degres C, ex: 38.4) : '))
spo2          = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst  = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur       = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

# --- VALIDATION DES PLAGES (S2 + S3 : conditions simples) --
# Verifier que la temperature est dans une plage physiologiquement possible
if spo2 < 50 or spo2 > 100:
    print("ERREUR : SpO2 hors plage — verifier le capteur")

if tension_syst < 50 or tension_syst > 250:
    print("ERREUR : Tension hors plage — verifier le brassard")

if douleur < 0 or douleur > 10:
    print("ERREUR : Douleur doit etre entre 0 et 10")

if age_patient < 0 or age_patient > 120:
    print("ERREUR : Age invalide — verifier la saisie")


if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage  = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec      = '0 minute'
    action_triage  = 'Medecin present immediatement — code ROUGE active'
# Niveau 2 : URGENT — conditions moins critiques mais toujours urgentes
elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
    niveau_triage  = '2 — URGENT'
    couleur_triage = '[ORANGE]'
    delai_pec      = '< 10 minutes'
    action_triage  = 'Appel medecin senior'
# Niveau 3 : URGENT DIFFERE
elif temperature > 37.5 or douleur >6:
    niveau_triage  = '3 — URGENT DIFFERE'
    couleur_triage = '[JAUNE]'
    delai_pec      = '< 30 minutes'
    action_triage  = 'Infirmier — surveillance'
# Niveau 4 : MOINS URGENT (cas par defaut)
else:
    niveau_triage  = '4 — MOINS URGENT'
    couleur_triage = '[VERT]'
    delai_pec      = '< 120 minutes'
    action_triage  = "File d'attente standard"

if temperature > 39.5:
    motif = f"Temperature {temperature} C > seuil 39.5 C"
elif spo2 < 90:
    motif = f"SpO2 {spo2}% < seuil 90%"
elif tension_syst > 180:
    motif = f"Tension {tension_syst} mmHg > seuil 180"
else:
    motif = "Parametres stables"


# --- AFFICHAGE FICHE TRIAGE (S2 reutilise : f-strings) --
print()
print('=' * 55)
print(f'  RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)
#
print(f"PARAMETRES VITAUX")
print(f"Temperature: {temperature:.2f} C")
print(f"Spo2: {spo2:.2f} %")
print(f"Tension syst: {tension_syst:.2f} mmHg")
print(f"Douleur: {douleur:.2f} / 10 ")
print('-'*35)
print(f'NIVEAU DE TRIAGE : {niveau_triage}')
print(f'COULEUR TRIAGE : {couleur_triage}')
print(f'DELAI_PEC : {delai_pec}')
print(f'ACTION TRIAGE : {action_triage}')
print('-'*35)
print(f"Motif principal : {motif}")