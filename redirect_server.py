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
    new_url = f"v2raytun://import/vless://945c40e3-fd50-4062-9473-39cb8d001994@de-3.wsocks.ru:443?type=tcp&security=reality&pbk=MCEDsjvqBrJGLXk-yJOsSu5-RK8fO7kkFT_RC_giNgM&fp=chrome&sni=google.com&sid=8e&spx=%2F&flow=xtls-rprx-vision#WSocks VPN Germany"
    return RedirectResponse(url=new_url)
