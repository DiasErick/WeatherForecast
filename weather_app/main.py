
from info import City
from helper import  getCredential, printWeather,initializeDB

#Creating instance for database
db = initializeDB()

#Getting App Key
app_key = getCredential(db = db, id = 1)
    
#Testing the function with some cities
printWeather(db = db, city = City("Fredericton", "New Brunswick", "CA") , app_key = app_key )
#printWeather(db = db, city = City("Toronto", "Ontario", "CA"), app_key = app_key )