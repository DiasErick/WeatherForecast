from WeatherAPI import WeatherAPI

#Just a test to make sure qye can reach the endpoint
obj = WeatherAPI()
obj.setLatitude(45.995321594837755)
obj.setLongitude(-66.65457929809905)
obj.setUnit("metric")

print(obj.getCurrentWeather())