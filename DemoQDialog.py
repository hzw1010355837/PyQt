#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dialog对话框使用")
        self.resize(500, 500)

        # 直接将button放在主窗口上
        self.button = QPushButton(self)
        self.button.resize(200, 20)
        self.button.setText("弹出对话框")
        # 移动按钮,无法居中,因为没有使用布局
        self.button.move(100, 100)

        self.button.clicked.connect(self.clickedButton)

    def clickedButton(self):
        dialog = QDialog()
        dialog.setWindowTitle("对话框")
        dialog.resize(200, 200)

        # 没有布局,直接放在对话框里
        button = QPushButton("确定", dialog)
        # button.setText("关闭对话框")
        button.move(50,50)
        button.clicked.connect(dialog.close)
        # 设置主窗口也可用
        dialog.setWindowModality(Qt.WindowModal)

        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    exit(app.exec_())
