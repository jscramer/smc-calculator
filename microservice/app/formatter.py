import json
import datetime
import numpy as np
from app.models import DataPacket, MultipleSplit,Split, Info, Coordinates, Zone, DataPacket, Acceleration, AnchorInfo

def format_split(jsonData):
    #List to store all created dataPackets
    sdv_data_packet_list = []
   
    for packet in jsonData["measurements"]:       
        sdv_data_packet = DataPacket(
            time=datetime.datetime.fromisoformat(packet["t"]),
            x = int(packet["x"]) if packet["x"] != None else None,
            y = int(packet["y"]) if packet["y"] != None else None,
            z = int(packet["z"]) if packet["z"] != None else None ,
            latency = int(packet["lat"]),
            acceleration = create_coordinates_model(packet),
            info = create_info_model(packet)
        )
        sdv_data_packet_list.append(sdv_data_packet)

    return sdv_data_packet_list

def format_split_multiple(jsonData):    
    sdv_multiple_splits = []
    for split in jsonData:
        sdv_multiple_splits.append(format_split(split))           
    return sdv_multiple_splits

def create_info_model(packet):   
    info_model = Info(
        succes_rate= int(packet["info"]["rate"]),
        packet_loss=int(packet["info"]["loss"]),
        idx=int(packet["info"]["idx"]),
        valid=bool(packet["info"]["valid"]),
        err=packet["info"]["err"],
    )
    return info_model

def create_coordinates_model(packet):
    #If the packet is not valid or the packet has no acceleration data, return none
    if(packet["info"]["valid"] != True or packet["acc"] == None): 
        return None   
    else:
        coordinates = Coordinates(
                x=int(packet["acc"][0]),
                y=int(packet["acc"][1]),
                z=int(packet["acc"][2]),
        )        
        return coordinates    