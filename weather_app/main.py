import models
from info import City
from helper import  getCredential, printWeather
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

#Creating instance for database
db = SessionLocal()

#Getting App Key
app_key = getCredential(db = db, id = 1)
    
#Testing the function with some cities
printWeather(db = db, city = City("Fredericton", "New Brunswick", "CA") , app_key = app_key )
#printWeather(db = db, city = City("Toronto", "Ontario", "CA"), app_key = app_key )