from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

dir_static = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'static')

dir_templates = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
print(f"dir static = {dir_static}")
print(f"dir templates = {dir_templates}")

app.mount("/static", StaticFiles(directory=dir_static), name="static")


templates = Jinja2Templates(directory=dir_templates)

@app.get("/chery/{id}", response_class=HTMLResponse)
async def chery(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="chery.html", context={"id": id}
    )
@app.get("/cucumber/{id}", response_class=HTMLResponse)
async def cucumber(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="cucumber.html", context={"id": id}
    )
@app.get("/apple/{id}", response_class=HTMLResponse)
async def apple(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="apple.html", context={"id": id}
    )
@app.get("/melon/{id}", response_class=HTMLResponse)
async def melon(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="melon.html", context={"id": id}
    )
@app.get("/watermelon/{id}", response_class=HTMLResponse)
async def watermelon(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="watermelon.html", context={"id": id}
    )
@app.get("/tomato/{id}", response_class=HTMLResponse)
async def tomato(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="tomato.html", context={"id": id}
    )
@app.get("/grape/{id}", response_class=HTMLResponse)
async def grape(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="grape.html", context={"id": id}
    )
@app.get("/blackberries/{id}", response_class=HTMLResponse)
async def blackberries(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="blackberries.html", context={"id": id}
    )
@app.get("/pear/{id}", response_class=HTMLResponse)
async def pear(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="pear.html", context={"id": id}
    )
@app.get("/potato/{id}", response_class=HTMLResponse)
async def potato(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="chery.html", context={"id": id}
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/produkt/{item_id}")
async def read_item(item_id):
    return {"produkt_id": item_id}
