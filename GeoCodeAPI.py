import requests

class GeoCodeAPI:
    
    def __init__(self):    
        self.country = ""
        self.city = ""
        self.state = ""
        self.appKey = "9c2e93f176d25559234a3d43712a506e"
        self.limit = 10
    
    def setCountry(self, country):
        self.country = country
        
    def setCity(self, city):
        self.city = city
        
    def setState(self, state):
        self.state = state
        
    def getGeoLocation(self):         
        
        url = f"http://api.openweathermap.org/geo/1.0/direct"
        url += "?q=" + self.city + ",," + self.country
        url += "&limit=" + str(self.limit)
        url += "&appid=" + self.appKey
        #Calling API
        
        response = requests.get(url).json()
        
        for city in response:
            print("-----------")
            print(city)
            #print(city['state'])
            #print(city['lat'])
            #print(city['lon'])