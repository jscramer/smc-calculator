import math
from typing import List
from app.models import Split,MultipleSplit, HeatMapDataPoint
from app.calculations.constant import HEATMAP_PRECISION_MULTIPLIER, AREA51_LENGTH, AREA51_WIDTH



def fill_heat_map_data(data_packet_list, heat_map_data):
    #For every datapacket in the datapacket list, round the x and y value and assign it to the correct heat mapa data point
    #TODO: Make the round number dependent on the precision
    for data_packet in data_packet_list:
        #Check if there are no null values or negative values
        if(data_packet.x == None or data_packet.x < 0 or data_packet.y < 0):
            continue

        #Round the x and y value. -3 now makes it round to the nearest multiply of 1000
        x_value = round(data_packet.x,-3)
        y_value = round(data_packet.y,-3)
        
        #Search for the data point in the list which has the correct x and y value and increase the counter of this
        next(data_point for data_point in heat_map_data if data_point.x == x_value and data_point.y == y_value).counter +=1
    return heat_map_data


def generate_heatm_map_data_single_split(dataPacketList):  
    #Get a list of all the squares
    heat_map_data : List[HeatMapDataPoint] = generate_heat_map_squares()
    heat_map_data = fill_heat_map_data(dataPacketList, heat_map_data)    

    return heat_map_data

def generate_heat_map_data_multiple_splits(splitList):
    heat_map_data : List[HeatMapDataPoint] = generate_heat_map_squares()
    
    #For every split fill the heat map data with the new values
    for split in splitList:
        fill_heat_map_data(split, heat_map_data)

    return heat_map_data

def generate_heat_map_squares():
    #Initiate list to store HeatMapDataPoints
    heat_map_data_points : List[HeatMapDataPoint] = []

    #Round the sizing values of Area 51 up to above and multiply by 1000 to convert from the m sizing of width/length
    #To the coordinates sizing of where the diff between x=1 and x=2 is 1mm. 
    #The heatmap precision constant allows for bigger/smaller squares
    area51_length = math.ceil(AREA51_LENGTH)*1000*HEATMAP_PRECISION_MULTIPLIER
    area51_width = math.ceil(AREA51_WIDTH)*1000*HEATMAP_PRECISION_MULTIPLIER

    #Loop that generates all the squares
    #Heatmap precision multiplier is used to define the steps between each x and y value
    y_counter = 0
    x_counter = 0

    while y_counter <= area51_length:
        while x_counter <= area51_width:
            heat_map_data_point = HeatMapDataPoint(
                x=x_counter,
                y=y_counter,
                counter=0
            )
            heat_map_data_points.append(heat_map_data_point)
            x_counter += 1000 * HEATMAP_PRECISION_MULTIPLIER
        x_counter= 0
        y_counter+=1000 * HEATMAP_PRECISION_MULTIPLIER

    return heat_map_data_points