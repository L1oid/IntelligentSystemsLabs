import requests

response = requests.get("https://static-maps.yandex.ru/1.x/?ll=88.365701%2C54.605293&spn=2.5,2.9&l=map&" +
                        "pl=86.107338%2C55.338070,86.213270%2C55.175653,86.229957%2C55.153833,86.278425%2C54.849400," +
                        "86.208463%2C54.801052,86.229035%2C54.741636,86.173111%2C54.665867,86.323659%2C54.582647," +
                        "86.350774%2C54.539580,86.365844%2C54.494871,86.519405%2C54.233129,86.805692%2C54.056053," +
                        "86.902603%2C53.818733,87.140770%2C53.758963,87.186473%2C53.486263,87.128217%2C53.320871," +
                        "87.148293%2C53.310017,87.129996%2C53.225853,87.524175%2C53.099552,87.673337%2C53.036962,87.736649%2C52.980124," +
                        "87.769463%2C52.898835,87.862995%2C52.890680,87.987732%2C52.929364")
map_pic = "road.png"
with open(map_pic, "wb") as file:
    file.write(response.content)