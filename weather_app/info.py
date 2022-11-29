class City:
    city = ""
    state = ""
    country = ""
    
    def __init__(self, city: str, state: str, country: str ):
        self.city = city
        self.state = state
        self.country = country

class Location(City):
    
    latitude:str   = "0"
    longitude:str  = "0"
    error:str      = ""
    status         = False
    
    def __init__(self, city: City, latitude: str, longitude: str):
        self.city = city.city
        self.state = city.state
        self.state = city.country
        self.latitude = latitude
        self.longitude = longitude

class Weather(Location):    
    condition:str      = ""
    neighborhood:str   = ""
    error:str          = ""
    temperature:int    = 0
    minTemperature:int = 0
    maxTemperature:int = 0
    humidity:int       = 0        
    wind:int           = 0        
    gust:int           = 0
    
    def __init__(self, location: Location):
        self.latitude = location.latitude
        self.longitude = location.longitude 
        self.city = location.city 
        self.state = location.state 
        self.country = location.country