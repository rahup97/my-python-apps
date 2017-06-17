import folium as fl
import pandas as pd

#for base layer of map
map = fl.Map(location=[30,-100], zoom_start=2, tiles="Mapbox Bright")

#now adding markers-adding objects to the map, and these objects are called children
fgcities = fl.FeatureGroup(name = "World Cities")
fgpop = fl.FeatureGroup(name = "World Population Indicator")
data = pd.read_csv("cities.csv")

lat = list(data["lat"])
lon = list(data["lng"])
city = list(data["city"])
popu = list(data["pop"])

#function to return different colour for marker depending on the population of the place
def color_generator(g):
    if g < 10000:
        return 'green'
    elif g > 10000 and g < 150000:
        return 'blue'
    else:
        return 'red'

#add marker for each city in csv file and add all of them to the cities Feature Group
for cod1, cod2, c, g in zip(lat, lon, city, popu) :
     fgcities.add_child(fl.CircleMarker(location = [cod1, cod2], popup = c, fill_color = color_generator(g), color = color_generator(g), radius = 4.7, fill_opacity = 0.88))

fgpop.add_child(fl.GeoJson(data = open('world.json', 'r', encoding =' utf-8-sig'),
style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 2500000 else 'orange' if 25000000 <= x['properties']['POP2005'] and x['properties']['POP2005'] < 100000000 else 'red'}))

#Finally add the feature group as children to the map to use in the Layer control(Top Right of Screen)
map.add_child(fgpop)
map.add_child(fgcities)
map.add_child(fl.LayerControl())

map.save("WorldMap_Info.html")
