from json.encoder import JSONEncoder
import re
import sys
sys.path.append('../')

import os
import sys
import json
import uuid

import tornado.ioloop
import tornado.web
import tornado.escape
from tornado.log import enable_pretty_logging

from service.ObservationService import InsertObservation
from service.ShipmentService import InsertShipment
from service.ShipmentService import EditShipment
from service.ShipmentService import DeleteShipment
from service.ObservationService import GetOneWeek
from service.ReleaseService import GetAllReleases
from service.ReleaseService import InsertRelease
from service.ReleaseService import DeleteRelease
from service.ShipmentService import GetAllShipments
from service.ButterflySpeciesService import GetPotentialSpecies
from service.ButterflySpeciesService import GetAllSpecies
from data_access.request.observation.insertObservationRequest import InsertObservationRequest
from data_access.request.shipment.insertShipmentRequest import InsertShipmentRequest
from data_access.request.shipment.updateShipmentRequest import UpdateShipmentRequest
from data_access.request.shipment.deleteShipmentRequest import DeleteShipmentRequest
from data_access.request.release.insertReleaseRequest import InsertReleaseRequest
from data_access.request.release.deleteReleaseRequest import DeleteReleaseRequest
from data_access.request.observation.getObservationsInRangeRequest import GetObservationsInRangeRequest
#from data_access.request.shipment.getShipmentRequest import GetShipmentsInRangeRequest
from data_access.request.butterfly_species.GetButterflySpeciesRequest import GetButterflySpeciesRequest


# from tornado import template
# from pyjade.ext.tornado import patch_tornado

# patch_tornado()

from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, bundle_path):
        self.bundle_path = bundle_path

    def get(self):
        self.render('index.html', bundle_path=self.bundle_path)

class DashboardHandler(tornado.web.RequestHandler):
    def get(self):
        #acces mongodb
        self.write({ 'dashboard': 'Dashboard!' })

class GetShipmentsHandler(tornado.web.RequestHandler):
    def get(self):
        response = GetAllShipments.getAllShipments()
        self.write({ 'allShipments': response.getShipment() })

class GetReleasesHandler(tornado.web.RequestHandler):
    def get(self):
        response = GetAllReleases.getAllReleases()
        self.write({ 'allReleases': response.getRelease() })

class GetAllButterfliesHandler(tornado.web.RequestHandler):
    def get(self):
        response = GetAllSpecies.getAllSpecies()
        #json_response = JSONEncoder().encode(response.getResponse())
        #json_response = json.dumps([ob for ob in json_response])
        self.write({"allButterflies": response.getResponse()})

class ObservationHandler(tornado.web.RequestHandler):
    def post(self):
        requestBody = tornado.escape.json_decode(self.request.body)
        speciesPrediction = requestBody["speciesPrediction"]
        filePath = requestBody['filePath']
        commonName = requestBody['commonName']
        request = InsertObservationRequest('1', filePath, speciesPrediction, commonName)
        responseMessage = InsertObservation.insertOneObservation(request).getMessage()
        
        self.write({"message": responseMessage})

class PostShipmentHandler(tornado.web.RequestHandler):
    def post(self):
        requestBody = tornado.escape.json_decode(self.request.body)
        date = requestBody["date"]
        species = requestBody['species']
        origin = requestBody['origin']
        quantity = requestBody['quantity']
        supplier = requestBody["supplier"]
        emergedEarly = requestBody['emergedEarly']
        deadOnArrival = requestBody['deadOnArrival']
        request = InsertShipmentRequest(date, species, origin, quantity, supplier, emergedEarly, deadOnArrival)
        responseMessage = InsertShipment.insertOneShipment(request).getMessage()
        
        self.write({"message": responseMessage})

class EditShipmentHandler(tornado.web.RequestHandler):
    def post(self):
        requestBody = tornado.escape.json_decode(self.request.body)
        ID = requestBody["_id"]
        date = requestBody["date"]
        species = requestBody['species']
        origin = requestBody['origin']
        quantity = requestBody['quantity']
        supplier = requestBody["supplier"]
        emergedEarly = requestBody['emergedEarly']
        deadOnArrival = requestBody['deadOnArrival']
        failedToEmerge = requestBody["FTE"]
        wings = requestBody["W"]
        parasite = requestBody["Parasite"]

        request = UpdateShipmentRequest(ID, date, species, origin, quantity, supplier,
         emergedEarly, deadOnArrival, failedToEmerge, wings, parasite)
        responseMessage = EditShipment.editOneShipment(request).getMessage()
        
        self.write({"message": responseMessage})

