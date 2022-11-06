from ClassInfo.GeoLocationInfo import GeoLocationInfo
import requests

class GeoCodeAPI:    
    def __init__(self):    
        self.country = ""
        self.city    = ""
        self.state   = ""
        self.appKey  = ""
        self.limit   = 10
    
    def setCountry(self, country):
        self.country = country
        
    def setCity(self, city):
        self.city = city
        
    def setState(self, state):
        self.state = state
    
    def setAppKey(self, appKey):
        self.appKey = appKey        
        
    def getGeoLocation(self):        
        #Creatng object with geo location information
        geo = GeoLocationInfo()
        
        #Cheking if all mandatory information was sent to method
        if not self.country:
            geo.setError("The country is mandatory to get geo locations details")
            return geo
        
        if not self.city:
            geo.setError("The city is mandatory to get geo locations details")
            return geo
        
        if not self.state:
            geo.setError("The state is mandatory to get geo locations details")
            return geo
        
        #Defininf url to the endpoint to get latitude and longitude
        url = f"http://api.openweathermap.org/geo/1.0/direct"
        url += "?q=" + self.city + ",," + self.country
        url += "&limit=" + str(self.limit)
        url += "&appid=" + self.appKey

        #Calling API
        response = requests.get(url).json()

        #Cheking if was procces successfuly
        if response:

            #Interation in the cities in the response
            for city in response:
                
                #Just cheking if we are considering the correct state, because it is possible the have cities with same name in differente states.
                if city['state'] == self.state:

                    #adding details in the object
                    geo.setCity(self.city)
                    geo.setCountry(self.country)
                    geo.setCState(self.state)
                    geo.setLat(city['lat'])
                    geo.setLon(city['lon'])
                    geo.setStatus(True)
                    break
        else:
            geo.setError("We got an error trying to get the location of city: " + self.city)
            
        return geo