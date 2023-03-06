from fastapi import APIRouter, Request, Response
from app.calculations.speed import *
from app.formatter import format_split, format_split_multiple

router = APIRouter(
    prefix="/speed"
)

@router.post("/average-speed")
async def calculateAverageSpeed(info: Request):    
    try:
        receivedJson = await info.json() 
        return get_average_speed(format_split(receivedJson))
    except Exception as e:   
        print(e)     
        return Response("Server couldn't calculate the average speed",400)

@router.post("/average-speed-multiple")
async def calculateAverageSpeedMultiple(info: Request):    
    try:
        receivedJson = await info.json()
        return get_average_speed_multiple(format_split_multiple(receivedJson))
    except Exception as e:   
        print(e)     
        return Response("Server couldn't calculate the average speed",400)

@router.post("/max-speed")
async def calculateMaxSpeed(info: Request):   
    try:
        receivedJson = await info.json()
        return get_max_speed(format_split(receivedJson))        
    except Exception as e:
        print(e)
        return Response("Server couldn't calculate the max speed",400)

@router.post("/max-speed-multiple")
async def calculateMaxSpeedMultiple(info: Request):   
    try:
        receivedJson = await info.json()
        return get_max_speed_multiple(format_split_multiple(receivedJson))        
    except Exception as e:
        print(e)
        return Response("Server couldn't calculate the max speed",400)

@router.post("/work-rate")
async def calculateWorkRate(info: Request):
    try:
        receivedJson = await info.json()
        return get_work_rate(format_split(receivedJson))        
    except Exception as e:
        print(e)
        return Response("Server couldn't calculate the work rate",400)

@router.post("/work-rate-multiple")
async def calculateWorkRate(info: Request):
    try:
        receivedJson = await info.json()
        return get_work_rate_multiple(format_split_multiple(receivedJson))        
    except Exception as e:
        print(e)
        return Response("Server couldn't calculate the work rate",400)

@router.post("/max-acceleration")
async def calculateMaxAcceleration(info: Request):
    try:
        receivedJson = await info.json()
        return get_max_acceleration(format_split(receivedJson))        
    except Exception as e:
        print(e)
        return Response("Server couldn't calculate the max acceleration",400)

@router.post("/max-acceleration-multiple")
async def calculateMaxAccelerationMultiple(info: Request):
    try:
        receivedJson = await info.json()
        return get_max_acceleration_multiple(format_split_multiple(receivedJson))        
    except Exception as e:
        print(e)
        return Response("Server couldn't calculate the max acceleration",400)