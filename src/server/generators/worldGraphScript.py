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
        reformatLocation = []
        #locationList = ["Africa", "Asia", "Africa", "oceania"]

        copyList = []
        for i in locationList:
            val = i["Location"]
            temp = val.lower()
            copyList.append(temp)

        for location in copyList:
            if location == "africa":
                reformatLocation.append("africa")
            elif location == "asia":
                reformatLocation.append("asia")
            elif location == "antarctica":
                reformatLocation.append("antartica")
            elif location == "north america":
                reformatLocation.append("north_america")
            elif location == "south america":
                reformatLocation.append("south_america")
            elif location == "europe":
                reformatLocation.append("europe")
            elif location == "australia":
                reformatLocation.append("oceania")
            elif location == "oceania":
                reformatLocation.append("oceania")
            

        for location in reformatLocation:
            if location in locationDict:
                count = locationDict[location]
                count += 1
                locationDict[location] = count
            else:
                locationDict[location] = 1

        custom_style = Style(colors=('#2a5835','#5e944d','#79ac54'))

        supra = pygal.maps.world.SupranationalWorld(show_legend=False,interpolate='cubic',style=custom_style)

        continents_dict_a = {}
        continents_dict_b = {}
        continents_dict_c = {}

        continents_dict_b['asia'] = 17
        continents_dict_b['africa'] = 17
        continents_dict_b['north_america'] = 14
        continents_dict_c['south_america'] = 32
        
        supra.add("test",locationDict)

        return supra.render_to_file(static_path + "/graphs/worldMap.svg")

    @staticmethod
    def generateGraph(longevityList):
        static_path=os.path.join(os.path.dirname(__file__), "../public")

        species = ['Adelpha fessonia', 'Agraulis vanillae', 'Amauris niavius', 'Anartia fatima', 'Archaeprepona demophon', 'Archaeprepona meander', 'Ascia limona', 'Athyma perius', 'Atrophaenura nevilli', 'Battus belus', 'Battus polydamas', 'Biblis hyperia', 'Brassolis isthmia', 'Caligo sp.', 'Callinaga buddha', 'Catonephele numilia', 'Catopsilia pomona', 'Catopsilia pyranthe', 'Catopsilia scylla', 'Catopsilis florella', 'Cethosia biblis', 'Cethosia cyane', 'Cethosia hypsea', 'Charaxes brutus', 'Charaxes castor']
        longevity = [14, 9, 15, 21, 12, 12, 38, 30, 10, 7, 36, 42, 6, 35, 35, 90, 14, 9, 30, 14, 8, 60, 21, 12, 19]

        width = 0.35 #width of the bars

        res = {longevity[i]: species[i] for i in range(len(longevity))} #make dictionary with species names as values so can be accessed by longevity

        sortedLongevity = sorted(longevity, reverse = True)

        sortedSpecies = [None]*len(longevity)
        for val in range(len(sortedLongevity)):
                sortedSpecies[val] = (res[sortedLongevity[val]])

        avg = sum(sortedLongevity)/float(len(sortedLongevity))

        #Make the actual bar chart below

        bar_chart = pygal.Bar(title=u'Butterfly Longevity', x_title='Species', y_title='Average Life Span (Days)', show_legend=False, x_label_rotation=30)
        bar_chart.add('Butterflies', sortedLongevity)
        bar_chart.x_labels = sortedSpecies

        bar_chart.render_to_file(static_path + "/graphs/longevityGraph.svg")