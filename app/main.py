import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.routes import client, login, account

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Loop Solutions",
    description="CRM para Loop Solutions",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(client.router)
app.include_router(client.front_router)
app.include_router(login.router)
app.include_router(account.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
async def front_page(request: Request):
    return templates.TemplateResponse(request, "index.html", {"titulo": "Loop Solutions CRM", "versao": "1.0.0"})

def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
