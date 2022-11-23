import requests
from location import Location
from credential import Credential
       
def get_lat_lon(location: Location, credential: Credential, limit: int = 10):
    
    #Cheking if all mandatory information was sent to method
    if not location.country:
        location.error("The country is mandatory to get geo locations details")
        return location
    
    if not location.city:
        location.error("The city is mandatory to get geo locations details")
        return location
    
    if not location.state:
        location.error("The state is mandatory to get geo locations details")
        return location
    
    #Defininf url to the endpoint to get latitude and longitude
    url = f"http://api.openweathermap.org/geo/1.0/direct"
    url += "?q=" + location.city + ",," + location.country
    url += "&limit=" + str(limit)
    url += "&appid=" + credential.appKey

    #Calling API
    response = requests.get(url).json()

    #Cheking if was procces successfuly
    if response:

        #Interation in the cities in the response
        for city in response:
            
            #Just cheking if we are considering the correct state, because it is possible the have cities with same name in differente states.
            if city['state'] == location.state:

                #adding details in the object
                return [ str(city['lat']), str(city['lon']) ]
                
    else:
        location.setError = "We got an error trying to get the location of city: " + city.city
        
    return []