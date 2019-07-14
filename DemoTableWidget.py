#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, math


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.setWindowTitle("单元表格中搜索Cell和特定行")
        self.setGeometry(0,0,500,500)

        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setColumnCount(4)
        tableWidget.setRowCount(40)

        layout.addWidget(tableWidget)
        for i in range(1, 41):
            for j in range(1,5):
                tableWidget.setItem(i-1,j-1,QTableWidgetItem('({0}, {1})'.format(i,j)))

        # 设置搜索文本
        text = '(13, 1)'
        items= tableWidget.findItems(text, Qt.MatchExactly) # 精确匹配
        if items:
            item = items[0]
            item.setBackground(QBrush(QColor(0, 255,0))) # 设置背景色
            item.setForeground(QBrush(QColor(255, 0,0))) # 设置文字颜色

            row = item.row()
            # 定位到指定行
            tableWidget.verticalScrollBar().setSliderPosition(row)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    exit(app.exec_())
