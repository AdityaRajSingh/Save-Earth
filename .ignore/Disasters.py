from geopy.geocoders import Nominatim
from math import sin, cos, sqrt, atan2, radians

class Disaster:

    def __init__(self, disaster_type, time, location):

        self.location = location
        geolocator = Nominatim(user_agent="Get_Coordinates")
        location = geolocator.geocode(location)

        self.centre.latitude = location.latitude
        self.centre.longitude = location.longitude

        self.time = time
        self.disaster = disaster_type

    def distance(self, lat1, lon1, lat2, lon2):
        R = 6373.0

        lat1 = radians(52.2296756)
        lon1 = radians(21.0122287)
        lat2 = radians(52.406374)
        lon2 = radians(16.9251681)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance