from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

app = FastAPI()

pbk_p=b"""-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAlBetA0wjbaj+h7oJ/d/h
pNrXvAcuhOdFGEFcfCxSWyLzWk4SAQ05gtaEGZyetTax2uqagi9HT6lapUSUe2S8
nMLJf5K+LEs9TYrhhBdx/B0BGahA+lPJa7nUwp7WfUmSF4hir+xka5ApHjzkAQn6
cdG6FKtSPgq1rYRPd1jRf2maEHwiP/e/jqdXLPP0SFBjWTMt/joUDgE7v/IGGB0L
Q7mGPAlgmxwUHVqP4bJnZ//5sNLxWMjtYHOYjaV+lixNSfhFM3MdBndjpkmgSfmg
D5uYQYDL29TDk6Eu+xetUEqry8ySPjUbNWdDXCglQWMxDGjaqYXMWgxBA1UKjUBW
wbgr5yKTJ7mTqhlYEC9D5V/LOnKd6pTSvaMxkHXwk8hBWvUNWAxzAf5JZ7EVE3jt
0j682+/hnmL/hymUE44yMG1gCcWvSpB3BTlKoMnl4yrTakmdkbASeFRkN3iMRewa
IenvMhzJh1fq7xwX94otdd5eLB2vRFavrnhOcN2JJAkKTnx9dwQwFpGEkg+8U613
+Tfm/f82l56fFeoFN98dD2mUFLFZoeJ5CG81ZeXrH83niI0joX7rtoAZIPWzq3Y1
Zb/Zq+kK2hSIhphY172Uvs8X2Qp2ac9UoTPM71tURsA9IvPNvUwSIo/aKlX5KE3I
VE0tje7twWXL5Gb1sfcXRzsCAwEAAQ==
-----END PUBLIC KEY-----"""

pbk = serialization.load_pem_public_key(pbk_p)

@app.get("/{token}", response_class=PlainTextResponse)
def get_subscription(token: str):
    expire_at = datetime.utcnow()+timedelta(days = 7)
    subscription = """#profile-title: Test
    vless://0d8dccc2-4dd7-43e6-a746-8a565bf52230@193.38.235.178:443?encryption=none&flow=xtls-rprx-vision&security=reality&pbk=8LX3OWbe3ToLmjjBciyby1N0pgQ77QPMOjXR3Prc7wk&sni=www.googletagmanager.com&fp=chrome&sid=d9dbc73b&spx=%2F&type=tcp#mydocker2
    """
    ciphertext = pbk.encrypt(
        subscription.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    if token == "PJv1fkV9nkCfgDmH":
        return ciphertext 


