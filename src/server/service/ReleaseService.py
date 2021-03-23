
import sys, os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)
# Add the parent to sys.pah
sys.path.insert(1, "/home/caseyjones/github/thanksgivingpoint-butterflies/src/server/data_access/")
from ReleaseDAO import ReleaseDAO


class InsertRelease:

    @staticmethod
    def insertOneRelease(request):
        releaseDAO = ReleaseDAO()
        return releaseDAO.insertOneRelease(request)

class GetAllReleases:

    @staticmethod
    def getAllReleases():
        releaseDAO = ReleaseDAO()
        return releaseDAO.getAllReleases()