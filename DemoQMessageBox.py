#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("消息对话框")
        self.resize(300, 300)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.button = QPushButton()
        self.button.setText("事件信号")
        self.button.clicked.connect(self.messageWindow)

        layout.addWidget(self.button)
        self.setLayout(layout)

    def messageWindow(self):
        QMessageBox().about(self, "关于", "这是一个关于对话框")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    exit(app.exec_())