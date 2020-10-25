from fastapi import Request, status, BackgroundTaks
from fastapi.response import JSONResponse
from api_app import app, templates
import time
from datetime import datetime

def _run_task(name:str, id=None):
    time.sleep(3)
    with open("tasks_out.txt", mode="a") as file:
        now         =datetime.now()
        
dsfds
s
