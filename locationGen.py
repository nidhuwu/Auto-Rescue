import geocoder

location = geocoder.ip('me')  # Get location based on IP address
latitude, longitude = location.latlng

print(f"Latitude: {latitude}, Longitude: {longitude}")
