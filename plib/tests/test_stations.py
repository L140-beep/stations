import pytest
from plib.station import Stations
from plib.base import Point

class TestStations:
    def test_init(self):
        stations = Stations()
    
    def test_loadJson(self):
        stations = Stations()
        stations.loadData('plib/tests/test_data/loadJson.json')
        
        assert stations.points == [Point(53, 53)] 
        
        stations = Stations()
        stations.loadData('plib/tests/test_data/aa.json')
        assert stations.points == [] 
        
    def test_minArea(self):
        stations = Stations()
        stations.loadData('plib/tests/test_data/minArea.json')
        
        assert pytest.approx(stations.minArea(), 0.01) == 0.99