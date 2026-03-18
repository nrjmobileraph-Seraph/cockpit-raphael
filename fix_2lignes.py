FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. Fix Parents hauteur
ancien_p = 'font-size:18px;font-family:Garamond,Georgia,serif;font-style:italic;letter-spacing:2px;'
nouveau_p = 'font-size:16px;font-family:Garamond,Georgia,serif;font-style:italic;letter-spacing:1px;line-height:1.2;'
if ancien_p in contenu:
    contenu = contenu.replace(ancien_p, nouveau_p)
    modifs += 1
    print("[1/3] OK - Parents hauteur")

# 2. Remplacer les _poches par les 10 poches capital seulement (enlever AAH et Loyers)
ancien_poches_fin = '            ("AAH", _aah_m, "#FFD060"),\n            ("Loyers LMNP", _loyer_m, "#4DFF99"),\n        ]'
nouveau_poches_fin = '            ("AV4 Bourso Vie", cap.get("av4", 0) or 0, "#E8C547"),\n            ("PEA Bourse", cap.get("pea", 0) or 0, "#5599FF"),\n            ("Crypto", cap.get("crypto", 0) or 0, "#FF9933"),\n            ("Crowdfunding", cap.get("crowdfunding", 0) or 0, "#CC66FF"),\n        ]'

if ancien_poches_fin in contenu:
    contenu = contenu.replace(ancien_poches_fin, nouveau_poches_fin)
    modifs += 1
    print("[2/3] OK - 10 poches capital")
else:
    print("[2/3] ERREUR poches")

# 3. Ajouter la ligne REVENUS au-dessus du bloc capital
cible_revenus = "        # --- Sources du capital avec grand rectangle total au-dessus ---"
revenus_bloc = '''        # === LIGNE 1 : REVENUS MENSUELS ===
        _aah_m = profil.get('aah_mensuel', 625) or 625
        _pch_m = profil.get('pch_mensuel', 0) or 0
        _loyer_m = profil.get('loyer_net', 0) or 0
        _rvd_m = profil.get('rvd_mensuel', 0) or 0
        _aspa_m = profil.get('aspa_mensuelle', 0) or 0
        _rev_pro = profil.get('revenus_pro', 0) or 0
        _autres_rentes = profil.get('autres_rentes', 0) or 0
        _revenus = [
            ("AAH", _aah_m, "#FFD060"),
            ("Loyers LMNP", _loyer_m, "#FF7777"),
            ("RVD", _rvd_m, "#FF66AA"),
            ("ASPA", _aspa_m, "#DDAAFF"),
            ("Revenus pro", _rev_pro, "#5599FF"),
            ("Autres rentes", _autres_rentes, "#CC66FF"),
        ]
        _rev_actives = [(n, v, c) for n, v, c in _revenus if v > 0]
        _rev_total = sum(v for _, v, _ in _rev_actives)
        _rev_nb = len(_rev_actives)
        _rev_mid = _rev_nb // 2

        if _rev_actives:
            # Grand rectangle revenus
            _rh = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #4DFF99;border-radius:12px;padding:16px;margin-bottom:2px;">'
            _rh += '<div style="display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;">'
            for _ri, (_rn, _rv, _rc) in enumerate(_rev_actives):
                if _ri > 0 and _ri != _rev_mid:
                    _rh += '<div style="color:#665544;font-size:14px;padding:0 3px;">+</div>'
                if _ri == _rev_mid:
                    _rh += '<div style="color:#4DFF99;font-size:18px;padding:0 6px;">\\u27A1</div>'
                    _rh += f'<div style="min-width:140px;background:#0A0A0A;border:2px solid #4DFF99;border-radius:10px;padding:10px;text-align:center;margin:0 4px;"><div style="color:#4DFF99;font-size:9px;text-transform:uppercase;letter-spacing:2px;">REVENUS/MOIS</div><div style="color:#4DFF99;font-size:22px;font-weight:900;">{_rev_total:,.0f} EUR</div></div>'
                    if _ri > 0:
                        _rh += '<div style="color:#4DFF99;font-size:18px;padding:0 6px;">\\u2B05</div>'
                _rv_col = "#4DFF99" if _rv > 0 else "#665544"
                _rh += f'<div style="flex:1;text-align:center;padding:2px;"><div style="color:{_rv_col};font-size:14px;font-weight:700;">{_rv:,.0f}</div></div>'
            _rh += '</div></div>'
            st.markdown(_rh, unsafe_allow_html=True)

            # Fleches revenus
            _rfh = '<div style="display:flex;justify-content:center;align-items:center;gap:0;margin:2px 0;">'
            for _ri, (_rn, _rv, _rc) in enumerate(_rev_actives):
                if _ri > 0 and _ri != _rev_mid:
                    _rfh += '<div style="padding:0 3px;"></div>'
                if _ri == _rev_mid:
                    _rfh += '<div style="min-width:140px;"></div>'
                _rfh += f'<div style="flex:1;text-align:center;"><span style="color:{_rc};font-size:20px;">\\u2B06</span></div>'
            _rfh += '</div>'
            st.markdown(_rfh, unsafe_allow_html=True)

            # Rectangles revenus dans cadre vert
            _rbh = '<div style="display:flex;gap:6px;flex-wrap:nowrap;">'
            for _ri, (_rn, _rv, _rc) in enumerate(_rev_actives):
                if _ri > 0 and _ri != _rev_mid:
                    _rbh += '<div style="padding:0 2px;"></div>'
                if _ri == _rev_mid:
                    _rbh += '<div style="min-width:140px;"></div>'
                _rbh += f'<div style="flex:1;min-width:90px;background:#1A0D12;border:1px solid {_rc};border-radius:10px;padding:8px;text-align:center;"><div style="color:{_rc};font-size:8px;text-transform:uppercase;letter-spacing:1px;">{_rn}</div><div style="color:#F0E6D8;font-size:13px;font-weight:700;margin-top:3px;">{_rv:,.0f} EUR</div></div>'
            _rbh += '</div>'
            st.markdown('<div style="border:2px solid #4DFF99;border-radius:12px;padding:14px;margin-bottom:16px;background:#0A0A0A;">' + _rbh + '</div>', unsafe_allow_html=True)

'''

if cible_revenus in contenu:
    contenu = contenu.replace(cible_revenus, revenus_bloc + cible_revenus)
    modifs += 1
    print("[3/3] OK - Ligne revenus ajoutee")
else:
    print("[3/3] ERREUR cible revenus")

# Supprimer _aah_m et _loyer_m en doublon dans le bloc capital
contenu = contenu.replace("        _aah_m = profil.get('aah_mensuel', 625) or 625\n        _loyer_m = profil.get('loyer_net', 0) or 0\n        _poches", "        _poches")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"\nTermine ! {modifs}/3")
