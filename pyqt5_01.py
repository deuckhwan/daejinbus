import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('PUSH ME!', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('툴팁입니다~')
        btn.move(20, 20)

        self.show()
app = QApplication(sys.argv)
w =  Exam()
sys.exit(app.exec_())