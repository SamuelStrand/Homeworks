import json

from bs4 import BeautifulSoup
import requests

url_1 = 'https://myfin.by/converter'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

# TASK 1
response = requests.get(url=url_1, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

exchange_dollar_data = soup.find_all('input', {'id': 'nbrb_usd'})
str_dollar_data = str(exchange_dollar_data)
dollar_value = str_dollar_data.split('value="')[1].split('"')[0]
print(f'Доллар: {dollar_value}')

exchange_rub_data = soup.find_all('input', {'id': 'nbrb_rub'})
str_rub_data = str(exchange_rub_data)
rub_value = str_rub_data.split('value="')[1].split('"')[0]
print(f'Рубль: {rub_value}')

print(f'{dollar_value}$ = {rub_value}rub ')

# TASK 2
index = 0
for i in range(1, 11):
    url_2 = 'https://picsum.photos/100/100/'
    response2 = requests.get(url=url_2, headers=headers)
    index += 1
    with open(f'Temp_hw/photo{index}.jpg', mode='wb') as file:
        file.write(response2.content)

# TASK 3

url3 = 'https://goweather.herokuapp.com/weather/%7Bcity%7D'

response3 = requests.get(url=url3, headers=headers)
api = response3.json()
temperature = api['temperature']
wind = api['wind']
description = api['description']
forecast_day1 = api['forecast'][0]
forecast_day2 = api['forecast'][1]
forecast_day3 = api['forecast'][2]
print(f"""      Weather Today:
Temperature = {temperature}
Wind = {wind}
Description: {description}
Forecast for 3 days:
    1st day: {forecast_day1}
    2nd day: {forecast_day2}
    3rd day: {forecast_day3}
""")
