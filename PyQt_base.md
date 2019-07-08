



```python
form PyQt5.QWidgets import *
import sys
```

* 主窗口类型:

  * QMainWindow:可以包含菜单栏,工具栏,状态栏
  * QDialog:是对话窗口的基类.没有菜单栏等
  * QWidget:不确定窗口的用途,就是用QWidget:arrow_right:窗口小部件

* 布局:QFormLayout(表单布局), QVBoxLayout(垂直布局) **常用方法addWidget(添加部件)** *最后需要使用setLayout(layout)*

* QLabel:展示文本信息

  * setAlignment():设置文本对齐方式
  * setIndent():设置文本缩进
  * text():获取文本内容
  * setBuddy():设置伙伴关系
  * setText():设置文本内容
  * selectedText():返回所选字符
  * setWordWrap():设置是否允许换行
  * QLabel常用的信号(事件)
    * 当鼠标滑过QLable控件时触发:linkHovered
    * 当鼠标单击QLable控件时触发:linkActivated

* QLineEdit:控件与回显模式
  * 基本功能:输入单行文本
    * setReadOnly()
    * setEchoMode()
    * setValidator()
  * EchoMode:设置回显模式
    1. Nomal
    2. NoEcho:并不显示在屏幕上
    3. Password:密文
    4. PasswordEchoOnEdit:先明文后密文显示
  * QLineEdit控件的输入(校验器)
    * 如整数,浮点数,字母和数字QRegExp(正则给校验器)
    * QRegExpValidator:正则校验器.setPegExp(正则)
    * QIntValidator & QDoubleValidator

* QTextEdit:输入多行文本

* QAbstractButton(所有按钮父类):

  * QPushButton:普通按钮

    * toggle设置开关,与setCheckable(True)搭配

    * **使用lambda表达式连接信号与槽(带参数情况) **

    * ```python
      self.button1.clicked.connect(lambda:self.whichButton(self.button1))
      ```

  * AToolButton

  * QRadioButton:单选按钮控件 多于toggled搭配传递信号

    * btn=**self.sender()获取当前点击按钮控件对象**
    * btn.text()就可以在槽函数内获取文本内容  btn.isChecked()

  * QCheckBox:复选框控件

    * **form PyQt5.QtCore import Qt**包含许多常量
    * 三种状态:0未选中(默认), 1半选中setTristate(True), 2选中setChecked(True)

  * QComboBox:下拉列表控件

    * addItem() & addItems([...])添加下拉选择
    * cb对象获取cb.current.text()获取当前选择文本/cb.itemText(index)获取下拉列表索引位置文本

  * 
