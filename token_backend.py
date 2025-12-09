from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/{token}")
def get_subscription(token: str):
    subscription = {
            "version":1,
            "proxies":[],
            "servers":["vless://0d8dccc2-4dd7-43e6-a746-8a565bf52230@193.38.235.178:443?encryption=none&flow=xtls-rprx-vision&security=reality&pbk=8LX3OWbe3ToLmjjBciyby1N0pgQ77QPMOjXR3Prc7wk&sni=www.googletagmanager.com&fp=chrome&sid=d9dbc73b&spx=%2F&type=tcp#mydocker2"],
            "expire_at":datetime.utcnow()+timedelta(days = 7) 
    }
    if token == "PJv1fkV9nkCfgDmH":
        return subscription

