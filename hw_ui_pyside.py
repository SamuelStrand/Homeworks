import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton, QSlider, \
    QComboBox, QVBoxLayout
from threading import Thread

        # hours_label.config(text=f"{hours}")
        # minuts_label.config(text=f"{minutes}")
        # seconds_label.config(text=f"{seconds}")
        # print(f"{hours}:{minutes}" + ":" + str(seconds))


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

    # hours_label.config(text=f"{hours}")
    # minuts_label.config(text=f"{minutes}")
    # seconds_label.config(text=f"{seconds}")


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.button_start = QPushButton('Start')
        self.layout.addWidget(self.button_start, 1, 6)
        self.button_start.clicked.connect(self.start_new_thread)
        # self.button_start.clicked.connect(start_timer)

        self.hours_label = QLabel('00')
        self.layout.addWidget(self.hours_label, 0, 1)

        self.hours_colon = QLabel(':')
        self.layout.addWidget(self.hours_colon, 0, 2)

        self.minutes_label = QLabel('00')
        self.layout.addWidget(self.minutes_label, 0, 3)

        self.hours_colon2 = QLabel(':')
        self.layout.addWidget(self.hours_colon2, 0, 4)

        self.seconds_label = QLabel('00')
        self.layout.addWidget(self.seconds_label, 0, 5)

        self.button_stop = QPushButton('Stop')  # экзампляр строки ввода текста
        self.layout.addWidget(self.button_stop, 1, 7)

        self.button_reset = QPushButton('Reset')  # экзампляр строки ввода текста
        self.layout.addWidget(self.button_reset, 1, 8)

        self.show()
    def start_timer(self):
        pause = True
        self.pause = pause
        hours = 0
        minutes = 0
        seconds = 0

        while pause:
            seconds += 1
            if seconds > 59:
                minutes += 1
                seconds = 0
                if minutes > 59:
                    hours += 1
                    minutes = 0
                    if hours > 23:
                        seconds = 0
                        minutes = 0
                        hours = 0
            time.sleep(0.01)
            self.hours_label.setText(str(hours))
            self.minutes_label.setText(str(minutes))
            self.seconds_label.setText(str(seconds))
            print(f"{hours}:{minutes}:{seconds}")

            print(seconds)

    def start_new_thread(self):
        Thread(
            target=self.start_timer
        ).start()


app = QApplication(sys.argv)
mw = MainWindow()
app.exec()
