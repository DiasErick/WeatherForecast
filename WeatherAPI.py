import requests

class WeatherAPI:
        
    def __init__(self):
        self.latitude = "0"
        self.longitude = "0"
        self.unit = "metric"
        self.appKey = "9c2e93f176d25559234a3d43712a506e"
        
    def setLatitude(self, latitude):
        self.latitude = str(latitude)
    
    def setLongitude(self, longetude):
        self.longetude = str(longetude)
    
    def setUnit(self, unit):
        self.unit = unit

    def getCurrentWeather(self):

        #Cheking if the geo positions was sent
        if not self.latitude:
            return "Latitude is mandatory to get current weahter"
        
        if not self.longetude:
            return "Longitude is mandatory to get current weather"
        
        #Checking the App key to access API
        if not self.appKey:
            return "App Key is mandatory to get current weather"
        
        #Getting the base URL from Endpoint
        url = f"https://api.openweathermap.org/data/2.5/weather"        

        #Adding the paramters to call endpoint
        url += "?lat="   + self.latitude
        url += "&lon="   + self.longetude
        url += "&appid=" + self.appKey
        url += "&units=" + self.unit
        
        #Calling API
        response = requests.get(url).json()
        
        return response