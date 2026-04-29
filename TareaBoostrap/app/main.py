from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routes.posts import router as posts_router

app = FastAPI(title="Tarea Bootstrap")

templates = Jinja2Templates(directory="templates")

app.include_router(posts_router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )