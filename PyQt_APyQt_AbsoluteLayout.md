> * 通过move方法实现

> * Signal&Slot
>
>   * pyqtSignal() 自定义信号 # 设置为类属性
>
>   * sendmsg  = pyqtSignal(object) # 定义并设置传递参数为对象,也可指定多参 pyqtSignal(str, int, int)
>
>   * 重载注意
>
>     * signal = pyqtSignal([str, int], [int]) 使用[]指定重载参数数量和类型
>     * 使用时也应当注意,只接收int类型时:信号连接方式 self.signal[int].connect(self.signalCall) 
>
>   * 信号槽N对N连接与断开连接
>
>     * 信号与槽:一对多,多对一
>
>   * 窗口类添加信号
>
>   * 信号与槽自动连接
>
>     * ```python
>        def __init__(self):
>        super(...)
>        btn = QPushButton("ok", self)
>        btn.setObjectName("btn") # 为按钮设置一个名字,与槽函数有规律: on_objectname_signalname
>        QtCore.QMetaObject.connectSlotsByName(self) # 统一调用连接
>        ```
>
>    @QtCore.pyqtSlot()
>    def on_btn_click(self):
>    	print("OK")
>
>    ```
>   
>    ```

> * 使用QSS为标签和按钮添加背景图
>
> * image  = QImage(filename)
>   * result = img.scaled(label1.width(), label1.height(), Qt.IgnoreAspectRatio~~忽略缩放比例, Qt.SmoothTransformation~~尽可能平滑显示~~)
> * label1.setPixmap(QPixmap.formImage(result))

