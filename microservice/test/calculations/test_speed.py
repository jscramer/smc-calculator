import pytest
import json
from fastapi import status
from conftest import client

import os

# Using test data recorded from Pozyx as base
with open('test/SMC_SampleRun.json') as json_file:  
    file_contents = json_file.read()

class TestSpeedMethods:          
    def test_max_speed_without_request_body(self):
        response = client.post("/max-speed")    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.content == b"Server couldn't calculate the max speed"

    def test_max_speed_with_request_body(self):
        response = client.post("/max-speed",file_contents) 
        assert response.status_code == status.HTTP_200_OK
        assert response.content == b"22.54"
        
    def test_average_speed_without_request_body(self):
        response = client.post("/average-speed")    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.content == b"Server couldn't calculate the average speed"

    def test_average_speed_with_request_body(self):
        response = client.post("/average-speed",file_contents) 
        assert response.status_code == status.HTTP_200_OK
        assert response.content == b"6.16"