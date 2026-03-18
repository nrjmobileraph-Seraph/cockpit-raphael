import os
import json
import time
from pathlib import Path

# --- Configuration ---
FINARY_EMAIL = os.environ.get('FINARY_EMAIL', 'nrjmobileraph@gmail.com')
FINARY_PASSWORD = os.environ.get('FINARY_PASSWORD', '')
TOKEN_CACHE_FILE = Path(__file__).parent / '.finary_token.json'
API_BASE = 'https://api.finary.com/users/me'

# --- Cache du token JWT ---

def _save_token(token_data):
    """Sauvegarde le token JWT et metadata dans un fichier local."""
    try:
        with open(TOKEN_CACHE_FILE, 'w') as f:
            json.dump(token_data, f)
    except Exception as e:
        print(f"[Finary] Erreur sauvegarde token: {e}")


def _load_token():
    """Charge le token JWT depuis le cache local."""
    try:
        if TOKEN_CACHE_FILE.exists():
            with open(TOKEN_CACHE_FILE, 'r') as f:
                data = json.load(f)
                # Verifier si le token n'est pas expire
                if data.get('expire_at', 0) > time.time():
                    return data
                else:
                    print("[Finary] Token expire, re-authentification necessaire.")
    except Exception as e:
        print(f"[Finary] Erreur lecture token: {e}")
    return None


def _extract_token_from_signin(signin_result):
    """Extrait le JWT token et les metadonnees depuis le resultat signin."""
    try:
        session = signin_result['client']['sessions'][0]
        token = session['last_active_token']['jwt']
        expire_at = session.get('expire_at', 0) / 1000  # ms -> secondes
        return {
            'jwt': token,
            'expire_at': expire_at,
            'created_at': time.time(),
            'session_id': session.get('id', '')
        }
    except (KeyError, IndexError) as e:
        print(f"[Finary] Erreur extraction token: {e}")
        return None


# --- Authentification ---

def finary_signin(otp_code=None):
    """
    Authentification Finary.
    - Si cookies Clerk valides -> refresh JWT automatiquement (pas d'OTP)
    - Sinon -> signin avec code OTP
    Retourne le JWT token (str) ou None si echec.
    """
    import http.cookiejar
    from curl_cffi import requests as crequests
    from pathlib import Path

    cookie_file = Path(__file__).parent / 'localCookiesMozilla.txt'
    jwt_file = Path(__file__).parent / 'jwt.json'

    # 1. Essayer refresh via cookies Clerk (pas besoin d'OTP)
    if cookie_file.exists() and jwt_file.exists():
        try:
            cj = http.cookiejar.MozillaCookieJar(str(cookie_file))
            cj.load()
            with open(jwt_file, 'r') as jf:
                jwt_data = json.load(jf)
            sid = jwt_data.get('session_id', '')
            if sid:
                s = crequests.Session()
                s.cookies = cj
                headers = {'Origin': 'https://app.finary.com', 'Referer': 'https://app.finary.com'}
                r = s.post(f'https://clerk.finary.com/v1/client/sessions/{sid}/tokens', headers=headers, impersonate='chrome110')
                if r.status_code == 200:
                    jwt_token = r.json().get('jwt', '')
                    if jwt_token:
                        # Mettre a jour le cache
                        jwt_data['session_token'] = jwt_token
                        with open(jwt_file, 'w') as jf:
                            json.dump(jwt_data, jf)
                        _save_token({
                            'jwt': jwt_token,
                            'expire_at': time.time() + 90*24*3600,
                            'created_at': time.time(),
                            'session_id': sid
                        })
                        print("[Finary] Token rafraichi via cookies Clerk")
                        return jwt_token
                else:
                    print(f"[Finary] Refresh cookies echoue (status {r.status_code})")
        except Exception as e:
            print(f"[Finary] Erreur refresh cookies: {e}")

    # 2. Pas de cookies ou refresh echoue -> signin avec OTP
    if otp_code is None:
        print("[Finary] Pas de session valide. Code OTP necessaire.")
        return None

    try:
        from finary_uapi.signin import signin
        result = signin(otp_code)
        token_data = _extract_token_from_signin(result)
        if token_data:
            _save_token(token_data)
            print("[Finary] Connexion reussie - token sauvegarde")
            return token_data['jwt']
    except Exception as e:
        print(f"[Finary] Erreur signin: {e}")

    return None


def is_connected():    return None


def is_connected():
    """Verifie si un token valide existe en cache."""
    cached = _load_token()
    return cached is not None


