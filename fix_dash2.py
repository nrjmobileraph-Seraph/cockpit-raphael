import os

FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"

with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# ============================================================
# 1. INSERER BOX "PROCHAINS MOUVEMENTS" au-dessus de SOURCES
# ============================================================
ancien_sources = "        _src_items = []"

nouveau_mouvements = '''        # --- Prochains mouvements (depuis chronologie) ---
        try:
            _db_mv = db_wrapper.connect()
            _cur_mv = _db_mv.cursor()
            _cur_mv.execute("SELECT date_cible, action, montant, sens FROM chronologie WHERE fait = 0 ORDER BY date_cible ASC LIMIT 6")
            _mvts = [dict(r) for r in _cur_mv.fetchall()]
            _db_mv.close()
        except:
            _mvts = []
        if _mvts:
            _mv_html = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:16px;margin-bottom:16px;">'
            _mv_html += '<div style="color:#C4922A;font-size:11px;text-transform:uppercase;letter-spacing:3px;text-align:center;margin-bottom:12px;">PROCHAINS MOUVEMENTS</div>'
            _mv_html += '<div style="display:flex;flex-direction:column;gap:6px;">'
            for _mv in _mvts:
                _mv_date = _mv.get("date_cible", "")[:10]
                _mv_act = _mv.get("action", "")
                _mv_mnt = _mv.get("montant", 0) or 0
                _mv_sens = _mv.get("sens", "info")
                if _mv_sens == "entree":
                    _mv_icon = "\\u2B06"
                    _mv_col = "#4DFF99"
                    _mv_txt = f"+{_mv_mnt:,.0f} EUR" if _mv_mnt > 0 else ""
                elif _mv_sens == "sortie":
                    _mv_icon = "\\u2B07"
                    _mv_col = "#FF7777"
                    _mv_txt = f"-{_mv_mnt:,.0f} EUR" if _mv_mnt > 0 else ""
                else:
                    _mv_icon = "\\u2139"
                    _mv_col = "#BBA888"
                    _mv_txt = ""
                _mv_html += f'<div style="display:flex;align-items:center;gap:10px;padding:4px 8px;border-bottom:1px solid #2A1A1A;">'
                _mv_html += f'<span style="color:#665544;font-size:11px;min-width:75px;">{_mv_date}</span>'
                _mv_html += f'<span style="font-size:14px;">{_mv_icon}</span>'
                _mv_html += f'<span style="color:#F0E6D8;font-size:12px;flex:1;">{_mv_act}</span>'
                if _mv_txt:
                    _mv_html += f'<span style="color:{_mv_col};font-size:13px;font-weight:700;">{_mv_txt}</span>'
                _mv_html += '</div>'
            _mv_html += '</div></div>'
            st.markdown(_mv_html, unsafe_allow_html=True)

'''

if ancien_sources in contenu:
    contenu = contenu.replace(ancien_sources, nouveau_mouvements + "        _src_items = []", 1)
    modifs += 1
    print("[1/2] OK - Box PROCHAINS MOUVEMENTS inseree")
else:
    print("[1/2] ERREUR - _src_items non trouve")

# ============================================================
# 2. HARMONISER "Pour mes Parents d'Amour" avec les autres KPI
# ============================================================
ancien_parents = '''            <div style="background:#1A0D12;border:2px solid #8B0000;border-radius:12px;padding:16px;text-align:center;">
                <div style="color:#BBA888;font-size:22px;font-weight:700;letter-spacing:2px;">Pour mes Parents d Amour...</div>
                <div style="color:#FF7777;font-size:42px;font-weight:900;">{reste_vivre} EUR</div>
                <div style="color:#DDCCBB;font-size:14px;">{versement_parents} EUR/mois</div>'''

nouveau_parents = '''            <div style="background:#1A0D12;border:2px solid #8B0000;border-radius:12px;padding:16px;text-align:center;">
                <div style="color:#BBA888;font-size:11px;text-transform:uppercase;">Pour mes Parents d Amour...</div>
                <div style="color:#FF7777;font-size:36px;font-weight:900;">{versement_parents} EUR</div>
                <div style="color:#DDCCBB;font-size:12px;">par mois · reste {reste_vivre} EUR</div>'''

if ancien_parents in contenu:
    contenu = contenu.replace(ancien_parents, nouveau_parents)
    modifs += 1
    print("[2/2] OK - Parents d'Amour harmonise avec les autres KPI")
else:
    print("[2/2] ERREUR - bloc Parents non trouve")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)

print(f"\nTermine ! {modifs}/2 modifications appliquees.")
print("Relance : streamlit run app.py")
