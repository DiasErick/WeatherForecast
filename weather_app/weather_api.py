import requests
from info import Location, Weather, City

def execute_api(url: str):
    return requests.get(url).json()

def get_lat_lon_api(city: City, credential: str, limit: int = 10) -> Location:    
    
    #Defining url to the endpoint to get latitude and longitude
    url = f"http://api.openweathermap.org/geo/1.0/direct"
    url += "?q=" + city.city + ",," + city.country
    url += "&limit=" + str(limit)
    url += "&appid=" + credential

    #Calling API
    response = execute_api(url)

    #Cheking if was procces successfuly
    if response:
        #Interation in the cities in the response
        for city in response:            
            #Just cheking if we are considering the correct state, because it is possible the have cities with same name in differente states.
            if city['state'] == city.state:
                #adding details in the object
                location = Location(city = city, latitude=str(city['lat']), longitude=str(city['lon']))
                location.status = True
                return location
        
    return location

#def getCurrentWeather(location: Location, credential: str, unit:str = "metric" ) -> Weather:
def getCurrentWeather(location: Location, credential: str, unit:str = "metric" ) -> Weather:
    
    #Creating the object to get info about current weather
    currWeather = Weather(location)
    
    #Getting the base URL from Endpoint
    url = f"https://api.openweathermap.org/data/2.5/weather"        

    #Adding the paramters to call endpoint
    url += "?lat="   + location.latitude
    url += "&lon="   + location.longitude
    url += "&appid=" + credential
    url += "&units=" + unit
    
    #Calling API
    response = execute_api(url)
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

def gettWeatherFOrecast(location: Location, credential: str, unit:str = "metric" ):
     
     #Creating the object to get info about current weather
    currWeather = Weather(location = location)
    
    #Getting the base URL from Endpoint
    url = f"https://api.openweathermap.org/data/2.5/forecast"

    #Adding the paramters to call endpoint
    url += "?lat="   + location.latitude
    url += "&lon="   + location.longitude
    url += "&appid=" + credential
    url += "&units=" + unit
    
    response = execute_api(url)
    if response['cod'] == "200":
        for item in response['list']:
            print(item['main']['temp'] )
            print(item['main']['temp_min'] )
            print(item['main']['temp_max'] )
            print(item['main']['humidity'] )
            print(item['weather'][0]['main'] + " - " + item['weather'][0]['description'])
            print(item['dt_txt'] )
    
    return []
