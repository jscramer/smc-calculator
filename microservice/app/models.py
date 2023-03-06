from pydantic import BaseModel
from typing import Optional, List
import datetime

class Coordinates(BaseModel):
    x: Optional[int]
    y: Optional[int]
    z: Optional[int] 

class Zone(BaseModel):
    id: str 
    name: str 

class AnchorInfo(BaseModel):  
    anchorId: int
    rss: int

class Acceleration(BaseModel):
    x: int
    y: int
    z: int

class DataPacket(BaseModel):
    tagId: int 
    time: datetime.datetime
    success: bool 
    coordinates: Coordinates 
    zones: Optional[List[Zone]]
    anchorData: Optional[List[AnchorInfo]]
    accelerometer: Optional[List[Acceleration]]

class HeatMapDataPoint(BaseModel):
    x: int
    y: int
    counter: int

class Answer(BaseModel):
    answer: int
    succesPercentage: int

#The info model
class Info(BaseModel):
    succes_rate: int
    packet_loss: int
    idx: int
    valid: bool
    error: Optional[str]

#Data packet model 
class DataPacket(BaseModel):
    time: datetime.datetime
    x: Optional[int]
    y: Optional[int]
    z: Optional[int]
    latency: int
    acceleration: Optional[Coordinates]
    info: Info    

#Model to store a split, contains a list of data packets
class Split(BaseModel):
    datapackets: List[DataPacket]

#Model to store multiple splits, this will be changed into a run in the future
class MultipleSplit(BaseModel):
    splits: List[Split]
    