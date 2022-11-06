class GeoLocationInfo:
    
    def __init__(self):
        
        self.city    = ""
        self.state   = ""
        self.country = ""
        self.error   = ""
        self.lat     = 0
        self.lon     = 0
        self.status = False

    def setCity(self, city):
        self.city = city        
    def getCity(self):
        return self.city        
    
    def setCState(self, state):
        self.state = state        
    def getState(self):
        return self.state        
    
    def setCountry(self, country):
        self.country = country        
    def getCountry(self):
        return self.country        
    
    def setLat(self, lat):
        self.lat = lat        
    def getLat(self):
        return self.lat        
    
    def setLon(self, lon):
        self.lon = lon        
    def getLon(self):
        return self.lon        
        
    def setStatus(self, status):
        self.status = status    
    def getStatus(self):
        return self.status
        
    def setError(self, error):
        self.error = error
    def getError(self):
        return self.error