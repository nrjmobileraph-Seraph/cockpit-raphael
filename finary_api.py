import subprocess
import json
import sys

def main():
    print("🚀 --- RECHERCHE DANS LES COMPTES SYNCHRONISÉS ---")
    try:
        # On interroge la section 'holdings_accounts' qui est la plus complète
        cmd = [sys.executable, "-m", "finary_uapi", "holdings_accounts"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                items = data.get("result", [])
                
                total = 0
                found = False
                
                print("📂 DÉTAIL DES COMPTES TROUVÉS :")
                print("-" * 30)
                
                for item in items:
                    name = item.get("name", "Compte inconnu")
                    balance = float(item.get("balance", 0))
                    if balance != 0:
                        found = True
                        total += balance
                        formated_bal = "{:,.2f}".format(balance).replace(",", " ").replace(".", ",")
                        print(f"   ➤ {name} : {formated_bal} €")
                
                if found:
                    print("-" * 30)
                    valeur_totale = "{:,.2f}".format(total).replace(",", " ").replace(".", ",")
                    print(f"💰 TOTAL DISPONIBLE : {valeur_totale} €")
                    print("-" * 30)
                else:
                    print("❌ Aucun solde trouvé dans 'holdings_accounts'.")
                    print("💡 Tentative de lecture brute pour comprendre...")
                    print(result.stdout[:500]) # Affiche un extrait si c'est vide
            except Exception as e:
                print(f"❌ Erreur d'analyse : {e}")
        else:
            print("❌ La commande 'holdings_accounts' a échoué.")
            
    except Exception as e:
        print(f"⚠️ Erreur système : {e}")

if __name__ == "__main__":
    main()