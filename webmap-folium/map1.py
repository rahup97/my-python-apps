import folium
import pandas

#for base layer of map
map = folium.Map(location=[30,-100], zoom_start=4, tiles="Mapbox Bright")

#now adding markers-adding objects to the map, and these objects are called children
fg = folium.FeatureGroup(name="Mein Map")
data = pandas.read_csv("latlon.csv")

lat = list(data["latitude"])
lon = list(data["longitude"])
city = list(data["city"])
zipcode = list(data["zip_code"])

#function to return different colour for marker depending on the zipcode of the place
def color_generator(zipc):
    if zipc < 50000:
        return 'green'
    elif zipc > 50000 and zipc < 76000:
        return 'blue'
    else:
        return 'red'


for cod1, cod2, c, z in zip(lat, lon, city, zipcode) :
     fg.add_child(folium.Marker(location=[cod1, cod2], popup=c, icon=folium.Icon(color=color_generator(z))))
     map.add_child(fg)

map.save("Map1.html")
