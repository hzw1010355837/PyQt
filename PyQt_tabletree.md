* 显示二维表数据:QTableView控件:需要创建QTAbleView实例和一个数据源Model,然后将两者关联 ***MVC:前后分离***

  * 实例对象

    * self.tableview = QTableView()
    * self.tableview.setModel(self.model) # 关联模型

  * 数据源Model

    * self.model = QStandardItemModel(row, col)
    * self.model.setHorizontalHeaderLabels([...]) # 设置行标题:特征
    * 添加数据至表中
      * item = QStandardItem(数据); self.model.setItem(row,col,item)

    > * 扩展表格控件tableWidget  = QTableWidget() : QTable子类 增加了许多信号
    >   * tableWidget.setColumnCount(3); tableWidget.setRowCount(4) :4行3列
    >   * 每一个Cell(单元格) 是一个QTableWidgetItem,默认是可以编辑  为单元格添加数据
    >   * item = QTableWidgetItem("张三"); tableWidget.setItem(row, col, item)
    >     * 禁止编辑 tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    >     * 整z行选择 tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
    >     * 调整行和列:根据输入的数据调整行和列 tableWidget.resizeColumnsToContents(); tableWidget.resizeRowsToContents()
    >     * 设置隐藏头: tableWidget.horizontalHeader().setVisible(False)   : table Widget.setHorizontalHeaderLabels(["姓名", "年龄", "籍贯"])
    >     * 自定义列的头: tableWidget.setVerticalHeaderLabels(["a"])
    >     * 设置隐藏表格线: tableWidget.setShowGrid(False)
    >   * 

> * 显示列表数据: QListView控件
>
>   > * ```python
>   >   listView = QListView()
>   >   listModel = QStringListModel() 
>   >   listModel.setStringList(列表数据) # 将数据添加至model
>   >   listView.setModel(listModel) # 将model添加至view
>   >   ```
>   >
>   > * QListWidget():扩展列表控件 QListView子类
>   >
>   >   * 添加数据与上面有所不同
>   >     * 可以使用addItem(数据)
>   >     * listWidget = QListWidget(); listWidget.addItem(数据1);...;self.setCentralWidget(self.listWidget)
>   >     * 在槽函数内获取点击的是哪个列表数据: self.listWidget.item(**self.listWidget.row(Index).text()**)



> * 如何在单元格内放置控件tableWidget.setCellWidget(row,col,item)
>   * QSS类似CSS,设置控件样式: **cb.setStyleSheet('QComboBox{margin:3px}')**设置所有QComboBox边距3px
>   * cb = QComboBox(); cb.addItems(["男", "女"]); tableWidget.setCellWidget(row,col,cb)

> * 在表格中快速定位到特定的行
>
>   * Qt.MatchStartsWith # 以指定字符串开头的都将匹配
>
>   1. 数据的定位: findItems
>
>      * tableWidget.finditems(text,Qt.MatchExactly) # 文本精确匹配
>
>      * item.setBackground(QBrush(QColor(红,绿,蓝))) # 设置选中文本背景色
>      * item.setForeground(QBrush(QColor(红,绿,蓝))) # 设置选中文本颜色
>      * 定位到指定行(需要用到滚动条): tableWidget.**verticalScrollBar()**.setSliderPosition(row)
>
>   2. 如找到指定单元格, 会定位到单元格所在的行: setSliderPosition(row)

* 设置单元格字体大小颜色
  * item = QTableWidgetitem("文本"); item.setFont(QFont("Times~~字体~~", 14, QFont.Black))

> * 单元格按列排序: orderType = Qt.DescendingOrder
>   * 1,按哪一列排序 2,排序类型
>   * tableWidget.sortItems(columnIndex, orderType)

> * 设置单元格文本对齐方式: item.setTexyAlignment(Qt.Alignright | Qt.AlignBottom)

> * 合并单元格: setSpan(row,col,要合并的行数,要合并的列数)

> * 设置单元格尺寸: tableWidget.setRowHeight(row_index, height): setColumnWidth(col_index,width)

> * 单元格实现图文混合: item = QTableWidgetItem(QIcon(图像路径), '描述文字')
>   * 更改图片尺寸: tableWidget.setIconSize(QSize(w,h))
>     * 为了单元格也适应图片大小 : tableWidget.setColumnWidth(index, w); tableWidget.setRowHeight(index, h)

> * 表格中添加上下文菜单: tableWidget.setConetextMenuPolicy(Qt.CustomContextMenu)
>
>   * QMenu.exec_
>
>   * 表格上下文菜单请求信号: tableWidget.customContextMenuRequested.connect(generateMenu)
>
>   * tableWidget.selectionModel().selection().indexes() 返回被选中的row索引
>
>   * ```python
>     def generateMenu(self, pos)
>     	menu = QMenu()
>         menu.addAction("...")
>         # 会被阻塞, 直到被中选择菜单项
>         # pos需要转换,不转换会导致菜单选项会出现在全屏对应位置
>         screenPos = tableWidget.mapToGlobal(pos)
>         action = menu.exec(screenPos)
>     ```

> * 树控件: QTreeWidget
>
>   * ```python
>     tree = QTreeWidget()
>     tree.setColumnCount(2) # 指定列数
>     tree.setColumnWidth(0, 120) # 设置列宽
>     tree.setHeaderLabels(["Key","Value"]) # 指定列标签
>     
>     root = QTreeWidgetItem(tree) # 添加根节点 重要
>     root.setText(0, "根节点") 
>     root.setIcon(0, QIcon('图标'))
>     
>     child = QTreeWidgetItem(root) # 添加子节点
>     child.setText(0, "子节点") 
>     child.setText(1, "描述子节点")
>     child.setIcon(0, QIcon('图标'))
>     child.setCheckState(0, Qt.Checked) # 为子节点添加复选框
>     
>     self.setCentralWidget(self.tree) # 使树控件充满整个屏幕
>     ```
>
>     * 添加响应事件 **查看事件是否携带参数,可以追踪接口里的信号是否带有参数**
>       * item = tree.currentItem()  # 可以获取当前点击对象
>       * item.text(列索引) # 获取文本 index.row() # 获取当前行索引
>
>   * 动态添加\删除\修改树控件节点
>
>     * ```python
>       root = self.tree.invisibleRootItem() # 删除根节点时,需要先创建虚拟根节点的根节点
>       for item in self.tree.selectedItems(): # type:QTreeWidgetItem
>           (item.parent() or root).removeChild(item) # 上面注释,可让下面代码有提示功能,即指定了item类型
>       ```
>
> * QTreeView控件与系统定制模式: view->model搭配使用
>
>   * QDirModel
>
>   * ```python
>     model = QDirModel()
>     tree = QTreeWidget()
>     tree.setModel(model)
>     tree.show()
>     ```

