from ClassApi.GeoCodeAPI import GeoCodeAPI
from ClassApi.WeatherAPI import WeatherAPI
import math

def getAppKey():
    #Probably  in real world this would be stored in a database, here it's just a test with AppKey hardcoded
    return "9c2e93f176d25559234a3d43712a506e"

#List with cities that we wish to know the current temperature
cities = []
#cities.append(['BR', "Gramado", "Rio Grande do Sul"])
cities.append(['BR', "Guarulhos", "São Paulo"])
cities.append(['CA', "Fredericton", "New Brunswick"])
cities.append(['CA', "Calgary", "Alberta"])
#cities.append(['CA', "Toronto", "Ontario"])
cities.append(['CA', "Ottawa", "Ontario"])

#List of places to be processed and call the API
places = []

#INterating the cities to get details from geo locations (latitute and longitude) based on the city, country and state.
for city in cities:
    
    #gettin the geolocations info (latitude and longitude)
    objGeo = GeoCodeAPI()
    objGeo.setCountry(city[0])
    objGeo.setCity(city[1])
    objGeo.setState(city[2])    
    objGeo.setAppKey( getAppKey() )
    location = objGeo.getGeoLocation()

    #just cheking if we got the information with no erros
    if not location:
        print("Looks like was not able to get geo location")
        break
    elif not location.getStatus() == True:
        #Print error we got from API
        print(location.getError())
        break
    else:
        #Everything good, adding latitude and logintude to places list
        places.append(location)

#Loop to get current weather from places in the list
for place in places:
    
    #Object to get details from current weather
    obj = WeatherAPI()
    obj.setLatitude(place.getLat())
    obj.setLongitude(place.getLon())
    obj.setUnit("metric")
    obj.setAppKey( getAppKey() )

    #Call the method to get current weather conditions
    currTemp = obj.getCurrentWeather()

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