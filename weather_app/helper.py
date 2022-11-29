import math
import models
from sqlalchemy.orm import Session
from crud import get_app_key_by_id, get_locations_by_address, create_locations
from info import Location, City, Weather
from weather_api import  get_lat_lon_api, getCurrentWeather, gettWeatherFOrecast
from database import SessionLocal, engine

def initializeDB():
    models.Base.metadata.create_all(bind=engine)

    #Creating instance for database
    return SessionLocal()

def getCredential(db: Session, id: int):
    
    #Run this code to insert the app key into the table
    #appKey = "9c2e93f176d25559234a3d43712a506e" ; #create_app_key(db = db, app_key = appKey )

    #Getting the app key from database
    db_app_key = get_app_key_by_id(db = db,  id = id)
    
    return db_app_key.appkey

def get_latitude_longitude(db: Session, city: City, app_key:str) -> Location:
    
    #Getting the geo-locations info (latitude and longitude)
    #First I'll check if we already have the lat and lon stored in database
    if db_location := get_locations_by_address(db = db, city = city):
        location = Location(city = city, latitude=db_location.latitude, longitude=db_location.longitude)
    else:
        #If we haven't seen this city before, we call the API to get latitude and longitude
        location = get_lat_lon_api(city, app_key)
        if not location.status:
            print("Looks like was not able to get geo location")
            return
        
        #Here I'm storing latitude and longitude in database, to avoid the API call next time for the same city
        create_locations(db = db, loc = location)
    
    return location

def printWeather(db:Session, city: City, app_key: str ):    
    
    location = get_latitude_longitude(db = db, city = city, app_key = app_key)
    
    #Object to get details from current weather
    currTemp = getCurrentWeather(location, app_key)
    
    #Just checking if was processed without erros
    if not currTemp:
        print("Looks like was not able to get current temperature")    
        return
    elif not currTemp.status == True:    
        print(currTemp.error)
        return
    else:
        printFormaCurrenttWeather(weather = currTemp)
    
    #Here I'm going to get the forecast next 5 days
    weather_list = gettWeatherFOrecast(location, credential = app_key, unit = "metric" )
    
    #Just checking if was processed without erros
    if not weather_list:
        print("Looks like was not able to get weather forecast")
        return
    else:
        printFormaForecastWeather(weather_list)
    
        
def printFormaCurrenttWeather(weather: Weather):
    #Show the current weather details/conditions           
    print("--------------------------------\n")    
    print("Neighborhood: " + weather.neighborhood)        
    print("Condition: " + weather.condition)
    print("Current Temperature: " + str(math.trunc(weather.temperature)) + " °C")    
    print("Humidity: " + str(weather.humidity) + " %")
    print("Wind: " + str(weather.wind) + " m/s")
    print("--------------------------------\n")
    
def printFormaForecastWeather(weather_list):
    
    for item in weather_list:
        #Show the current weather details/conditions
        obj_weather  = weather_list[item]
        date_hour = item.split()
        date = date_hour[0]
        hour = date_hour[1]        
        print("Weather forecast to " + obj_weather.city  + " on " + date + " at " + hour + ":")        
        print("Condition: " + obj_weather.condition + \
              ", Temperature: " + str(math.trunc(obj_weather.temperature)) + " °C" + \
              ", Humidity: " + str(obj_weather.humidity) + " %" +  \
              ", Wind: " + str(obj_weather.wind) + " m/s \n" )