import sys
import PySide6.QtWidgets as QtWidgets
from PySide6.QtWidgets import QMainWindow, QPushButton, QSpinBox


class ExampleWindow(QMainWindow):
    def __init__(self, window_name: str):
        super().__init__()

        self.window_name = window_name
        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle(self.window_name)
        self.layout = QtWidgets.QGridLayout()

        self.spin = QSpinBox(self)
        self.spin.setGeometry(120, 0, 100, 40)

        self.button = QPushButton("Press Me!", self)
        self.layout.addWidget(self.button, 0, 0)
        self.button.clicked.connect(self.create_files)

    def create_files(self):
        for num in range(1, int(self.spin.value()) + 1):
            with open(f'Temp_hw/new_file{num}.txt', 'w') as file:
                file.write('')
        print('done')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ExampleWindow('Наше приложение на PySide6')
    ex.show()
    sys.exit(app.exec())
