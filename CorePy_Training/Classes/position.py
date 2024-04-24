class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= 90):
            raise ValueError(f"Latitude {latitude} is out of range; must be between -90 and 90.")

        if not (-180 <= longitude <= 180):
            raise ValueError(f"Longitude {longitude} is out of range; must be between -180 and 180.")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude
