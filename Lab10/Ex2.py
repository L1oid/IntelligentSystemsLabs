import requests

api_key = "f9a79194-9733-4df6-a725-7891a7e4a167"

#а
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Якутск&format=json")
print(request.text)
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Магадан&format=json")
print(request.text)

#b
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Ленинск-Кузнецкий&format=json")
print(request.text)
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Торонто&format=json")
print(request.text)

#c
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Хабаровск&format=json")
print(request.text)
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Уфа&format=json")
print(request.text)
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Нижний+Новгород&format=json")
print(request.text)
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Калининград&format=json")
print(request.text)
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Ленинск-Кузнецкий&format=json")
print(request.text)

#c
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Кемерово,+ул.+Красная+6&format=json")
print(request.text)