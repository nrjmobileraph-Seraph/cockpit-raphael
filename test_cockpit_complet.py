#!/usr/bin/env python3
"""
TEST COMPLET DU COCKPIT PATRIMONIAL RAPHAEL
============================================
Verifie TOUTES les variables, calculs, coherences.
Genere un rapport detaille.
"""
import sys, os, math
from datetime import datetime, date

# --- CANON FINANCIER ---
CANON = {
    'date_naissance': '1975-08-26',
    'age_cible': 92,
    'capital_cible': 50000,
    'rail_mensuel': 2500,
    'rail_plancher': 2200,
    'rail_bonus': 2700,
    'aah_mensuel': 625,  # 2026
    'aah_plein': 1033,
    'loyer_net': 325,    # Parents (sortie) — loyer LMNP pas encore actif
    'rendement_annuel': 0.0345,
    'taux_mdph': 75,
    'parents_mensuel': 325,
    'capital_total_canon': 454000,
    # Poches
    'cc': 22732, 'livret_a': 22950, 'ldds': 12000, 'lep': 10000,
    'av1': 130000, 'av2': 130000, 'av3': 148550,
    'av4': 0, 'av5': 0, 'pea': 0, 'crypto': 0,
    # Taux livrets
    'taux_lep': 0.025, 'taux_la': 0.015, 'taux_ldds': 0.015,
    # Flux prevus
    'av_jeanluc': 23400,
    'sci_nette': 296100,
    'succession_hors_av': 182900,
    'vente_kleber': 202000,
    'donation_usufruit': 3349,
    'travaux_meylan': 33000,
    'mobilier_lmnp': 10000,
}

# --- RESULTATS ---
resultats = []
nb_ok = 0
nb_ko = 0
nb_warn = 0

def ok(test, detail=""):
    global nb_ok
    nb_ok += 1
    resultats.append(("OK", test, detail))

def ko(test, detail=""):
    global nb_ko
    nb_ko += 1
    resultats.append(("ERREUR", test, detail))

def warn(test, detail=""):
    global nb_warn
    nb_warn += 1
    resultats.append(("ATTENTION", test, detail))

print("=" * 70)
print("  TEST COMPLET COCKPIT PATRIMONIAL RAPHAEL")
print("  Date : " + datetime.now().strftime("%d/%m/%Y %H:%M"))
print("=" * 70)

# ================================================================
# 1. CONNEXION BASE DE DONNEES
# ================================================================
print("\n[1] CONNEXION BASE DE DONNEES...")
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import db_wrapper
    db = db_wrapper.connect()
    cur = db.cursor()
    ok("Connexion base OK")
except Exception as e:
    ko("Connexion base", str(e))
    print("FATAL : impossible de se connecter. Arret.")
    sys.exit(1)

# ================================================================
# 2. TABLE PROFIL — TOUTES LES VARIABLES
# ================================================================
print("\n[2] VERIFICATION TABLE PROFIL...")
cur.execute("SELECT * FROM profil LIMIT 1")
profil_row = cur.fetchone()
if profil_row:
    profil = dict(profil_row)
    ok("Table profil existe et contient des donnees")

    champs_requis = [
        'date_naissance', 'age_cible', 'capital_cible', 'taux_mdph',
        'aah_mensuel', 'pch_mensuel', 'loyer_net', 'rail_mensuel',
        'rendement_annuel', 'rvd_mensuel', 'aspa_mensuelle',
        'revenus_pro', 'autres_rentes', 'mdph_80plus'
    ]
    for c in champs_requis:
        if c in profil:
            ok(f"  profil.{c} = {profil[c]}")
        else:
            ko(f"  profil.{c} MANQUANT")

    # Verifier coherence valeurs
    if profil.get('age_cible') == 92:
        ok("  age_cible = 92 (canon)")
    else:
        ko(f"  age_cible = {profil.get('age_cible')} (attendu 92)")

    if profil.get('rail_mensuel') == 2500:
        ok("  rail_mensuel = 2500 (canon)")
    else:
        warn(f"  rail_mensuel = {profil.get('rail_mensuel')} (canon = 2500)")

    if abs(profil.get('rendement_annuel', 0) - 0.0345) < 0.001:
        ok(f"  rendement_annuel = {profil.get('rendement_annuel')} (canon 3.45%)")
    else:
        warn(f"  rendement_annuel = {profil.get('rendement_annuel')} (canon = 0.0345)")

    if profil.get('capital_cible') == 50000:
        ok("  capital_cible = 50000 (canon)")
    else:
        ko(f"  capital_cible = {profil.get('capital_cible')} (attendu 50000)")
