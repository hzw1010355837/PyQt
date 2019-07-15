> * 容器控件: 目的在屏幕上显示更多控件 :多个窗口,多个页面实现
>   * 多页面
>     * QTabWidget : **创建类时继承此类**
>
>       * ```python
>          tab1 = QWidget() # 创建显示页面窗口
>          tab2 = QWidget()
>          tab3 = QWidget()
>          ```
>
>      self.addTab(tab1, "选项卡1")
>      self.addTab(tab2, "选项卡2")
>      self.addTab(tab3, "选项卡3")
>
>      self.setTabText(index, "控件名1")
>      ```
>     
>     * 堆栈窗口控件: QStackedWidget
>     
>       * 通过索引切换栈页面
>     
>       * ```python
>      self.list = QListWidget()
>      self.list.insertItem(0, "联系方式")
>      self.list.insertItem(1, "个人信息")
>      self.list.insertItem(2, "教育程度")
>      stack1 = QWidget()
>      self.stack = QStackedWidget() # 创建堆栈控件对象
>      self.stack.addWidget(stack1)
>      ...
>      self.list.currentRowChanged.connect(self.display)
>      
>      def display(self, index):
>          self.stack.setCurrentIndex(index) # 根据索引切换栈里面页面
>      ```
>
>     * 停靠窗口控件: QDockWidget
>       * self.items = QDockWidget("name", self)
>       * self.items.setWidget(其他控件~~QListWidget~~) # 
>       * self.items.setFloating(True) # 设置默认悬浮状态
>       * self.addDockWidget(Qt.RightDockWidgetArea, self.items) # 添加,并设置位置

> * 容纳多文档窗口:QMdiArea&QMdiSubWindow  将窗口添加至容器
>
>   * 层叠,平铺两种模式
>
>   * ```python
>     self.mdi = QMdiArea()
>     self.setCentralWidget(self.mdi)
>     bar = self.menuBar()
>     file = bar.addMenu("File")
>     file.addAction("New")
>     file.triggered.connect(self.windowaction)
>     
>     def windowaction(self, q):
>         if q.text() == "New":
>             MultiWindows.count += 1
>             sub = QMdiSubWindow()
>             sub.setWindowTitle("child" + str(MultiWindows.count))
>             sub.setWidget(QTextEdit())
>             self.mdi.addSubWindow(sub)
>             sub.show()
>         elif q.text() == "cascade":
>             self.mdi.cascadeSubWindows() # 设置层叠
>             self.mdi.titleSubWindows() # 设置平铺
>     ```

> * 滚动条控件: QScrollBar 通过滚动条值变化控制状态和位置变化
>   * sc = QScrollBar(); sc.setMaximum(255); palette = Qpalette() 调色板

> * 多线程: QTimer&QThread