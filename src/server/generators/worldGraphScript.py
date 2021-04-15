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
    def generateGraph(goodReleasesList):
        static_path=os.path.join(os.path.dirname(__file__), "../public")

        width = 0.35 #width of the bars

        res = {}

        res = {item["Probable_Longevity"]: item["Scientific_name"] for item in goodReleasesList}

        longevity = []
        for item in goodReleasesList:
            longevity.append(item.pop("Probable_Longevity"))

        sortedLongevity = sorted(longevity, reverse = True)                                      

        sortedSpecies = [None]*len(longevity)
        for val in range(len(sortedLongevity)):                                                  
                sortedSpecies[val] = (res[sortedLongevity[val]])                              
                                                                                                
        avg = sum(sortedLongevity)/float(len(sortedLongevity))                                   

        #Make the actual bar chart below
                                                                                                
        custom_style = Style(
                major_guide_stroke_dasharray='4,4',                                              
                guide_stroke_color = 'black',                                                    
                major_guide_stroke_color = 'black',                                              
                foreground='black',
                foreground_strong='black',
                foreground_subtle='black',
                colors=('#F38C3C', '#daa520', '#9BC850', '#ffeb44', '#ff00ff'))                  
                                                                                                
        bar_chart = pygal.HorizontalStackedBar(y_title='Species', x_title='Average Life Span (Days)', show_legend=False, style=custom_style)
        bar_chart.add('Butterflies', sortedLongevity)
        bar_chart.x_labels = sortedSpecies

        return bar_chart.render_to_file(static_path + "/graphs/longevityGraph.svg")