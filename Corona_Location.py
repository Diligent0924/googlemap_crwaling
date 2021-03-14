import googlemaps
from datetime import datetime
import folium

gmaps = googlemaps.Client(key = "AIzaSyBu4keOe0HaeIUPuIdG8d0XOtiyL0s_pKE")

geocode_result = gmaps.geocode('한경대학교', language = 'ko')


lat = geocode_result[0]['geometry']['location']['lat'] # Dictionary 형태
lng = geocode_result[0]['geometry']['location']['lng'] # Dictionary 형태

map = folium.Map([lat,lng],zoom_start=9)
folium.Marker([lat,lng]).add_to(map)

map.save("mymap.html") # Spyder은 Rendering이 불가능

