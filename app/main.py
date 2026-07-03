import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.routes.client import router as router_client

app = FastAPI(
    title="Loop Solutions",
    description="CRM para Loop Solutions",
    version="1.0.0",
)

app.include_router(router_client)

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/front", response_class=HTMLResponse)
async def front_page():
    html_content = """
        <html>
            <head>
                <title>Loop Solutions</title>
            </head>
            <body>
                <h1>Loop Solutions</h1>
                <p>Sistema de Gestão de Ordens de Serviço</p>
                <p>Status: <strong>Operacional </strong></p>
            </body>
        </html>
    """
    return html_content

def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()