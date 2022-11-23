class Weather:
    condition:str      = ""
    neighborhood:str   = ""
    error:str          = ""
    temperature:int    = 0
    minTemperature:int = 0
    maxTemperature:int = 0
    humidity:int       = 0        
    wind:int           = 0        
    gust:int           = 0        
    status:int         = False
    
class Location():
    latitude:str   = "0"
    longitude:str  = "0"
    city:str       = ""
    state:str      = ""
    country:str    = ""
    error:str      = ""
    status         = False