else:
    ko("Table profil VIDE")
    profil = {}

# ================================================================
# 3. TABLE CAPITAL — TOUTES LES POCHES
# ================================================================
print("\n[3] VERIFICATION TABLE CAPITAL...")
cur.execute("SELECT * FROM capital ORDER BY id DESC LIMIT 1")
cap_row = cur.fetchone()
if cap_row:
    cap = dict(cap_row)
    ok("Table capital existe et contient des donnees")

    poches = ['cc', 'livret_a', 'ldds', 'lep', 'av1', 'av2', 'av3']
    for p in poches:
        if p in cap:
            ok(f"  capital.{p} = {cap[p]:,.0f} EUR")
        else:
            ko(f"  capital.{p} MANQUANT")

    # Nouvelles poches
    for p in ['av4', 'av5', 'pea', 'crypto']:
        if p in cap:
            ok(f"  capital.{p} = {cap[p]:,.0f} EUR (nouvelle poche)")
        else:
            warn(f"  capital.{p} MANQUANT (ajoutee recemment)")

    # Capital total
    total = sum(cap.get(k, 0) for k in poches)
    canon_total = sum(CANON[k] for k in poches)
    if abs(total - canon_total) < 100:
        ok(f"  Capital total = {total:,.0f} EUR (canon {canon_total:,.0f})")
    else:
        warn(f"  Capital total = {total:,.0f} EUR (ecart {total - canon_total:+,.0f} vs canon {canon_total:,.0f})")

    # Metadonnees AV
    for av in ['av1', 'av2', 'av3']:
        for meta in ['date_ouverture', 'versements', 'rendement']:
            key = f'{av}_{meta}'
            if key in cap:
                ok(f"  capital.{key} = {cap[key]}")
            else:
                warn(f"  capital.{key} MANQUANT")
else:
    ko("Table capital VIDE")
    cap = {}

# ================================================================
# 4. TABLE CHRONOLOGIE
# ================================================================
print("\n[4] VERIFICATION TABLE CHRONOLOGIE...")
cur.execute("SELECT COUNT(*) as n FROM chronologie")
row = cur.fetchone()
nb_chrono = dict(row)['n'] if row else 0
if nb_chrono > 0:
    ok(f"Table chronologie : {nb_chrono} actions")
    cur.execute("SELECT * FROM chronologie ORDER BY date_cible ASC")
    actions = [dict(r) for r in cur.fetchall()]

    # Verifier actions clefs
    actions_attendues = [
        'Confirmer abattement',
        'Demander dates baux',
        'AV Jean-Luc',
        'Don signature usufruit',
        'Vente SCI',
        'travaux',
        'Succession Jean-Luc',
        'maison Kleber',
        'LMNP operationnel',
    ]
    for att in actions_attendues:
        found = any(att.lower() in a['action'].lower() for a in actions)
        if found:
            ok(f"  Action trouvee : {att}")
        else:
            ko(f"  Action MANQUANTE : {att}")

    # Verifier montants cles
    for a in actions:
        if 'av jean-luc' in a['action'].lower() and a['montant'] > 0:
            if abs(a['montant'] - 23400) < 100:
                ok(f"  AV Jean-Luc = {a['montant']} EUR (OK)")
            else:
                ko(f"  AV Jean-Luc = {a['montant']} EUR (attendu 23400)")
        if 'vente sci' in a['action'].lower() and a['montant'] > 0:
            if abs(a['montant'] - 296100) < 100:
                ok(f"  SCI = {a['montant']} EUR (OK)")
            else:
                ko(f"  SCI = {a['montant']} EUR (attendu 296100)")
else:
    ko("Table chronologie VIDE — pas d'actions")

