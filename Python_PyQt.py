import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()
        self.menubar()

    def initui(self):
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("icon.png"))

        bnt = QPushButton("Button1", self)
        bnt.move(10, 30)

        bnt1 = QPushButton("Button2", self)
        bnt1.move(10, 70)

        bnt.clicked.connect(self.btn_clicked)   # (QApplication.instance().quit)     이벤트 수행 후 종료
        bnt1.clicked.connect(self.btn_clicked1)

    def menubar(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요")

        menu = self.menuBar() # 메뉴 객체 생성
        menu_file = menu.addMenu("file")   # 그룹 생성 인스턴트
        menu_edit = menu.addMenu("edit")   # 그룹 생성 인스턴트

        file_exit = QAction("exit", self)   # 액션 객체 생성
        file_exit.setShortcut("ctrl+Q")  # 액션 툴팁 인스턴트

        file_new = QMenu("New", self)  # 매뉴 객체 생성

        menu_file.addMenu(file_new)  # 인스턴트
        menu_edit.addAction(file_exit)  #인스턴트


    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ans == QMessageBox.Yes:
            QCloseEvent.accept()    # accept 동의(익셉트)
        else:
            QCloseEvent.ignore()     # ignore 무시하다(이그놀)

    def btn_clicked(self):
        print("Button1 Click (1.버튼 클릭)")

    def btn_clicked1(self):
        print("Button2 Click (2.클릭 버튼)")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())