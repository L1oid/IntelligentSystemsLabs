import requests

api_key = "f9a79194-9733-4df6-a725-7891a7e4a167"

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Барнаул&format=json")
json_response = response.json()
city = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
city_region = city["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
print("Барнаул: " + city_region)

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Мелеуз&format=json")
json_response = response.json()
city = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
city_region = city["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
print("Мелеуз: " + city_region)

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Йошкар-Ола&format=json")
json_response = response.json()
city = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
city_region = city["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
print("Йошкар-Ола: " + city_region)