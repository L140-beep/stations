import json
from plib.plib.triangle import Triangle
from plib.plib.base import Point
from plib.plib.station import Stations


station = Stations()

station.loadData('plib/stations.json')

print(station.minArea())