# ================================================================
# 5. TABLE AAH_SUIVI
# ================================================================
print("\n[5] VERIFICATION TABLE AAH_SUIVI...")
cur.execute("SELECT * FROM aah_suivi ORDER BY mois ASC")
aah_rows = [dict(r) for r in cur.fetchall()]
if aah_rows:
    ok(f"Table aah_suivi : {len(aah_rows)} lignes")
    for a in aah_rows:
        mois = a['mois']
        prevu = a['montant_prevu']
        if mois == '2026' and prevu == 625:
            ok(f"  AAH 2026 = {prevu} EUR (OK)")
        elif mois == '2027' and prevu == 0:
            ok(f"  AAH 2027 = {prevu} EUR (OK — pas d'AAH)")
        elif mois == '2027' and prevu != 0:
            ko(f"  AAH 2027 = {prevu} EUR (DEVRAIT ETRE 0)")
        elif mois == '2028' and prevu == 1033:
            ok(f"  AAH 2028 = {prevu} EUR (OK plein taux)")
        elif mois == '2028' and prevu != 1033:
            ko(f"  AAH 2028 = {prevu} EUR (DEVRAIT ETRE 1033)")
        elif mois == '2029' and prevu == 1033:
            ok(f"  AAH 2029 = {prevu} EUR (OK)")
        else:
            warn(f"  AAH {mois} = {prevu} EUR")
else:
    ko("Table aah_suivi VIDE")

# ================================================================
# 6. TABLE LMNP
# ================================================================
print("\n[6] VERIFICATION TABLE LMNP...")
cur.execute("SELECT * FROM lmnp LIMIT 1")
lmnp_row = cur.fetchone()
if lmnp_row:
    lmnp = dict(lmnp_row)
    ok("Table lmnp existe")
    for c in ['date_acquisition', 'valeur_acquisition', 'valeur_terrain',
              'travaux', 'loyer_brut_mensuel', 'charges_annuelles',
              'duree_amort_immeuble', 'duree_amort_mobilier', 'valeur_mobilier']:
        if c in lmnp:
            ok(f"  lmnp.{c} = {lmnp[c]}")
        else:
            warn(f"  lmnp.{c} MANQUANT")
else:
    ko("Table lmnp VIDE")

# ================================================================
# 7. CALCULS MATHEMATIQUES
# ================================================================
print("\n[7] VERIFICATION CALCULS...")

# Age actuel
if profil:
    dn = datetime.strptime(profil['date_naissance'], '%Y-%m-%d')
    age = (datetime.today() - dn).days / 365.25
    if 50 < age < 52:
        ok(f"  Age actuel = {age:.1f} ans (coherent)")
    else:
        ko(f"  Age actuel = {age:.1f} ans (devrait etre ~50.5)")

    # Mois restants
    mois_rest = max(0, int((profil['age_cible'] * 365.25 - (datetime.today() - dn).days) / 30.44))
    if 480 < mois_rest < 510:
        ok(f"  Mois restants = {mois_rest} (~41 ans)")
    else:
        warn(f"  Mois restants = {mois_rest}")

# Capital total
if cap:
    total = sum(cap.get(k, 0) for k in ['cc', 'livret_a', 'ldds', 'lep', 'av1', 'av2', 'av3'])
    ok(f"  Capital total calcule = {total:,.0f} EUR")

    # ARVA
    if profil and mois_rest > 0:
        r_m = (1 + profil['rendement_annuel']) ** (1/12) - 1
        facteur = (1 + r_m) ** mois_rest
        annuite = (facteur - 1) / r_m
        arva_val = max(0, (total * facteur - profil['capital_cible']) / annuite)
        if arva_val > 0:
            ok(f"  ARVA (rente max) = {arva_val:,.0f} EUR/mois")
            if arva_val > profil['rail_mensuel']:
                ok(f"  ARVA > Rail ({arva_val:,.0f} > {profil['rail_mensuel']}) = PLAN VIABLE")
            else:
                ko(f"  ARVA < Rail ({arva_val:,.0f} < {profil['rail_mensuel']}) = PLAN EN DANGER")
        else:
            ko("  ARVA = 0 (probleme de calcul)")

    # Rendement pondere
    taux = {'cc': 0.0, 'livret_a': 0.024, 'ldds': 0.024, 'lep': 0.035,
            'av1': 0.035, 'av2': 0.035, 'av3': 0.035}
    rp = sum(cap.get(k, 0) * taux[k] for k in taux) / total if total > 0 else 0
    ok(f"  Rendement pondere = {rp*100:.2f}%")

    # PV latentes AV
    for av in ['av1', 'av2', 'av3']:
        vers_key = f'{av}_versements'
        if av in cap and vers_key in cap:
            pv = max(0, cap[av] - cap[vers_key])
            ok(f"  PV latentes {av} = {pv:,.0f} EUR (val={cap[av]:,.0f}, vers={cap[vers_key]:,.0f})")

    # Phase
    ph = 1 if age < 64 else (2 if age < 75 else 3)
    ok(f"  Phase actuelle = {ph} (age {age:.1f})")

    # Pioche ce mois
    if profil:
        aah = profil['aah_mensuel'] + profil.get('pch_mensuel', 0)
        loyer = profil['loyer_net']
        rail = profil['rail_mensuel']
        if ph == 1:
            pioche = rail - aah - loyer
        elif ph == 2:
            pioche = rail
        else:
            pioche = rail - profil.get('rvd_mensuel', 450)
        ok(f"  Pioche ce mois = {pioche:,.0f} EUR (rail {rail} - AAH {aah} - loyer {loyer})")

