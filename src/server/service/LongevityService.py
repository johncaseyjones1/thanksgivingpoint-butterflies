
import sys, os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)
from data_access.LongevityDAO import LongevityDAO

from datetime import datetime

class GetLongevity:

    @staticmethod
    def getLongevityStillFlying():
        longevityDAO = LongevityDAO()
        return longevityDAO.getLongevityStillFlying()

    @staticmethod
    def getLongevityRecentReleases():
        longevityDAO = LongevityDAO()
        return longevityDAO.getLongevityRecentReleases()