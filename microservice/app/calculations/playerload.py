import numpy as np
from typing import List
from app.models import DataPacket, Split

#Resource: https://support.catapultsports.com/hc/en-us/articles/360000574716-What-is-Player-Load-

#Playerload is calculated by the following formula:
#squareroot((fwd2-fwd1)^2 + (side2-side1)^2 + (up2-up1)^2)
#Where fwd = forward acceleration, side = sideways acceleration, up = upwards accelerations.
#1 and 2 are refering to the relation of both accelerations in terms of time. 

def get_player_load(data_packet_list: List[DataPacket]):    
    playerload_list = []
    total_player_load = 0

    #Get only the datapackets that were succesfull and thus have x,y,z coordinates from the list
    succesful_data_packet_list: List[DataPacket] = get_succesfull_data_packets(data_packet_list)

    
    #Get length of the succesfull datapackets, needed for calculations 
    length_of_list = len(succesful_data_packet_list)
    
    #Counter/index used to determine if at the end of the list 
    index = 0
    for data_packet in succesful_data_packet_list:
            #Check if at the end of the list, as there won't be two points to calculate playerload between
            if(index+1 == length_of_list):
                continue

            #Get last index in the array of accelerations, the highest index is the newest measurement
            last_acceleration_index = len(data_packet.acceleration) - 1

            #Grab the x,y,z values of the current data packet and the one after to calculate the playerload between
            #The x value = forward acceleration, y value = sideways acceleration and z value is upwards acceleration
            fwd1=succesful_data_packet_list[index].acceleration[last_acceleration_index].x       
            fwd2=succesful_data_packet_list[index+1].acceleration[last_acceleration_index].x 
            side1=succesful_data_packet_list[index].acceleration[last_acceleration_index].y
            side2=succesful_data_packet_list[index+1].acceleration[last_acceleration_index].y
            up1=succesful_data_packet_list[index].acceleration[last_acceleration_index].z
            up2=succesful_data_packet_list[index+1].acceleration[last_acceleration_index].z
            
            #Formula to calculate playerload between two points
            #plyr_load = squareroot((fwd2-fwd1)^2 + (side2-side1)^2 + (up2-up1)^2)        
            plyr_load = np.sqrt(np.power((fwd2-fwd1),2) + np.power((side2-side1),2) + np.power((up2-up1),2))

            #Add player load to the list
            playerload_list.append(plyr_load)
            total_player_load += plyr_load
            index += 1   
    
    #Potential to return list with total player_load and playerload between two timestamps
    playerload_list.insert(0, total_player_load)

    return total_player_load

def get_succesfull_data_packets(data_packet_list: List[DataPacket]):
    succesful_data_packet_list: List[DataPacket] = []

    for data_packet in data_packet_list:        
        #Grab only the datapackets that were succesfull and have acceleration data
        if(data_packet.info.valid == True and data_packet.acceleration != None):
            succesful_data_packet_list.append(data_packet)   
    return succesful_data_packet_list

def get_player_load_multiple(split_list: List[Split]):
    playerload_list = []
    for split in split_list:
        playerload_list.append(get_player_load(split))
    return playerload_list