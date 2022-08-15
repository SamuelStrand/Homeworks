import requests
import json

url = "https://api.instantwebtools.net/v1/airlines/"
n = 0
new_url = ""

for num in range(1, 100+1):
    for number in range(0, 1):
        n += 1
    new_url = f'{url}{n}'
    print(new_url)
    response = requests.get(new_url)
    new_url = response.content.decode()
    with open(file=f"Temp_hw/get_many_{num}.json", mode="w", encoding="cp1251") as file:
        json.dump(new_url, file)
# airlines = json.loads(new_url)
# print(type(airlines))
# print(airlines)
# print(type(new_url))
# print(new_url)
