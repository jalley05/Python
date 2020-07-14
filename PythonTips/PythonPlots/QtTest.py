import sys
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.uic.properties import QtGui


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Stability')

        extractAction = QAction('&Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

        button = QPushButton('Start Recording',self)
        button.clicked.connect(self.startRecording)
        button.move(50,200)
        self.show()

    def startRecording(self):
        print("Show")
        #self.store = showgraph()

    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

if __name__ == "__main__":

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
