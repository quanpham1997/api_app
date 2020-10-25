from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 

app = FastAPI()

app.mount("/static", StaticFiles(directory="./api_app/static"),name="static")

templates = Jinja2Templates(directory="./api_app/templates")

from api_app.views import main , tasks



