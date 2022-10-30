def getCredentials():
    appKey = "9c2e93f176d25559234a3d43712a506e"
    return appKey

def getCurrentWeather(appKey, lat, lon):
    
    if not appKey:
        return "App Key is mandatory to get current weather"

    if not lat:
        return "Latitude is mandatory to get current weahter"
    
    if not lon:
        return "Longitude is mandatory to get current weather"

    url = getBaseUrl("current")
    if not url:
        return "Base URL for current weather was not found."    

    url += "?lat=" + lat
    url += "&lon=" +lon
    url += "&appid=" + appKey

    return

def getBaseUrl(cOption):

    if cOption == "current":
        return "https://api.openweathermap.org/data/2.5/weather"
    
    return ""
