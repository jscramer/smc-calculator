from typing import List
from app.models import DataPacket, Split
from app.calculations.constant import PLAYER_HEIGHT

#Simple height function. Improvements can be done by using the current zone to adjust minimum height level.
#Think of that an user might be higher due to being on a ramp.
def get_max_height(datapacket_list: List[DataPacket]):
    max_height = 0

    #Check for every datapacket if the height minus the player height is bigger than max_height
    for packet in datapacket_list:
        if packet.z - PLAYER_HEIGHT > max_height:
            max_height = packet.z - PLAYER_HEIGHT
    return max_height

def get_max_height_from_multiple_split(split_list: List[Split]):
    max_height_list = []
    for split in split_list:
        max_height_list.append(get_max_height(split))
    return max_height_list
