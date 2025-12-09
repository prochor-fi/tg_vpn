from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/{token}", response_class=PlainTextResponse)
def get_subscription(token: str):
    expire_at = datetime.utcnow()+timedelta(days = 7)
    subscription = """#profile-title: Test
    vless://0d8dccc2-4dd7-43e6-a746-8a565bf52230@193.38.235.178:443?encryption=none&flow=xtls-rprx-vision&security=reality&pbk=8LX3OWbe3ToLmjjBciyby1N0pgQ77QPMOjXR3Prc7wk&sni=www.googletagmanager.com&fp=chrome&sid=d9dbc73b&spx=%2F&type=tcp#mydocker2
    """
    if token == "PJv1fkV9nkCfgDmH":
        return subscription


