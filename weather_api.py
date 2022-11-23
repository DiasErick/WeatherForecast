import requests
from weather import Weather
from location import Location

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