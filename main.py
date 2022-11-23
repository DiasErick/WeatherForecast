from weather_api import getCurrentWeather, get_lat_lon
from info import Location, Weather
import math
import models
from database import SessionLocal, engine
from crud import create_app_key, get_app_key_by_id, get_locations_by_address, create_locations
models.Base.metadata.create_all(bind=engine)

def printWeather(loc: Location):
    
    #Cheking if all mandatory information was sent to method
    if not loc.country:
        print("The country is mandatory to get geo locations details")
        return
    
    if not loc.city:
        print("The city is mandatory to get geo locations details")
        return
    
    if not loc.state:
        print("The state is mandatory to get geo locations details")
        return
    
    #Creating instance for database
    db = SessionLocal()

    #Run this code to insert the app key into the table
    #appKey = "9c2e93f176d25559234a3d43712a506e" ; #create_app_key(db = db, app_key = appKey.appKey )

    #Getting the app key from database
    db_app_key= get_app_key_by_id(db = db,  id = 1)    
        
    #Getting the geo-locations info (latitude and longitude)
    #First I'll check if we already have the lat and lon stored in database
    if db_location := get_locations_by_address(db = db, loc = loc):
        loc.latitude = db_location.latitude
        loc.longitude = db_location.longitude
    else:
        # If we haven't seen this city before, we call the API to get latitude and longitude    
        lat_lon = get_lat_lon(loc, db_app_key.appkey)
        if not lat_lon:
            print("Looks like was not able to get geo location")
            return
        loc.latitude = lat_lon[0]
        loc.longitude = lat_lon[1]
        
        #Here I'm storing latitude and longitude in database, to avoid the API call next time for the same city
        create_locations(db = db, loc = loc)

    #Object to get details from current weather
    currTemp = getCurrentWeather(loc, db_app_key.appkey)

    #Just checking if was processed without erros
    if not currTemp:
        print("Looks like was not able to get current location")    
        return
    elif not currTemp.status == True:    
        print(currTemp.error)
        return
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

#Testing the function with some cities
loc = Location() ; loc.city = "Fredericton" ; loc.state = "New Brunswick" ; loc.country = "CA"
printWeather(loc)

loc = Location() ; loc.city = "Moncton" ; loc.state = "New Brunswick" ; loc.country = "CA"
printWeather(loc)