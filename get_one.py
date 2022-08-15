import requests
import json

url = "https://api.instantwebtools.net/v1/airlines/1"
response = requests.get(url)
json_data = response.content.decode()
airlines = json.loads(json_data)
with open('Temp_hw/get_one.json', 'w') as file:
    json.dump(json_data, file)
print(json_data)
print(type(json_data))