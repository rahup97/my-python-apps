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

for cod1, cod2, c in zip(lat, lon, city) :
     fg.add_child(folium.Marker(location=[cod1, cod2], popup=c, icon=folium.Icon(color="red")))
     map.add_child(fg)


map.save("Map1.html")
