from WeatherAPI import WeatherAPI
import math

#Just a test to make sure qye can reach the endpoint
places = []

#São Paulo (Brazil)
places.append([-11.1129897,-68.6030167])

#Toronto (Canada)
places.append([43.64229060302755,-79.38706290425942])

#Toronto (Canada)
places.append([49.283226866979,-123.12177428172556])

#Solth Afraica
places.append([-31.68019546509566,24.22328184725608])

#Fredericton
places.append([45.948947159729464,-66.65050468080652])

for place in places:    
    obj = WeatherAPI()
    obj.setLatitude(place[0])
    obj.setLongitude(place[1])
    obj.setUnit("metric")

    currTemp = obj.getCurrentWeather()

    if currTemp.getStatus:        
        print("--------------------------------")
        print("Neighborhood: " + currTemp.getNeighborhood())
        print("Condition: " + currTemp.getCondition())
        print("Current Temperature: " + str(math.trunc(currTemp.getTemperature())) + " °C")    
        print("Humidity: " + str(currTemp.getHumidity()) + "%")
        print("--------------------------------")        
    else:
        print("We got an error :(")
        break