def get_token_info():
    """Retourne les infos du token cache (pour affichage dans le cockpit)."""
    cached = _load_token()
    if cached:
        import datetime
        expire_dt = datetime.datetime.fromtimestamp(cached['expire_at'])
        created_dt = datetime.datetime.fromtimestamp(cached['created_at'])
        days_left = (expire_dt - datetime.datetime.now()).days
        return {
            'connected': True,
            'created': created_dt.strftime('%d/%m/%Y %H:%M'),
            'expires': expire_dt.strftime('%d/%m/%Y %H:%M'),
            'days_left': days_left,
            'session_id': cached.get('session_id', '')
        }
    return {'connected': False}


# --- Appels API Finary ---

def _api_get(endpoint, token):
    """Appel GET a l'API Finary."""
    try:
        from curl_cffi import requests as crequests
        headers = {'Authorization': f'Bearer {token}'}
        url = f'{API_BASE}/{endpoint}'
        r = crequests.get(url, headers=headers, impersonate='chrome')
        if r.status_code == 200:
            return r.json()
        else:
            print(f"[Finary] API {endpoint}: status {r.status_code}")
            return None
    except Exception as e:
        print(f"[Finary] Erreur API {endpoint}: {e}")
        return None


def get_holdings_accounts(token):
    """Recupere tous les comptes bancaires (CC, livrets, etc.)."""
    data = _api_get('holdings_accounts', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_institution_connections(token):
    """Recupere les connexions bancaires (BoursoBank, etc.)."""
    data = _api_get('institution_connections', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_fonds_euro(token):
    """Recupere les fonds euros (assurances-vie)."""
    data = _api_get('fonds_euro', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_investments(token):
    """Recupere les investissements (PEA, CTO, etc.)."""
    data = _api_get('investments', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_cryptos(token):
    """Recupere les cryptomonnaies."""
    data = _api_get('cryptos', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_real_estates(token):
    """Recupere l'immobilier."""
    data = _api_get('real_estates', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_scpis(token):
    """Recupere les SCPI."""
    data = _api_get('scpis', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_generic_assets(token):
    """Recupere les actifs generiques."""
    data = _api_get('generic_assets', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_crowdlendings(token):
    """Recupere les crowdlendings."""
    data = _api_get('crowdlendings', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_precious_metals(token):
    """Recupere les metaux precieux."""
    data = _api_get('precious_metals', token)
    if data and 'result' in data:
        return data['result']
    return []


def get_checking_transactions(token, page=1, perpage=50):
    """Recupere les transactions du compte courant."""
    data = _api_get(f'transactions?page={page}&per_page={perpage}&transaction_type=checking', token)
    if data and 'result' in data:
        return data['result']
    return []


# --- Fonction principale : tout recuperer d'un coup ---

def get_full_patrimoine(token):
    """
    Recupere TOUT le patrimoine Finary en un seul appel.
    Retourne un dict avec toutes les categories.
    """
    patrimoine = {
        'holdings_accounts': get_holdings_accounts(token),
        'institution_connections': get_institution_connections(token),
        'fonds_euro': get_fonds_euro(token),
        'investments': get_investments(token),
        'cryptos': get_cryptos(token),
        'real_estates': get_real_estates(token),
        'scpis': get_scpis(token),
        'generic_assets': get_generic_assets(token),
        'crowdlendings': get_crowdlendings(token),
        'precious_metals': get_precious_metals(token),
    }
    
    # Calcul du total
    total = 0.0
    for account in patrimoine['holdings_accounts']:
        total += account.get('balance', 0) or 0
    for fe in patrimoine['fonds_euro']:
        total += fe.get('current_value', 0) or 0
    for inv in patrimoine['investments']:
        total += inv.get('current_value', 0) or 0
    for crypto in patrimoine['cryptos']:
        total += crypto.get('current_value', 0) or 0
    for re_item in patrimoine['real_estates']:
        total += re_item.get('user_estimated_value', 0) or 0
    for scpi in patrimoine['scpis']:
        total += scpi.get('current_value', 0) or 0
    for ga in patrimoine['generic_assets']:
        total += ga.get('current_price', 0) or 0
    for cl in patrimoine['crowdlendings']:
        total += cl.get('current_price', 0) or 0
    for pm in patrimoine['precious_metals']:
        total += pm.get('current_value', 0) or 0
    
    patrimoine['total_brut'] = total
    patrimoine['last_sync'] = time.strftime('%d/%m/%Y %H:%M:%S')
    
    return patrimoine