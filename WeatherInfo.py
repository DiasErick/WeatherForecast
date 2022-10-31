class WeatherInfo:
    
    def __init__(self):
        
        self.temperature = 0
        self.minTemperature = 0
        self.maxTemperature = 0
        self.humidity = 0
        self.condition = ""
        self.neighborhood = ""
        self.status = False

    def setTemperature(self, temperature):
        self.temperature = temperature
        
    def setMinTemperature(self, minTemperature):
        self.minTemperature = minTemperature
        
    def setMaxTemperature(self, maxTemperature):
        self.maxTemperature = maxTemperature
        
    def setHumidity(self, humidity):
        self.humidity = humidity
    
    def setCondition(self, condition):
        self.condition = condition
        
    def setStatus(self, status):
        self.condition = status 

    def setNeighborhood(self, neighborhood):
        self.neighborhood = neighborhood                       
            
    def getTemperature(self):
        return self.temperature
        
    def getMinTemperature(self):
        return self.minTemperature
        
    def getMaxTemperature(self):
        return self.maxTemperature
        
    def getHumidity(self):
        return self.humidity
    
    def getCondition(self):
        return self.condition
    
    def getStatus(self):
        return self.status
    
    def getNeighborhood(self):
        return self.neighborhood        