import requests
from info import Location, Weather

def get_lat_lon(location: Location, credential: str, limit: int = 10):
    
    #Cheking if all mandatory information was sent to method
    if not location.country:
        location.error("The country is mandatory to get geo locations details")
        return location
    
    if not location.city:
        location.error("The city is mandatory to get geo locations details")
        return location
    
    if not location.state:
        location.error("The state is mandatory to get geo locations details")
        return location
    
    #Defininf url to the endpoint to get latitude and longitude
    url = f"http://api.openweathermap.org/geo/1.0/direct"
    url += "?q=" + location.city + ",," + location.country
    url += "&limit=" + str(limit)
    url += "&appid=" + credential

    #Calling API
    response = requests.get(url).json()

    #Cheking if was procces successfuly
    if response:

        #Interation in the cities in the response
        for city in response:
            
            #Just cheking if we are considering the correct state, because it is possible the have cities with same name in differente states.
            if city['state'] == location.state:

                #adding details in the object
                return [ str(city['lat']), str(city['lon']) ]   
        
    return []

def getCurrentWeather(location: Location, credential: str, unit:str = "metric" ) -> Weather:
    
    #Creating the object to get info about current weather
    currWeather = Weather()
    
    #Cheking if all mandatory information was sent to method
    if location.latitude == "0":
        currWeather.error("The latitude is mandatory to get current weather.")
        return currWeather
    
    if location.longitude == "0":
        currWeather.error("The longitude is mandatory to get current weather.")
        return currWeather        
    
    #Getting the base URL from Endpoint
    url = f"https://api.openweathermap.org/data/2.5/weather"        

    #Adding the paramters to call endpoint
    url += "?lat="   + location.latitude
    url += "&lon="   + location.longitude
    url += "&appid=" + credential
    url += "&units=" + unit
    
    #Calling API
    response = requests.get(url).json() 
    if response['cod'] == 200:            
        #Adding information about the current weather            
        currWeather.temperature = response['main']['temp']
        currWeather.maxTemperature = response['main']['temp_max']
        currWeather.minTemperature = response['main']['temp_min']
        currWeather.humidity = response['main']['humidity']
        currWeather.condition = response['weather'][0]['main'] + ", " + response['weather'][0]['description']
        currWeather.neighborhood = response['name']
        currWeather.wind = response['wind']['speed']
        currWeather.status = True
    else:
        currWeather.error = "We got an error trying to get the current weather"
    
    return currWeather

