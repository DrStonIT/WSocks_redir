from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "V2Ray Redirect Server is running!"}

@app.get("/redirect")
async def redirect_v2ray(request: Request):
    v2ray_link = request.query_params.get("v2ray_link")

    if not v2ray_link:
        return {"error": "No V2Ray link provided"}

    return RedirectResponse(url=v2ray_link)

# Запускаем сервер: uvicorn redirect_server:app --host 0.0.0.0 --port 8080