from fastapi import APIRouter, Request, Response
from app.calculations import distance
from app.formatter import format_split, format_split_multiple

router = APIRouter(
    prefix="/distance"
)

@router.post("/calculate")
async def calculate_distance(info: Request):    
    try:
        received_Json = await info.json()
        return distance.get_distance(format_split(received_Json))
    except:        
        return Response("Server couldn't calculate the distance",400)

@router.post("/calculate-multiple")
async def calculate_distance_multiple_splits(info: Request):    
    try:
        received_Json = await info.json()
        return distance.get_distance_multiple(format_split_multiple(received_Json))
    except:        
        return Response("Server couldn't calculate the distance",400)