class DeleteShipmentHandler(tornado.web.RequestHandler):
    def post(self):
        requestBody = tornado.escape.json_decode(self.request.body)
        ID = requestBody["_id"]

        request = DeleteShipmentRequest(ID)
        responseMessage = DeleteShipment.deleteOneShipment(request).getMessage()
        
        self.write({"message": responseMessage})

class PostReleaseHandler(tornado.web.RequestHandler):
    def post(self):
        requestBody = tornado.escape.json_decode(self.request.body)
        date = requestBody["date"]
        species = requestBody['species']
        quantity = requestBody['quantity']
        request = InsertReleaseRequest(species, quantity, date)
        responseMessage = InsertRelease.insertOneRelease(request).getMessage()
        
        self.write({"message": responseMessage})

class DeleteReleaseHandler(tornado.web.RequestHandler):
    def post(self):
        requestBody = tornado.escape.json_decode(self.request.body)
        ID = requestBody["_id"]

        request = DeleteReleaseRequest(ID)
        responseMessage = DeleteRelease.deleteOneRelease(request).getMessage()
        
        self.write({"message": responseMessage})

class PhotoHandler(tornado.web.RequestHandler):
    def post(self):
        hex = uuid.uuid4().hex
        filePath = "/var/www/butterfly/static/uploads/" + hex + ".jpg"
        imgFile = self.request.files.get('image')
        for img in imgFile:
            img ['filename']
            with open(filePath, "wb") as f:
                f.write(img["body"])
        
        self.write({"filePath": filePath})

class StaffDashboardHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({ 'staff_dashboard': 'Dashboard!' })
              
class GetPotentialPredictions(tornado.web.RequestHandler):
    # I'm doing a post request so that way I can still send a body even though I'm not posting
    def post(self):
        requestBody = tornado.escape.json_decode(self.request.body)
        request = GetButterflySpeciesRequest(requestBody)
        response = GetPotentialSpecies.getPotentialSpecies(request)
        self.write({"speciesPrediction": response.getResponse()})

class GetObservationsOneWeek(tornado.web.RequestHandler):
    # I'm doing a post request so that way I can still send a body even though I'm not posting
    def get(self):
        response = GetOneWeek.getOneWeek()
        self.write({"observations": response.getObservations()})


def make_app(bundle_path, debug):
    static_path=os.path.join(os.path.dirname(__file__), "public")
    return tornado.web.Application(
       template_path=os.path.join(os.path.dirname(__file__), "views"),
       static_path=os.path.join(os.path.dirname(__file__), "public"),
       debug=debug,
       handlers=[
           (r"/", MainHandler, dict(bundle_path=bundle_path)),
           (r".*/api/dashboard", DashboardHandler),
           (r".*/api/shipment", GetShipmentsHandler),
           (r".*/api/shipment/post", PostShipmentHandler),
           (r".*/api/shipment/edit", EditShipmentHandler),
           (r".*/api/shipment/delete", DeleteShipmentHandler),
           (r".*/api/release", GetReleasesHandler),
           (r".*/api/release/post", PostReleaseHandler),
           (r".*/api/release/delete", DeleteReleaseHandler),
           (r".*/api/butterfly_species", GetAllButterfliesHandler),
           (r".*/api/observations", ObservationHandler),
           (r".*/api/photos", PhotoHandler),
           (r".*/api/staff/dashboard", StaffDashboardHandler),
           (r".*/api/prediction/get", GetPotentialPredictions),
           (r".*/api/observations/week", GetObservationsOneWeek)
           ],
       )

if __name__ == "__main__":
    enable_pretty_logging()
    bundle_path = '/static/javascripts/bundle.js'
    debug = False
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        bundle_path = 'http://localhost:8008/bundle.js'
        debug = True
    app = make_app(bundle_path, debug)
    port = 8080
    app.listen(port)
    print('http://localhost:{}'.format(port))
    tornado.ioloop.IOLoop.current().start()
