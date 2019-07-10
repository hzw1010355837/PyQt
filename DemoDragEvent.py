#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, math


class ComboBoxDemo(QComboBox):
    def __init__(self):
        super(ComboBoxDemo, self).__init__()
        self.addItem("Java")
        self.setAcceptDrops(True)

    def dropEvent(self, event):
        # super(ComboBoxDemo, self).dropEvent(event)
        print(event.mimeData().text())
        self.addItem(event.mimeData().text())

    def dragEnterEvent(self, event):
        # super(ComboBoxDemo, self).dragEnterEvent(event)
        # print(event.mimiData().text())
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

# class DragEventDemo(QMainWindow):
class DragEventDemo(QWidget):
    def __init__(self):
        super(DragEventDemo, self).__init__()
        self.setWindowTitle("支持拖拽案例")

        # 创建form layout
        formlayout = QFormLayout()

        formlayout.addRow(QLabel("将左边选中文字拖拽至右边下拉列表控件"))
        cb = ComboBoxDemo()
        ld = QLineEdit("Python")
        ld.setDragEnabled(True)
        formlayout.addRow(ld, cb)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DragEventDemo()
    main.show()
    exit(app.exec_())