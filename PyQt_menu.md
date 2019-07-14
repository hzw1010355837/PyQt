* 创建和使用菜单

  * ```python
    # 在QMainWindow中
    # TODO 菜单栏(最上方)
    bar = self.menuBar() # 获取菜单栏
    file = bar.addMenu("文件")
    file.addAction("新建")
    # 设置带快捷键
    save = QAction("保存", self)
    save.setShortcut("Ctrl + S")
    file.addAction(save)
    # TODO 工具栏
    tb = self.addToolBar("File")
    new = QAction(QIcon(图片), 文本作为悬停提示, self) # 工具栏默认按钮:只显示图标, 如果有多个时,会在图标右侧显示 
    tb.setToolButtonStyle(Qt.ToolButtonTextOnly) # 设置样式:图标和文本显示
    tb.addAction(new)
    # TODO 状态栏(最下方)
    file.triggered.connect(self.processTrigger)
    self.sb = QStatusBar()
    self.setStatusBar(self.sb) # 设置状态栏
    # 槽函数内
    def processTrigger(self, q):
        if q.text() == "show":
            self.sb.showMessage(q.text(), 5000) # 显示5000ms
    ```

  * question: 为什么菜单栏槽函数内获取文本需要通过 self.sender().text()  ,而工具栏却只需要a.text() ,a代表槽函数的形参?

* 输出到打印机:

  * ```python
    self.editor = QTextEdit("默认文本", self)
    
    printer = QtPrintSupport.Qprinter() # 创建打印机对象
    painter = QPainter()
    painter.begin(printer) # 将绘制的目标重定向到打印机
    screen = self.editor.grab()
    painter.drawPixmap(10,10,screen)
    painter.end()
    ```

    

  * Tips:设置窗口大小时,使用self.resize(w,h)和**self.setGeometry(x,y,w,h)**后者居多

  * 显示打印对话框

    * printDialog = QPageSetupDialog(self.printer, self); printDialog.exec() # 显示打印设置对话框
    * printdialog = QPrintDialog(self.printer, self); printerdialog.exec() # 显示打印对话框~~指定输出格式PDF...~~
    * QTextEdit()对象直接由print()方法可以直接将文本输出至打印机:self.editor.print(self.printer)

