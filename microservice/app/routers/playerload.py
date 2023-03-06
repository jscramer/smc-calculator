from fastapi import APIRouter, Request, Response
from app.calculations import playerload
from app.formatter import format_split, format_split_multiple

router = APIRouter(
    prefix="/playerload"
)

@router.post("/calculate")
async def calculateDistance(info: Request):    
    try:
        receivedJson = await info.json()
        return playerload.get_player_load(format_split(receivedJson))
    except:        
        return Response("Server couldn't calculate the player load",400)

@router.post("/calculate-multiple")
async def calculateDistance(info: Request):    
    try:
        receivedJson = await info.json()
        return playerload.get_player_load_multiple(format_split_multiple(receivedJson))
    except:        
        return Response("Server couldn't calculate the player load",400)