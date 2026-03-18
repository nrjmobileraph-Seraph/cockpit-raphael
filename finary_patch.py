import http.cookiejar, json, os, time, pathlib
from curl_cffi import requests
CLERK_ROOT = "https://clerk.finary.com"
APP_ROOT = "https://app.finary.com"
SD = pathlib.Path(__file__).parent
def finary_signin():
    from dotenv import load_dotenv
    load_dotenv(SD / ".env")
    email = os.environ.get("FINARY_EMAIL")
    password = os.environ.get("FINARY_PASSWORD")
    if not email or not password:
        raise RuntimeError("Set FINARY_EMAIL and FINARY_PASSWORD in .env")
    session = requests.Session()
    h = {"Accept-Encoding":"identity","Origin":APP_ROOT,"Referer":APP_ROOT,"User-Agent":"finary_uapi patched"}
    print(f"Connexion Finary ({email})...")
    r1 = session.post(f"{CLERK_ROOT}/v1/client/sign_ins", data={"identifier":email}, headers=h, impersonate="chrome110")
    j1 = r1.json()
    sia = j1["response"]["id"]
    print(f"  Step 1: {j1['response']['status']}")
    time.sleep(0.5)
    r2 = session.post(f"{CLERK_ROOT}/v1/client/sign_ins/{sia}/attempt_first_factor", data={"strategy":"password","password":password}, headers=h, impersonate="chrome110")
    j2 = r2.json()
    status = j2.get("response",{}).get("status","")
    print(f"  Step 2: {status}")
    if status == "needs_second_factor":
        factors = j2.get("response",{}).get("supported_second_factors",[])
        print(f"  2FA methodes: {factors}")
        strat = factors[0]["strategy"] if factors else "totp"
        if strat in ("email_code","phone_code"):
            session.post(f"{CLERK_ROOT}/v1/client/sign_ins/{sia}/prepare_second_factor", data={"strategy":strat}, headers=h, impersonate="chrome110")
            print(f"  Code envoye par {strat}")
        code = input("  Code (6 chiffres) : ").strip()
        r3 = session.post(f"{CLERK_ROOT}/v1/client/sign_ins/{sia}/attempt_second_factor", data={"strategy":strat,"code":code}, headers=h, impersonate="chrome110")
        j2 = r3.json()
        status = j2.get("response",{}).get("status","")
        print(f"  Step 3: {status}")
    if status == "complete":
        cs = j2["client"]["sessions"][0]
        with open(str(SD/"jwt.json"),"w") as f:
            json.dump({"session_token":cs["last_active_token"]["jwt"],"session_id":cs["id"]}, f)
        print("  >>> FINARY CONNECTE! <<<")
        return session
    raise RuntimeError(f"Echec: {status}")
if __name__ == "__main__":
    finary_signin()
