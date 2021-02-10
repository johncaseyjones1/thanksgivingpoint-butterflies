
import os
import sys

import tornado.ioloop
import tornado.web

# from tornado import template
# from pyjade.ext.tornado import patch_tornado

# patch_tornado()

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, bundle_path):
        self.bundle_path = bundle_path

    def get(self):
        self.render('index.html', bundle_path=self.bundle_path)

class DashboardHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({ 'dashboard': 'Dashboard!' })

class ActivitiesHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({ 'activities': 'Activities!' })

class GalleryHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({ 'gallery': 'Gallery!' })

def make_app(bundle_path, debug):
    return tornado.web.Application(
       template_path=os.path.join(os.path.dirname(__file__), "views"),
       static_path=os.path.join(os.path.dirname(__file__), "public"),
       debug=debug,
       handlers=[
           (r"/", MainHandler, dict(bundle_path=bundle_path)),
           (r".*/api/dashboard", DashboardHandler),
           (r".*/api/activities", ActivitiesHandler),
           (r".*/api/gallery", GalleryHandler),
           ],
       )

if __name__ == "__main__":
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
