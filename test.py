import requests

api_address='http://api.openweathermap.org/data/2.5/forecast?appid=cd8af2ac28fc48ad9d890c97a82f7d1e&q='

city = input('City:')

url = api_address + city

json_data = requests.get(url).json()

weather = json_data['list'][0]['weather'][0]['description']
temperature = str(float(json_data['list'][0]['main']['temp'])-273.15)
temp_min = str(float(json_data['list'][0]['main']['temp_min'])-273.15)
temp_max = str(float(json_data['list'][0]['main']['temp_max'])-273.15)
humidity = str(json_data['list'][0]['main']['humidity'])
windspeed = str(json_data['list'][0]['wind']['speed'])
datetime = json_data['list'][0]['dt_txt']

print('Date&Time: ' + datetime)
print('Weather: ' + weather)
print('Temperature: ' + temp_min + ' celsius' + ' ~ ' + temp_max + ' celsius') 
print('Humidity: ' + humidity + '%')
print('Windspeed: ' + windspeed + 'm/s')