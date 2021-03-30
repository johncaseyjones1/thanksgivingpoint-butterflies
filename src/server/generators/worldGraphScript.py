import os
import sys
sys.path.append('../../')
import pygal
import math
#import cairosvg
from pygal.style import Style
from pygal.style import LightenStyle

class MapGenerator:

    @staticmethod
    def generateMap(locationList):
        static_path=os.path.join(os.path.dirname(__file__), "../public")
        
        locationDict = {}

        for location in locationList:
            if locationDict.has_key(location):
                count = locationDict[location]
                count += 1
                locationDict[location] = count
            else:
                locationDict[location] = 1

        #dark_lighten_style = LightenStyle('#62AD50', step=30)
        custom_style = Style(colors=('#2a5835','#5e944d','#79ac54'))

        supra = pygal.maps.world.SupranationalWorld(show_legend=False,interpolate='cubic',style=custom_style)
        supra.title = 'Species Distribution by Continent'

        continents_dict_a = {}
        continents_dict_b = {}
        continents_dict_c = {}

        continents_dict_b['asia'] = 17
        continents_dict_b['africa'] = 17
        continents_dict_b['north_america'] = 14
        continents_dict_c['south_america'] = 32
        #continents_dict_a['oceania'] = 0
        #continents_dict_a['antartica'] = 0
        #continents_dict_a['europe'] = 0

        supra.add("0 species",continents_dict_c)
        supra.add("1 to 17 species",continents_dict_a)
        supra.add("17+ species",continents_dict_b)

        supra.render_to_file(static_path + "/graphs/worldMap.svg")
        return (static_path + "/graphs/worldMap.svg")
