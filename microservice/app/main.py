import json
from fastapi import FastAPI, Request, Response, HTTPException
from app.formatter import format_split, format_split_multiple
from app.models import DataPacket
from .routers import speed, distance, heatmap, playerload, height
from fastapi.middleware.cors import CORSMiddleware

#Create fastAPI app
app = FastAPI()

#Attach the routers of each calculations to the app
app.include_router(speed.router)
app.include_router(distance.router)
app.include_router(heatmap.router)
app.include_router(playerload.router)
app.include_router(height.router)


# Avoid CORS-policy blocking
origins = [
    "http://localhost:8080", # For the testing env   
    "https://smc-frontend.sportdatavalley.app" # For the prod env
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type", "Origin", "Accept"],
    max_age=1000 # For dev purposes
)

#Format endpoints
@app.post("/format")
async def getFormatData(info: Request):
    try:        
        receivedJson = await info.json() 
        return format_split(receivedJson)
    except Exception as e:
        print(e)
        return Response("Server couldn't format the data",400)

@app.post("/format-multiple")
async def getFormatDataMultiple(info: Request):
    try:        
        receivedJson = await info.json() 
        return format_split_multiple(receivedJson)
    except Exception as e:
        print(e)
        return Response("Server couldn't format the data",400)