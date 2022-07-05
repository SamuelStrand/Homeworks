import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from threading import Thread

hours = 0
minutes = 0
seconds = 0

pause = True


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.button_start = QPushButton('Start')
        self.layout.addWidget(self.button_start, 1, 6)
        self.button_start.clicked.connect(self.start_new_thread)

        self.button_stop = QPushButton('Stop')
        self.layout.addWidget(self.button_stop, 1, 7)
        self.button_stop.clicked.connect(self.stop_timer)

        self.button_reset = QPushButton('Reset')
        self.layout.addWidget(self.button_reset, 1, 8)
        self.button_reset.clicked.connect(self.reset_timer)

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

        self.show()

    def stop_timer(self):
        global pause

        pause = False
        print('paused')

    def reset_timer(self):
        global hours
        hours = 0
        global minutes
        minutes = 0
        global seconds
        seconds = 0

        self.hours_label.setText("00")
        self.minutes_label.setText("00")
        self.seconds_label.setText("00")

        print("Already reset")

    def start_timer(self):
        global pause

        pause = True

        global hours
        global minutes
        global seconds

        while pause is True:
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

            time.sleep(1)
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
