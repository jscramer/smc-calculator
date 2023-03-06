from fastapi import APIRouter, Request, Response
from app.calculations import height
from app.formatter import format_split, format_split_multiple

router = APIRouter(
    prefix="/height"
)

@router.post("/calculate-max")
async def calculateMaxHeight(info: Request):    
    try:
        receivedJson = await info.json()
        return height.get_max_height(format_split(receivedJson))
    except:        
        return Response("Server couldn't calculate the max height",400)

@router.post("/calculate-max-multiple")
async def calculateMaxHeightMultiple(info: Request):    
    try:
        receivedJson = await info.json()
        return height.get_max_height_from_multiple_split(format_split_multiple(receivedJson))
    except:        
        return Response("Server couldn't calculate the max height",400)