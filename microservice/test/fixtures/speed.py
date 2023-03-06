import pytest

from app.models import DataPacket, Coordinates, Zone, AnchorInfo, Acceleration
from typing import List

zone1: Zone = Zone(
    id=1,
    name="Test zone 1"
)
zone2: Zone = Zone(
    id=2,
    name="Test zone 2"
)
zoneList : List[Zone] = [zone1,zone2]

anchor1: AnchorInfo = AnchorInfo(
       anchorId=11,
            rss=-84
)
anchor2: AnchorInfo = AnchorInfo(
 anchorId=8458,
            rss=-91
)
anchor3: AnchorInfo = AnchorInfo(
          anchorId=16888,
            rss=-82
)
anchor4: AnchorInfo = AnchorInfo(
      anchorId=17948,
            rss=-84
)
anchor5: AnchorInfo = AnchorInfo(
     anchorId=19005,
            rss=-97
)
anchor6: AnchorInfo = AnchorInfo(
      anchorId=34558,
            rss=-96
)
anchor7: AnchorInfo = AnchorInfo(
  anchorId=35862,
            rss=-89
)

anchorList : List[AnchorInfo] = [anchor1,anchor2,anchor3,anchor4,anchor5,anchor6,anchor7]

data_packet1: DataPacket = DataPacket(
    tagId=1,
    time="2022-11-07T14:37:38",
    success=True,
    coordinates= Coordinates(
        x=0,
        y=0,
        z=0
    ),
    zones=zoneList,
    anchorData=anchorList,
    accelerometer=None
)
data_packet2: DataPacket = DataPacket(
    tagId=1,
    time="2022-11-07T14:37:40",
    success=True,
    coordinates= Coordinates(
        x=1,
        y=1,
        z=1
    ),
    zones=zoneList,
    anchorData=anchorList,
    accelerometer=None       
    
)
data_packet3: DataPacket = DataPacket(
    tagId=1,
    time="2022-11-07T14:37:41",
    success=True,
    coordinates= Coordinates(
        x=3,
        y=3,
        z=3
    ),
    zones=zoneList,
    anchorData=anchorList,
    accelerometer=None
)
all_data_packets_list : List[DataPacket] = [data_packet1,data_packet2,data_packet3]

@pytest.mark.usefixtures
class TestSpeedFunctions:
    def get_mock_datapackets_list():        
        return all_data_packets_list



