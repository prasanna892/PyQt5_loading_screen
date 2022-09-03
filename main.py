from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from loding_Screen import lode

# Basic empty window creating
class MainWindow_(QWidget):
    def __init__(self):    
        QWidget.__init__(self)

        # setting window properties
        self.width = 610
        self.height = 610
        self.setGeometry(0, 0, self.width, self.height)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.show()  # Display the window

def main():
    if lode(): # display this empty window after loding animation finish
        app = QApplication(sys.argv)
        window = MainWindow_()
        sys.exit(app.exec())

if __name__ == '__main__':
    main()