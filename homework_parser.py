import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
import sys
import time
from threading import Thread
from datetime import datetime

url = 'https://myfin.by/converter'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
html = soup.prettify("utf-8")

dollar_exchange_data = 0.0
euro_exchange_data = 0.0
gbp_exchange_data = 0.0
cny_exchange_data = 0.0
rub_exchange_data = 0.0

with open('Temp_hw/data.html', 'a') as f:
    f.write(str(html))
    f.close()


def get_exchange_rate():
    while True:
        global dollar_exchange_data
        global euro_exchange_data
        global gbp_exchange_data
        global cny_exchange_data
        global rub_exchange_data
        if response.status_code == 200:
            exchange_data = soup.find_all('div', class_='record vis_bestmbusd')
            # print(exchange_data)
            dollar_exchange_data = str(exchange_data).split(sep='value=')[-1].split("/")[0].split('"')[1]
            # print(new_exchange_data)
            dollar = {'dollar': dollar_exchange_data}
            print(dollar)

            exchange_data = soup.find_all('div', class_='record vis_bestmbeur')
            euro_exchange_data = str(exchange_data).split(sep='value=')[-1].split("/")[0].split('"')[1]
            euro = {'euro': euro_exchange_data}
            print(euro)

            exchange_data = soup.find_all('div', class_='record vis_bestmbgbp')
            gbp_exchange_data = str(exchange_data).split(sep='value=')[-1].split("/")[0].split('"')[1]
            gbp = {'gbp': gbp_exchange_data}
            print(gbp)

            exchange_data = soup.find_all('div', class_='record vis_bestmbcny')
            cny_exchange_data = str(exchange_data).split(sep='value=')[-1].split("/")[0].split('"')[1]
            cny = {'cny': cny_exchange_data}
            print(cny)

            exchange_data = soup.find_all('div', class_='record vis_bestmbrub')
            rub_exchange_data = str(exchange_data).split(sep='value=')[-1].split("/")[0].split('"')[1]
            rub = {'rub': rub_exchange_data}
            print(rub)

            current_datetime = datetime.now()
            seconds_now = current_datetime.second
            seconds = int(seconds_now)
            if seconds > 10 and seconds % 2 != 0:
                print(seconds, "курс обновлен")
                time.sleep(2)

            elif seconds % 2 != 0 and seconds < 10:
                print("нет десятка (курс будет обновлен через 9 секунд)", seconds)
                time.sleep(9)


Thread(target=get_exchange_rate).start()


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label_head1 = QLabel("Конвертер по лучшему курсу в Москве!")
        layout.addWidget(self.label_head1)

        self.label_head = QLabel("Введите сумму в долларах:")
        layout.addWidget(self.label_head)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label_dollar = QLabel()
        layout.addWidget(self.label_dollar)

        self.label_euro = QLabel()
        layout.addWidget(self.label_euro)

        self.label_gbp = QLabel()
        layout.addWidget(self.label_gbp)

        self.label_cny = QLabel()
        layout.addWidget(self.label_cny)

        self.label_rub = QLabel()
        layout.addWidget(self.label_rub)

        self.line_edit.textChanged.connect(self.line_edit_text_changed_dollar)
        self.line_edit.textChanged.connect(self.line_edit_text_changed_euro)
        self.line_edit.textChanged.connect(self.line_edit_text_changed_gbp)
        self.line_edit.textChanged.connect(self.line_edit_text_changed_cny)
        self.line_edit.textChanged.connect(self.line_edit_text_changed_rub)

        self.show()

    def line_edit_text_changed_dollar(self, text_dollar):
        try:
            text_dollar = round(float(dollar_exchange_data) * float(text_dollar), 3)
            self.label_dollar.setText("Ваша сумма в долларах:   " + str(text_dollar) + "  " + " $")
        except Exception as error:
            self.label_dollar.setText('ошибка ввода данных')

    def line_edit_text_changed_euro(self, text_euro):
        try:
            text_euro = round(float(euro_exchange_data) * float(text_euro), 3)
            self.label_euro.setText("Ваша сумма в евро:   " + str(text_euro) + "  " + "Евро")
        except Exception as error:
            self.label_euro.setText('ошибка ввода данных')

    def line_edit_text_changed_gbp(self, text_gbp):
        try:
            text_gbp = round(float(gbp_exchange_data) * float(text_gbp), 3)
            self.label_gbp.setText("Ваша сумма в фунтах стерлингов:   " + str(text_gbp) + "  " + "Фунтов стерлингов")
        except Exception as error:
            self.label_gbp.setText('ошибка ввода данных')

    def line_edit_text_changed_cny(self, text_cny):
        try:
            text_cny = round(float(cny_exchange_data) * float(text_cny), 3)
            self.label_cny.setText("Ваша сумма в китайских юань:   " + str(text_cny) + "  " + "Китайских юань")
        except Exception as error:
            self.label_cny.setText('ошибка ввода данных')

    def line_edit_text_changed_rub(self, text_rub):
        try:
            text_rub = round(float(rub_exchange_data) * float(text_rub), 3)
            self.label_rub.setText("Ваша сумма в рублях:   " + str(text_rub) + "  " + "рублей")
        except Exception as error:
            self.label_rub.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow()
app.exec()
