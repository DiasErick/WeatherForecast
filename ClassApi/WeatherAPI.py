import requests
from ClassInfo.WeatherInfo import WeatherInfo

class WeatherAPI:
        
    def __init__(self):
        self.latitude  = "0"
        self.longitude = "0"
        self.unit      = "metric"
        self.appKey    = "9c2e93f176d25559234a3d43712a506e"
        
    def setLatitude(self, latitude):
        self.latitude = str(latitude)
    
    def setLongitude(self, longitude):
        self.longitude = str(longitude)
    
    def setUnit(self, unit):
        self.unit = unit

    def getCurrentWeather(self):        
        
        #Creating the object to get info about current weather
        currWeather = WeatherInfo()
        
        #Cheking if all mandatory information was sent to method
        if self.latitude == "0":
            currWeather.setError("The latitude is mandatory to get current weather.")
            return currWeather
        
        if self.longitude == "0":
            currWeather.setError("The longitude is mandatory to get current weather.")
            return currWeather        
        
        #Getting the base URL from Endpoint
        url = f"https://api.openweathermap.org/data/2.5/weather"        

        #Adding the paramters to call endpoint
        url += "?lat="   + self.latitude
        url += "&lon="   + self.longitude
        url += "&appid=" + self.appKey
        url += "&units=" + self.unit
        
        #Calling API
        response = requests.get(url).json() 
        if response['cod'] == 200:            
            #Adding information about the current weather
            currWeather.setTemperature(response['main']['temp'])
            currWeather.setMaxTemperature(response['main']['temp_max'])
            currWeather.setMinTemperature(response['main']['temp_min'])
            currWeather.setHumidity(response['main']['humidity'])
            currWeather.setCondition(response['weather'][0]['main'] + ", " + response['weather'][0]['description'])
            currWeather.setNeighborhood(response['name'])
            currWeather.setWind(response['wind']['speed'])
            currWeather.setStatus(True)
        else:
            currWeather.setError("We got an error trying to get the current weather")
        
        return currWeather