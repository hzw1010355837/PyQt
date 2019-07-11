```python
from PyQt5.QtCore import *
from PyQt5.QtGui import *
form PyQt5.QtWidgets import *
import sys
```

* 主窗口类型:

  * QMainWindow:可以包含菜单栏,工具栏,状态栏
  * QDialog:是对话窗口的基类.没有菜单栏等
  * QWidget:不确定窗口的用途,就是用QWidget:arrow_right:窗口小部件

* 布局:QFormLayout(表单布局), QGridLayout(栅格布局), QVBoxLayout(垂直布局) **常用方法addWidget(添加部件) ** *最后需要使用setLayout(layout)*

  * QFormLayout中添加控件:按行添加layout.addRow(*args)

* 查看信号可以直接进入**源代码搜索signal** (QAbstractButton内有,QPushButton只是继承而已)

  ----

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

  * QToolButton

  * QRadioButton:单选按钮控件 多于toggled搭配传递信号

    * btn=**self.sender()获取当前点击按钮控件对象**
    * btn.text()就可以在槽函数内获取文本内容  btn.isChecked()

* QCheckBox:复选框控件

  * **form PyQt5.QtCore import Qt**包含许多常量
  * 三种状态:0未选中(默认), 1半选中setTristate(True), 2选中setChecked(True)

* QComboBox:下拉列表控件

  * addItem() & addItems([...])添加下拉选择
  * cb对象获取cb.current.text()获取当前选择文本/cb.itemText(index)获取下拉列表索引位置文本

* QSpinBox:计数器控件

  *  信号与槽之间触发,当值发生变化时sb.valueChanged.connect()

* QSlider:滑块控件

  * setTickPosition(QSlider.TickBelow)设置刻度的位置,刻度在下方
  * setTickInterval(6)设置刻度间隔
  * 获取刻度值:slider.value()
  * **信号使用**:slider.valueChanged.connect(槽)
  * **与之相同,当多个信号与槽绑定时,获取当前绑定信号对象使用self.sender()**

* QDialog:对话框

  * ```python
    # 设置主窗口也可用Qt.NonModal,Qt.WindowModal,Qt.ApplicationModal
    # 模态、非模态、半模态窗口
    # 窗口级模态对话框，即只会阻塞父窗口、父窗口的父窗口及兄弟窗口
    # 应用程序级模态对话框，即会阻塞整个应用程序的所有窗口
    dialog.setWindowModality(Qt.WindowModal)
    ```

  * QMessageBox

    * 显示对话框图标可能不同,显示按钮不一样

    1. 关于对话框:`QMessageBox.about(self, 对话框title,对话框内容)`
    2. 错误对话框:`QMessageBox.information(self, 对话框title,对话框内容, QMessageBox.Yes | QMessageBox.No, 默认Enter键 QMessageBox.Yes)`
    3. 警告对话框:QMessageBox.warning
    4. 提问对话框:QMessageBox.question
    5. 错误对话框:QMessageBox.critical

  * QColorDialog:颜色对话框

    * color =  QColorDialog.getColor()

    * ```python
      p = QPalette()
      # 1,设置文字颜色
      p.setColor(QPalette.WindowText, color)
      # 设置调色板颜色
      self.colorLabel.setPalette(p)
      # 2,设置背景色
      p.setColor(QPalette.Window, color)
      self.colorLabel.setAutoFillBackground(True)
      self.colorLabel.setPalette(p)
      ```

  * QFileDialog:文件对话框

    * 打开图像文件:fname, _ = QFileDialog.getOpenFileName(self, 对话框title, 默认路径, 过滤文件~~格式:图像文件 (*.jpg *.png)~~)

      * self.imageLabel.setPixmap(QPixmap(fname))  在Label上添加图片

    * 打开文本:

      * ```python
        # 槽函数内定义
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFileter(QDir.Files)
        # 尝试打开对话框
        dialog.exec()
        # 可以打开多个
        dialog.selectedFiles()
        with open(filenames[0], encoding="utf-8, mode="r") as f:
        	data = f.read()
        	self.contents.setText(data)
        ```

  * QFontDialog:字体对话框

    * font, ok = QFonfDialog.getFont()

  * QInputDialog:输入对话框

    1. QInputDialog.getItem()传入一个列表或元组生成一个QComboBox下拉列表
       * item, ok = QInputDialog.getItem(self, 对话框title, 对话框内容, 下拉列表选项)
    2. QInputDialog.getText()普通文本
       * text, ok = QInputDialog.getText(self, 对话框title, 对话框内容)
    3. QInputDialog.getInt()
       * num, ok = QInputDialog.getInt(self, 对话框title, 对话框内容)

```python
if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = DemoClass()
	main.show()
	exit(app.exec_())
```



