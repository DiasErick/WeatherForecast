from geo_code_api import GeoCodeAPI, get_lat_lon
from weather_api import WeatherAPI, getCurrentWeather
import math
from location import Location
from credential import Credential


appKey = Credential()

#List with cities that we wish to know the current temperature
locations = []
loc = Location() ; loc.city = "Guarulhos" ; loc.state = "São Paulo" ; loc.country = "BR" ; locations.append(loc)
loc = Location() ; loc.city = "Fredericton" ; loc.state = "New Brunswick" ; loc.country = "CA" ; locations.append(loc)

#INterating the cities to get details from geo locations (latitute and longitude) based on the city, country and state.
for location in locations:
    
    #getting the geolocations info (latitude and longitude)
    location = get_lat_lon(location = location, credential = appKey)    

    #just cheking if we got the information with no erros
    if not location:
        print("Looks like was not able to get geo location")
        break
    elif not location.getStatus() == True:
        #Print error we got from API
        print(location.getError())
        break
       
#Loop to get current weather from places in the list
for location in locations:
    
    #Object to get details from current weather    
    currTemp = getCurrentWeather(location = location, credential = appKey)    

    #Just checkin if was processed without erros
    if not currTemp:
        print("Looks like was not able to get current location")
        break        
    elif not currTemp.getStatus() == True:
        #Print error we got from API
        print(currTemp.getError())
        break
    else:        
        #Show the current weather details/conditions        
        print()
        print("--------------------------------")
        print("Neighborhood: " + currTemp.getNeighborhood())        
        print("Condition: " + currTemp.getCondition())
        print("Current Temperature: " + str(math.trunc(currTemp.getTemperature())) + " °C")    
        print("Humidity: " + str(currTemp.getHumidity()) + " %")
        print("Wind: " + str(currTemp.getWind()) + " m/s")
        print()