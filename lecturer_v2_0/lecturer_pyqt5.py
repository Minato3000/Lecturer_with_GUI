from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QTextEdit
import sys

import lecturer_gtts as lg

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("dialog.ui", self)

        self.open_button = self.findChild(QPushButton, "open_button")
        self.file_text = self.findChild(QLabel, "filetext")
        self.file_text.setStyleSheet("background-color: #3A8891")

        self.speak_button = self.findChild(QPushButton, "speak_button")


        self.open_button.clicked.connect(self.clicker)
        self.speak_button.clicked.connect(self.speaker)

        self.show()

    def clicker(self):
        # self.label.setText("U clicked the button")

        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);; Python Files (*.py)")

        file_info = lg.readfile(fname[0])

        if fname:
            self.file_text.setText(file_info)
            text = self.file_text.text()
            lg.textspeech(text)

    def speaker(self):
        lg.speak()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
