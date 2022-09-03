from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# Creating loding class
class LodingScreen(QWidget):
    # initializating
    def __init__(self, parent = None):
        super(LodingScreen, self).__init__(parent)

        # Setting window to frameless and transparent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Setting window size
        self.width = 310
        self.height = 310

        # Setting window position
        self.setGeometry(0, 0, self.width, self.height)

        # Centering window position
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        # Initializating timer to update window
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_value)
        self.timer.start(20)    # Wait for 20 miliSecond

        # arc value
        self.value = 0
        self.dot = 1

        self.container1() # loading in % status
        self.container2() # display jarvis text
        self.container3() # display loading text

    # Container1 for showing loding in percentage
    def container1(self):
        # Creating QWidget container_1 and setting its property and style
        self.container_1 = QWidget(self)
        self.container_1.setContentsMargins(0, 0, 0, 0)
        self.container_1.resize(100, 50)
        self.container_1.move((self.width-100)//2, (self.height-50)//2-70)

        # Creating Horizontal layout and setting margin to 0
        self.layoutH = QHBoxLayout(self.container_1)
        self.layoutH.setContentsMargins(0, 0, 0, 0)

        # Creating label l1 and l2 to display text
        self.l1 = QLabel(str(self.value))
        self.l1.setFont(QFont("Times New Roman", 30, 10, True))
        self.l1.setAlignment(Qt.AlignBottom)
        self.l1.setStyleSheet("color: white")
        self.layoutH.addWidget(self.l1)

        self.l2 = QLabel("%")
        self.l2.setFont(QFont("Times New Roman", 20, 60, True))
        self.l2.setStyleSheet("color: white")
        self.l2.setAlignment(Qt.AlignBottom)
        self.layoutH.addWidget(self.l2)

    # Container2 for showing jarvis text
    def container2(self):
        # Creating QWidget container_2 and setting its property and style
        self.container_2 = QWidget(self)
        self.container_2.setContentsMargins(0, 0, 0, 0)
        self.container_2.resize(166, 50)
        self.container_2.move((self.width-166)//2, (self.height-50)//2)

        # Creating Horizontal layout and setting margin to 0
        self.layoutH_2 = QHBoxLayout(self.container_2)
        self.layoutH_2.setContentsMargins(0, 0, 0, 0)
        # remove below line triple qutes if you want full letter
        """self.layoutH_2.setSpacing(0)"""

        # Creating multiple label to display JARVIS in different colour
        self.jarvis1 = QLabel("J")
        self.jarvis1.setFont(QFont("Consolas", 30, 20, True))
        self.jarvis1.setStyleSheet("color: Chocolate")
        self.layoutH_2.addWidget(self.jarvis1)

        self.jarvis2 = QLabel("A")
        self.jarvis2.setFont(QFont("Consolas", 30, 20, True))
        self.jarvis2.setStyleSheet("color: Coral")
        self.layoutH_2.addWidget(self.jarvis2)

        self.jarvis3 = QLabel("R")
        self.jarvis3.setFont(QFont("Consolas", 30, 20, True))
        self.jarvis3.setStyleSheet("color: CornflowerBlue")
        self.layoutH_2.addWidget(self.jarvis3)

        self.jarvis4 = QLabel("V")
        self.jarvis4.setFont(QFont("Consolas", 30, 20, True))
        self.jarvis4.setStyleSheet("color: Gold")
        self.layoutH_2.addWidget(self.jarvis4)

        self.jarvis5 = QLabel("I")
        self.jarvis5.setFont(QFont("Consolas", 30, 20, True))
        self.jarvis5.setStyleSheet("color: Cyan")
        self.layoutH_2.addWidget(self.jarvis5)

        self.jarvis6 = QLabel("S")
        self.jarvis6.setFont(QFont("Consolas", 30, 20, True))
        self.jarvis6.setStyleSheet("color: DarkKhaki")
        self.layoutH_2.addWidget(self.jarvis6)

    # Creating container3 for displaying loding text
    def container3(self):
        # Creating QWidget container_2 and setting its property and style
        self.container_3 = QWidget(self)
        self.container_3.setContentsMargins(0, 0, 0, 0)
        self.container_3.resize(118, 50)
        self.container_3.move((self.width-self.container_3.width())//2, (self.height-self.container_3.height())//2+60)

        # Creating Horizontal layout and setting margin to 0
        self.layoutH_3 = QHBoxLayout(self.container_3)
        self.layoutH_3.setContentsMargins(0, 0, 0, 0)

        # Creating label l3 for displaying loding text
        self.l3 = QLabel("Loding...")
        self.l3.setFont(QFont("Times New Roman", 20, 10, True))
        self.l3.setStyleSheet("color: LawnGreen")
        self.layoutH_3.addWidget(self.l3)
            
    # paint event to draw 
    def paintEvent(self, event):
        # fix drawing in center of window
        draw_width = draw_height = 300
        centerX = (self.width-draw_width)//2
        centerY = (self.height-draw_height)//2

        # Creating QPainter start painting
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing) # for smoothing image

        # color gradiant
        radial = QLinearGradient(QPoint(0, 0), QPoint(self.width, self.height))
        radial.setColorAt( 0.3, QColor(191, 100, 255))
        radial.setColorAt( 0.6, QColor(134, 0, 179))

        #drawing circle
        painter.setPen(QPen(Qt.yellow, 6))
        painter.setBrush(QBrush(radial))
        painter.drawEllipse(centerX+20, centerY+20, 260, 260)

        # drawing loading circle
        painter.setBrush(QBrush())
        painter.setPen(QPen(Qt.gray, 8))
        painter.drawEllipse(centerX, centerY, draw_width, draw_height)

        # drawing loading arc
        painter.setPen(QPen(Qt.green, 8, cap=Qt.RoundCap))
        painter.drawArc(centerX, centerY, draw_width, draw_height, 90 * 16, -self.value * 16)

        # close painter
        painter.end()

    # For changing animation
    def change_value(self):
        # Arc animation by increasing arc value
        self.value += 3
        self.l1.setText(str(int((self.value/360)*100)))   # setting new text to label l1
        self.container_1.adjustSize()   # Dinamically adjust size 
        self.container_1.move((self.width-self.container_1.width())//2, (self.height-self.container_1.height())//2-70) # resetng position
        
        # Animating loding... text
        loding = "Loding"
        dot = "."*self.dot
        if self.value%12 == 0:
            if self.dot < 3:
                self.dot += 1
            else:
                self.dot = 1
        string = loding + dot
        self.l3.setText(string)          # setting new text to label l3
        self.container_3.adjustSize()    # Dinamically adjust size
        
        if self.value >= 363: # stop the animation after 100% lode
            self.timer.stop()
            self.timer1 = QTimer()
            # 500ms delay between close this window
            self.timer1.timeout.connect(self.finish)
            self.timer1.start(500)
        else:  # Else update the class for animation
            self.update()

    # quit this window
    def finish(self): 
        QCoreApplication.instance().quit()

def lode():
    app = QApplication(sys.argv)  # Creating App
    loding_screen = LodingScreen() # defing class
    loding_screen.show()  # Display the window
    app.exec()   # exit from app
    return True 