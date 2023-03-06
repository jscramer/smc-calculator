import numpy as np
from typing import List
from app.calculations.time import get_total_time_elapsed
from app.calculations.distance import get_distance
from app.models import DataPacket, Split
from app.calculations.constant import WORK_RATE_SPEED

def get_average_speed(data_packet_list: List[DataPacket]):
    #Calculating average speed formula
    #S = d/t where S is the average speed, d is total distance and t is total time
   
    #Get the total time elapsed 
    t = get_total_time_elapsed(data_packet_list)
    
    #Check if t is not 0, if it is return average speed of 0 since there wasn't a time difference to calculate from
    if (t == 0):
        return 0

    #Get distance from distance calculation method
    d = get_distance(data_packet_list)   

    #Calculate average speed with distance in meter and total time in seconds. Multiplying this with 3.6 to get km/h. 
    #Round is used to round the number to 2 decimals.
    S = (d/t)*3.6
    S = round(S,2)

    #Returns the average speed in km/h
    return S

def get_average_speed_multiple(split_list: List[Split]):
    list_of_average_speed = []
    
    for split in split_list:
        list_of_average_speed.append(get_average_speed(split))
    return list_of_average_speed

def get_max_speed(data_packet_list: List[DataPacket]):
    #MaxSpeed is in this context the highest speed calculated between two chronical packets
    S_max = 0

    #Get the  length of list and initialize an index. 
    # Both are used to determine if the loop below is at it's end.
    lenght_of_list = len(data_packet_list) 
    index = 0   

    list_for_calculations: List[DataPacket] = []
    for data_packet in data_packet_list:
        #Check if at the end of the list, as there won't be two points available to calculate between
        if(index+1 == lenght_of_list):
            continue

        #Clear the list to work with
        list_for_calculations.clear()

        #Add the two points to calculate speed (point(n) and point(n+1))
        list_for_calculations.append(data_packet_list[index])
        list_for_calculations.append(data_packet_list[index+1])
        
        #Get the speed. Average speed can be used here since it will only calculate the speed between the two points
        S = get_average_speed(list_for_calculations)      

        #If the speed is higher than the current max speed, change the max speed to be equal to the new speed
        if(S > S_max):
            S_max = S  
        index+=1   

    return S_max

def get_max_speed_multiple(split_list: List[Split]):
    list_of_max_speed = []

    for split in split_list:
        list_of_max_speed.append(get_max_speed(split))
    return list_of_max_speed

#Workrate is the percentage of time that an user of the system is having a minimun speed greater than 1.5
def get_work_rate(data_packet_list : List[DataPacket]):
    active_packets = 0
    lenght_list = len(data_packet_list) 
    index = 0   

    list_for_calculations: List[DataPacket] = []
    for data_packet in data_packet_list:
        #Check if at the end of the list, as there won't be two points to calculate speed between
        if(index+1 == lenght_list):
            continue

        #Clear the list to work with
        list_for_calculations.clear()

        #Add the two points to calculate speed
        list_for_calculations.append(data_packet_list[index])
        list_for_calculations.append(data_packet_list[index+1])
        
        #Get the speed between two timestamps
        S = get_average_speed(list_for_calculations)
        
        if(S > WORK_RATE_SPEED):
            active_packets+=1       

        index+=1
   
    work_rate = ((active_packets)/(lenght_list-1))*100
    return round(work_rate,2)       

def get_work_rate_multiple(split_list: List[Split]):  
    work_rate_list = [] 
    for split in split_list:
        work_rate_list.append(get_work_rate(split))
    return work_rate_list

def get_max_acceleration(data_packet_list : List[DataPacket]):
    max_acceleration = 0
    for data_packet in data_packet_list:        
        length_of_list = len(data_packet.acceleration)        
        x_acceleration = data_packet.acceleration[length_of_list-1].x
        y_acceleration = data_packet.acceleration[length_of_list-1].y
        z_acceleration = data_packet.acceleration[length_of_list-1].z    
        #Acceleration is a total vector of three vectors in the x, y and z direction. To calculate the total resulting vector all vectors have to be added.
        #This results in the formula of the square root of the (acceleration x-axis)^2+ (acceleration y-axis)^2 + (acceleration z-axis)^2
        #The three values of the pozyx data are expressed in mg (milli-G's)
        acceleration = np.sqrt(np.power(x_acceleration,2)+np.power(y_acceleration,2)+np.power(z_acceleration,2))
        if acceleration > max_acceleration:
            max_acceleration = acceleration
    return max_acceleration

def get_max_acceleration_multiple(split_list: List[Split]):
    max_acceleration_list = []
    for split in split_list:
        max_acceleration_list.append(get_max_acceleration(split))
    return max_acceleration_list