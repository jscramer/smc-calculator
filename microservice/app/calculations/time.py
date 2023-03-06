from app.models import DataPacket
from typing import List
import datetime

def get_total_time_elapsed(data_packet_list : List[DataPacket]):
    #Define start and end time
    start_time = datetime
    end_time = datetime
   
    #Grab the index of the last model in the list in order to find the end time
    last_index = len(data_packet_list)-1
    
    # #Grab the time from the first and last record in the list    
    start_time = data_packet_list[0].time    
    end_time = data_packet_list[last_index].time

    # #Calculate time difference in seconds  
    time_elapsed = datetime.timedelta.total_seconds(end_time - start_time)    
    
    return time_elapsed


    
