from fastapi import FastAPI
from starlette.responses import RedirectResponse
import urllib.parse

app = FastAPI()

# Главная страница (можно убрать)
@app.get("/")
def home():
    return {"message": "Этот сервер выполняет редирект для V2Ray"}

@app.get("/{encoded_key}")
def redirect(encoded_key: str):
    # Декодируем ключ обратно в исходный формат
    key = urllib.parse.unquote(encoded_key)

    # Формируем корректную ссылку для V2RayTun
    new_url = f"v2raytun://import/{key}"
    
    return RedirectResponse(url=new_url)
