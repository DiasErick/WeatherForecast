from geo_code_api import  get_lat_lon
from weather_api import getCurrentWeather
from location import Location
import math
import models
from database import SessionLocal, engine
from crud import create_app_key, get_app_key_by_id, get_locations_by_address, create_locations
models.Base.metadata.create_all(bind=engine)

#Creating instance for database
db = SessionLocal()

#Run this code to insert the app key into the table
#appKey = "9c2e93f176d25559234a3d43712a506e"
#create_app_key(db = db, app_key = appKey.appKey )

#getting the app key to call API
db_app_key= get_app_key_by_id(db = db,  id = 1)

#List with cities that we wish to know the current temperature
locations = []
loc = Location() ; loc.city = "Guarulhos" ; loc.state = "São Paulo" ; loc.country = "BR" ; locations.append(loc)
loc = Location() ; loc.city = "Fredericton" ; loc.state = "New Brunswick" ; loc.country = "CA" ; locations.append(loc)

#Iterating the cities to get details from geo locations (latitute and longitude) based on the city, country and state.
for location in locations:
    
    #Getting the geo-locations info (latitude and longitude)
    #First I'll check if we already have the lat and lon stored in database
    if db_location := get_locations_by_address(db = db, loc = location):
        location.latitude = db_location.latitude
        location.longitude = db_location.longitude
    else:
        # If we haven't seen this city before, we call the API to get latitude and longitude
        #Calling API
        lat_lon = get_lat_lon(location, db_app_key.appkey)
        if not lat_lon:
            print("Looks like was not able to get geo location")
            break
        location.latitude = lat_lon[0]
        location.longitude = lat_lon[1]
        
        #Here I'm storing latitude and longitude in database, to avoid the API call next time for the same city
        create_locations(db = db, loc = location)
    
    #Object to get details from current weather
    currTemp = getCurrentWeather(location, db_app_key.appkey)
    
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