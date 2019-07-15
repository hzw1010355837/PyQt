#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, math


class TreeWidgetDemo(QWidget):
    def __init__(self):
        super(TreeWidgetDemo, self).__init__()
        self.setWindowTitle("TreeWidget")
        self.setGeometry(0, 0, 1000, 1000)
        layout = QHBoxLayout()
        button1 = QPushButton("添加节点")
        button2 = QPushButton("删除节点")
        button3 = QPushButton("修改节点")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        button1.clicked.connect(self.addNode)
        button2.clicked.connect(self.removeNode)
        button3.clicked.connect(self.updateNode)

        layout1 = QVBoxLayout()
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setColumnWidth(0, 200)
        self.tree.setHeaderLabels(["Key", "Value"])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, "root")
        child1 = QTreeWidgetItem(root)
        child1.setText(0, "child1")
        child1.setText(1, "child1_v")
        child2 = QTreeWidgetItem(root)
        child2.setText(0, "child2")
        child2.setText(1, "child2_v")
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, "child3")
        child3.setText(1, "child3_v")


        layout1.addLayout(layout)
        layout1.addWidget(self.tree)
        self.setLayout(layout1)

    def addNode(self, ):
        item = self.tree.currentItem()
        child = QTreeWidgetItem(item)
        child.setText(0, "新节点")
        child.setText(1, "新值")

    def removeNode(self):
        item1 = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems(): # type:QTreeWidgetItem
            (item.parent() or root).removeChild(item)
            # (item.parent() or root).removeChild(item)


    def updateNode(self):
        item = self.tree.currentItem()
        item.setText(0, "新节点")
        item.setText(1, "新值")
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TreeWidgetDemo()
    main.show()
    exit(app.exec_())
