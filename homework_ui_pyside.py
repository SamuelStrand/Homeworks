from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton, QSlider, \
    QComboBox, QVBoxLayout
import sys
import time
from threading import Thread

hours = 0
minutes = 0
seconds = 0

pause = True


def stop_timer():
    global pause

    pause = False


def reset_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0
    hours_label.config(text=f"{hours}")
    minuts_label.config(text=f"{minutes}")
    seconds_label.config(text=f"{seconds}")


# def start_timer():
#     global pause
#
#     pause = True
#
#     global hours
#     # hours = 0
#     global minutes
#     # minutes = 0
#     global seconds
#     # seconds = 0
#
#     # код до цикла
#     while pause:
#         # seconds = seconds + 1
#         seconds += 1
#
#         if seconds > 59:
#             minutes += 1
#             seconds = 0
#
#         if minutes > 59:
#             hours += 1
#             minutes = 0
#
#         if hours > 23:
#             seconds = 0
#             minutes = 0
#             hours = 0

# time.sleep(0.00001)

# hours_label.config(text=f"{hours}")
# minuts_label.config(text=f"{minutes}")
# seconds_label.config(text=f"{seconds}")
# print(f"{hours}:{minutes}" + ":" + str(seconds))


# # определение(создание) функции
# def start_new_thread():
#     Thread(
#         target=start_timer
#     ).start()  # Используйте для вызова функции в отдельный поток, тогда остальная часть окна не
#     # будет виснуть


class MainWindow(QWidget):
    def __init__(self, width=640, heigth=480, title='calculator'):
        QWidget.__init__(self)

        layout = QGridLayout
        self.setLayout(self.layout())

        self.setWindowTitle(title)
        self.resize(width, heigth)

        self.push_button_start = QPushButton('Start')
        # self.push_button_start.clicked.connect()
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        # layout.addWidget(self.push_button_start, 1, 1)
        self.layout.addWidget(self.push_button_start, 7, 1)

        self.show()

    # def start_timer:
    #         global pause
    #
    #         pause = True
    #
    #         global hours
    #         # hours = 0
    #         global minutes
    #         # minutes = 0
    #         global seconds
    #         # seconds = 0
    #
    #         # код до цикла
    #         while pause:
    #             # seconds = seconds + 1
    #             seconds += 1
    #
    #             if seconds > 59:
    #                 minutes += 1
    #                 seconds = 0
    #
    #             if minutes > 59:
    #                 hours += 1
    #                 minutes = 0
    #
    #             if hours > 23:
    #                 seconds = 0
    #                 minutes = 0
    #                 hours = 0


app = QApplication(sys.argv)
mw = MainWindow()
app.exec()
