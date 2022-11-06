class WeatherInfo:
    
    def __init__(self):
        
        self.condition      = ""
        self.neighborhood   = ""
        self.error          = ""
        self.temperature    = 0
        self.minTemperature = 0
        self.maxTemperature = 0
        self.humidity       = 0        
        self.wind           = 0        
        self.gust           = 0        
        self.status         = False

    def setTemperature(self, temperature):
        self.temperature = temperature
    def getTemperature(self):
        return self.temperature        
        
    def setMinTemperature(self, minTemperature):
        self.minTemperature = minTemperature
    def getMinTemperature(self):
        return self.minTemperature        
        
    def setMaxTemperature(self, maxTemperature):
        self.maxTemperature = maxTemperature
    def getMaxTemperature(self):
        return self.maxTemperature 
        
    def setHumidity(self, humidity):
        self.humidity = humidity
    def getHumidity(self):
        return self.humidity
    
    def setCondition(self, condition):
        self.condition = condition
    def getCondition(self):
        return self.condition        
        
    def setStatus(self, status):
        self.status = status
    def getStatus(self):
        return self.status        

    def setNeighborhood(self, neighborhood):
        self.neighborhood = neighborhood
    def getNeighborhood(self):
        return self.neighborhood
    
    def setError(self, error):
        self.error = error
    def getError(self):
        return self.error
    
    def setWind(self, wind):
        self.wind = wind
    def getWind(self):
        return self.wind

    def setGust(self, gust):
        self.wind = gust
    def getGust(self):
        return self.gust