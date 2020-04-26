from datetime import datetime
import folium
import json
import requests
r = requests.get('http://api.open-notify.org/iss-now.json')
obj = r.json()
timestamp = datetime.utcfromtimestamp(obj['timestamp']).strftime('%Y-%m-%d %H:%M:%d:%S')
lat = obj['iss_position']['latitude']
lon = obj['iss_position']['longitude']
print(f"{lat} {lon} {timestamp}")
m = folium.Map(
    tiles='OpenStreetMap',
)
folium.Marker(
	location=[lat, lon],
        radius=5,
        fill=True,
        popup=f"iss {timestamp}",
        color="black",
).add_to(m)
m.save('iss.html')