# ================================================================
# 8. COHERENCE FLUX CHRONOLOGIE
# ================================================================
print("\n[8] COHERENCE FLUX CHRONOLOGIE...")
if nb_chrono > 0:
    total_entrees = sum(a['montant'] for a in actions if a['sens'] == 'entree')
    total_sorties = sum(a['montant'] for a in actions if a['sens'] == 'sortie')
    solde_chrono = total_entrees - total_sorties
    ok(f"  Total entrees = {total_entrees:,.0f} EUR")
    ok(f"  Total sorties = {total_sorties:,.0f} EUR")
    ok(f"  Solde net = {solde_chrono:,.0f} EUR")

    # Verifier que les entrees sont coherentes
    entrees_attendues = 23400 + 296100 + 182900 + 202000  # AV + SCI + succession + Kleber
    if abs(total_entrees - entrees_attendues) < 5000:
        ok(f"  Entrees coherentes avec le plan (~{entrees_attendues:,.0f} attendu)")
    else:
        warn(f"  Entrees = {total_entrees:,.0f} (attendu ~{entrees_attendues:,.0f}, ecart {total_entrees-entrees_attendues:+,.0f})")

# ================================================================
# 9. TABLES SECONDAIRES
# ================================================================
print("\n[9] TABLES SECONDAIRES...")
for table in ['surplus_affectation', 'jalons_notes', 'devis_artisans', 'depenses']:
    try:
        cur.execute(f"SELECT COUNT(*) as n FROM {table}")
        n = dict(cur.fetchone())['n']
        ok(f"  Table {table} : {n} lignes")
    except Exception as e:
        warn(f"  Table {table} : {e}")

# ================================================================
# 10. VARIABLES EN DUR DANS LE CODE
# ================================================================
print("\n[10] VARIABLES EN DUR (informationnel)...")
hardcoded = [
    ("Plancher", 2200, "Regle du jeu — normal en dur"),
    ("Bonus", 2700, "Regle du jeu — normal en dur"),
    ("Capital objectif construction", 454000, "Regle du jeu — normal en dur"),
    ("Parents 325 EUR/mois", 325, "Charge fixe — a surveiller si changement"),
    ("AAH plein taux 1033", 1033, "Montant legal — a surveiller si revalorisation"),
    ("FGAP 70000/assureur", 70000, "Regle legale — normal en dur"),
    ("Taux LEP fallback 3.5%", 0.035, "A mettre a jour si taux change (actuellement 2.5%)"),
    ("Taux LA/LDDS fallback 2.4%", 0.024, "A mettre a jour si taux change (actuellement 1.5%)"),
]
for nom, val, comment in hardcoded:
    warn(f"  {nom} = {val} — {comment}")

db.close()

# ================================================================
# RAPPORT FINAL
# ================================================================
print("\n" + "=" * 70)
print("  RAPPORT FINAL")
print("=" * 70)
print(f"  OK     : {nb_ok}")
print(f"  ERREURS: {nb_ko}")
print(f"  ATTENT.: {nb_warn}")
print()

if nb_ko == 0:
    print("  >>> COCKPIT OPERATIONNEL — Aucune erreur critique <<<")
elif nb_ko <= 3:
    print("  >>> COCKPIT QUASI-OPERATIONNEL — Corrections mineures a faire <<<")
else:
    print("  >>> COCKPIT A CORRIGER — Erreurs a resoudre <<<")

print()
print("  ERREURS A CORRIGER :")
for status, test, detail in resultats:
    if status == "ERREUR":
        print(f"    [KO] {test} — {detail}")

print()
print("  POINTS D'ATTENTION :")
for status, test, detail in resultats:
    if status == "ATTENTION":
        print(f"    [!!] {test} — {detail}")

print("\n" + "=" * 70)
print("  FIN DU TEST")
print("=" * 70)
