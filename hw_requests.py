import json

import requests

url1 = 'https://picsum.photos/300/300/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

# TASK 1
response = requests.get(url=url1, headers=headers)
print(response.status_code)

with open('Temp_hw/photo.jpg', mode='wb') as file:
    file.write(response.content)

# TASK 2
index = 0
for i in range(1, 20):
    index += 1
    url2 = f'https://jsonplaceholder.typicode.com/photos/{index}'
    response2 = requests.get(url=url2)

    # Формирование текстового файла(json)
    with open(f'Temp_hw/hw_json_{index}.json', mode='w') as file:
        file.write(response2.text)


# TASK 3
index = 0
for i in range(1, 20):
    index += 1
    url2 = f'https://jsonplaceholder.typicode.com/photos/{index}'
    response2 = requests.get(url=url2)

    # Поиск ссылки по ключу
    unique_url = response2.json()['url']

    # Сохранение фото
    with open(f'Temp_hw/hw_photo_{index}.jpg', mode='w') as file:
        json.dump(unique_url, fp=file)
