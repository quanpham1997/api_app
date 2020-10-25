from api_app import app, templates 
from fastapi import Request 

@app.get("/")
async def index(request: Request) :
    return templates.TemplateResponse("index.html",{"request": request})
@app.get("/app_api")
async def app_api():
    """ This is a app_api dunction to use this run curl '0.0.0.0:5700' """
    return {"message" : {"this is another route"}} 


            
