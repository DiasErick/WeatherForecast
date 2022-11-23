from geo_code_api import  get_lat_lon
from weather_api import getCurrentWeather
from location import Location
from credential import Credential
import math

#getting the app key to call API
appKey = Credential()

#List with cities that we wish to know the current temperature
locations = []
loc = Location() ; loc.city = "Guarulhos" ; loc.state = "São Paulo" ; loc.country = "BR" ; locations.append(loc)
loc = Location() ; loc.city = "Fredericton" ; loc.state = "New Brunswick" ; loc.country = "CA" ; locations.append(loc)

#INterating the cities to get details from geo locations (latitute and longitude) based on the city, country and state.
for location in locations:
    
    #getting the geolocations info (latitude and longitude)
    lat_lon = get_lat_lon(location, appKey)    
    if not lat_lon:
        print("Looks like was not able to get geo location")
        break    
    location.latitude = lat_lon[0]
    location.longitude = lat_lon[1]
    
    #Object to get details from current weather    
    currTemp = getCurrentWeather(location, appKey)
    
    #Just checkin if was processed without erros
    if not currTemp:
        print("Looks like was not able to get current location")
        break        
    elif not currTemp.status == True:
        #Print error we got from API
        print(currTemp.error)
        break
    else:        
        #Show the current weather details/conditions        
        print()
        print("--------------------------------")
        print("Neighborhood: " + currTemp.neighborhood)        
        print("Condition: " + currTemp.condition)
        print("Current Temperature: " + str(math.trunc(currTemp.temperature)) + " °C")    
        print("Humidity: " + str(currTemp.humidity) + " %")
        print("Wind: " + str(currTemp.wind) + " m/s")
        print()