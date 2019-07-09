#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class TestDemo(QWidget):
    def __init__(self):
        # super().__init__()
        super(TestDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("开始制作GUI")
        self.resize(300, 300)

        # layout = QLayout(QHBoxLayout)
        self.layout = QHBoxLayout()
        self.label = QLabel("当前位置")
        self.label.setAlignment(Qt.AlignCenter)

        self.sb = QSpinBox()
        self.sb.setValue(18)
        self.sb.valueChanged.connect(self.valueChangeSignal)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.sb)
        self.setLayout(self.layout)

    def valueChangeSignal(self):
        value = self.sender().value()
        print(value)
        self.label.setText(str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TestDemo()
    main.show()
    exit(app.exec_())
