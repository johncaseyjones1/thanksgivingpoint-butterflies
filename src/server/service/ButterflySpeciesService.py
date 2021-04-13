import sys, os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)

from data_access.ButterflySpeciesDAO import ButterflySpeciesDAO

class GetPotentialSpecies:

    @staticmethod
    def getPotentialSpecies(request):
        butterflySpeciesDAO = ButterflySpeciesDAO()
        return butterflySpeciesDAO.getManySpecies(request)

class GetAllSpecies:

    @staticmethod
    def getAllSpecies():
        butterflySpeciesDAO = ButterflySpeciesDAO()
        return butterflySpeciesDAO.getAllSpecies()

class DeleteSpecies:
    
    @staticmethod
    def deleteOneSpecies(request):
        butterflySpeciesDAO = ButterflySpeciesDAO()
        return butterflySpeciesDAO.deleteSpecies(request)

class InsertSpecies:
    
    @staticmethod
    def insertOneSpecies(request):
        # Rename image to name of butterfly
        static_path=os.path.join(os.path.dirname(__file__), "../public")
        scientificName = request.getScientificName()
        newFilePath = static_path + "/photos/" + scientificName.replace(" ", "") + ".jpg"
        os.rename(request.getImagePath(), newFilePath)
        request.setImagePath("/static/photos/" + scientificName.replace(" ", "") + ".jpg")
        butterflySpeciesDAO = ButterflySpeciesDAO()
        return butterflySpeciesDAO.insertOneSpecies(request)

class EditSpecies:
    
    @staticmethod
    def editOneSpecies(request):
        # Rename image to name of butterfly
        butterflySpeciesDAO = ButterflySpeciesDAO()
        return butterflySpeciesDAO.editOneSpecies(request)