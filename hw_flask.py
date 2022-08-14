from flask import Flask
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout
import sys

app = Flask(__name__)

lorem_text = 'for_hw_flask.txt'


@app.route("/")
def main():
    return "<h1>main</h1>"


@app.route("/lorem")
def lorem():
    with open(lorem_text, "r", encoding='utf-8') as file1:
        text_web = file1.readlines()
        result = str(text_web)
        return result


with open(lorem_text, "r", encoding='utf-8') as file:
    text = file.readlines()
    new_text = str(text)
    print(text)


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.line_edit = QLineEdit(new_text)
        self.layout.addWidget(self.line_edit)

        self.show()


app_pyside = QApplication(sys.argv)
mw = MainWindow()
app_pyside.exec()
