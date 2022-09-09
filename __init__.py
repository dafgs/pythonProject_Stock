import sys
sys.path.append("C:/Users/SAMSUNG/PycharmProjects/pythonProject_Stock/")
from kiwoom.kiwoom import *
from PyQt5.QtWidgets import *


class Main():
    def __init__(self):
        print("Main() start")

        self.app = QApplication(sys.argv) # sys.argv는 파일명으로 주어진 파일을 인지하고 동시성 처리를 하게끔 함
        self.kiwoom = Kiwoom() # 객체화
        self.app.exec_() # 이벤트루프 실행


        Kiwoom()


if __name__ == "__main__":
    Main()