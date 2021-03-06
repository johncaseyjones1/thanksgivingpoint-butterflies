
import sys, os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)
# Add the parent to sys.pah
sys.path.insert(1, "/home/caseyjones/github/thanksgivingpoint-butterflies/src/server/data_access/")
from data_access.ButterflySpeciesDAO import ButterflySpeciesDAO

class GetPotentialSpecies:

    @staticmethod
    def getPotentialSpecies(request):
        butterflySpeciesDAO = ButterflySpeciesDAO()
        return butterflySpeciesDAO.getManySpecies(request)