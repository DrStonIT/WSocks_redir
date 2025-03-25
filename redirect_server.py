from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

# Главная страница (можно убрать)
@app.get("/")
def home():
    return {"message": "Этот сервер выполняет редирект для V2Ray"}

# Настраиваем редирект
@app.get("/{path:path}")
def redirect(path: str):
    new_url = f"v2raytun://import/https://de-1.wsocks.ru:2096/SubWSocks_VPN_DE_FRA-1/{path}"
    return RedirectResponse(url=new_url)
