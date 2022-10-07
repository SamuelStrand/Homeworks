import json
import requests
from openpyxl import Workbook

url = 'https://jsonplaceholder.typicode.com/todos/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
data = response.json()
data_arr = []
for i in response.json():
    data_arr.append(i)


class Api:
    def __init__(self, url1):
        self.url = url1
        self.response = requests.get(url=self.url)
        self.data = self.response.json()
        self.my_status_code = self.response.status_code
        self.empty_arr = []

    def get_status_code(self):
        return self.my_status_code

    def get_all_data(self):
        return self.data

    def create_empty_arr(self):
        print('Array has been created')
        return self.empty_arr

    def get_data_one_by_one(self):
        for j in self.data:
            self.empty_arr.append(j)
        return self.empty_arr

    @staticmethod
    def save_to_json_file():
        data1 = json.dumps(data_arr)
        print(data_arr)
        with open('Temp_hw/data123.json', mode='w') as file:
            file.write(data1)
            return True

    def save_to_many_jsons(self):
        for num in range(1, 30 + 1):
            self.url = f'https://jsonplaceholder.typicode.com/todos/{num}'
            response3 = requests.get(self.url)
            data3 = response3.json()
            with open(f'Temp_hw/data{num}.json', mode='w') as file:
                file.write(str(data3))

    @staticmethod
    def read_all_jsons():
        arr4 = []
        for num2 in range(1, 31):
            directory = f'Temp_hw/data{num2}.json'
            with open(directory, mode='r') as new_file:
                content = new_file.read()
                arr4.append(content)
        return arr4

    @staticmethod
    def write_to_excel():
        arr5 = Api.read_all_jsons()
        wb = Workbook()
        ws = wb.active
        for n in range(1):
            for m in range(1, 30):
                ws[f'A{m}'] = arr5[m]

        wb.save("Temp_hw/json_table.xlsx")


obj = Api(url1=url)
obj.write_to_excel()
