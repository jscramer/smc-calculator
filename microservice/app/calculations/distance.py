import numpy as np
from typing import List
from app.models import DataPacket, Split
from app.calculations.constant import DISTANCE_SCALE

#Distance between two 3d points can be calculated with
#d = ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)1/2 
#Where d = distance (m, inches ...)
#x, y, z = coordinates

def get_distance(data_packet_list: List[DataPacket]):
    #Declare variable to store distance
    total_distance = 0

    #Get only the datapackets that were succesfull and thus have x,y,z coordinates from the list
    succesful_data_packet_list: List[DataPacket] = get_succesfull_data_packets(data_packet_list)

    #Get length of the succesful datapackets, needed for calculations 
    length_of_list = len(succesful_data_packet_list)
  
    index = 0
    for data_packet in succesful_data_packet_list:
        #Check if at the end of the list, as there won't be two points to calculate distance between
        if(index+1 == length_of_list):
            continue

        #Grab the x,y,z values of the data_packet(n) and of data_packet(n+1) to calculate distance between the two 3D-points
        x1=succesful_data_packet_list[index].x        
        x2=succesful_data_packet_list[index+1].x
        y1=succesful_data_packet_list[index].y
        y2=succesful_data_packet_list[index+1].y
        z1=succesful_data_packet_list[index].z
        z2=succesful_data_packet_list[index+1].z
        
        #Formula to calculate distance between two 3D Points: 
        # d = ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)1/2        
        d= np.sqrt(np.power((x2-x1),2) + np.power((y2-y1),2) + np.power((z2-z1),2))

        #Add distance to total_distance
        total_distance += d
        index += 1   
            
    #Use scaling constant to get the distance back to meter. 
    total_distance = total_distance * DISTANCE_SCALE

    #Rounding the distance to 2 decimals
    total_distance = round(total_distance,2)
    
    return total_distance

def get_distance_multiple(split_list: List[Split]):
    distance_list = []
    for split in split_list:
        distance_list.append(get_distance(split))
    return distance_list

def get_succesfull_data_packets(data_packet_list: List[DataPacket]):
    succesful_data_packet_list: List[DataPacket] = []

    for data_packet in data_packet_list:        
        #Grab only the datapackets that were succesfull and have acceleration data
        if(data_packet.info.valid == True and data_packet.acceleration != None):
            succesful_data_packet_list.append(data_packet)   
    return succesful_data_packet_list
