from fastapi import APIRouter, Request, Response
from app.calculations import heatmap
from app.formatter import format_split, format_split_multiple

router = APIRouter(
    prefix="/heatmap"
)

@router.post("/single-split")
async def get_heatmap_data_singple_split(info: Request):    
    try:
        received_Json = await info.json()
        return heatmap.generate_heatm_map_data_single_split(format_split(received_Json))
    except Exception as e:    
        print(e)    
        return Response("Server couldn't generate the heatmap",400)

@router.post("/multiple-split")
async def get_heatmap_data_multiple_splits(info: Request):    
    try:
        received_Json = await info.json()
        return heatmap.generate_heat_map_data_multiple_splits(format_split_multiple(received_Json))
    except Exception as e:    
        print(e)    
      