import requests

 
url = f"http://api.openweathermap.org/geo/1.0/direct?q=Manaus,,BR&limit=5&appid=9c2e93f176d25559234a3d43712a506e"
#Calling API
response = requests.get(url).json() 

print(response)