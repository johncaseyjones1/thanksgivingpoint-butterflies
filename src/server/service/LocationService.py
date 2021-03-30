import sys, os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)
# Add the parent to sys.pah
sys.path.insert(1, "/Users/bradyneeley/Bio465/thanksgivingpoint-butterflies/src/server/data_access/")
from data_access.ButterflySpeciesDAO import ButterflySpeciesDAO
from data_access.LocationDAO import LocationDAO

from datetime import datetime

class GetLocations:

    @staticmethod
    def getAllLocations():
        locationDAO = LocationDAO()
        return locationDAO.getAllLocations()