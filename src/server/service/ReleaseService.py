
import sys, os
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data_access'))
sys.path.append(lib_path)
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

class GetReleasesInRange:
    
    @staticmethod
    def getReleasesInRange(days):
        releaseDAO = ReleaseDAO()
        return releaseDAO.getReleasesInRange(days)

class DownloadAllReleases:
    
    @staticmethod
    def generateAllReleasesDownload():
        releaseDAO = ReleaseDAO()
        return releaseDAO.generateAllReleasesDownload()

class DeleteRelease:
    
    @staticmethod
    def deleteOneRelease(request):
        releaseDAO = ReleaseDAO()
        return releaseDAO.deleteRelease(request)