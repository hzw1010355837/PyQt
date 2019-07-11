```python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
```

* 让控件支持拖拽动作
  * A.setAcceptDrops(True) :A控件支持接受其他控件拖入, B.setDragEnabled(True)
    * B进入触发事件:dragEnterEvent(event)
      * B为主窗口类,A为下拉框控件类
    * 在A区域放下A触发:dropEvent(event)
      * [代码参考链接](<https://github.com/hzw1010355837/PyQt/blob/master/DemoDragEvent.py>)
      * 注意点:获取下拉框拖拽事件数据时用:`event.mimeData().text()`可用`event.mimeData().hasText()`先判断

* 剪贴板

  * clipboard = QApplication.clipboard() **通过此对象Copy&Paste剪贴板内容**

  * ```python
    clipboard.setText(剪贴板文字)
    # Copy&Paste图像
    clipboard.setPixmap(QPixmap("./images/book.png"))
    # HTML剪贴板复制**Copy**
    mimeData = QMimeData()
    mimeData.setHtml(html字符串)
    clipboard.setMimeData(mimeData)
    # 设置HTML粘贴格式**Paste**
    mimeData = clipboard.mimeData()
    if mimeData.hasHtml():
    	self.textLabel.setText(mimeData.html())
    ```

* 日历控件:

  * QCalendarWidget() :表格控件形式

  * ```python
    cw = QCalendarWidget(self)
    cw.setMinimumDate(QDate(1995,6,20)) # QDate(1995,6,20).addDays(365)
    cw.setMaximumDate(QDate(2995,6,20))
    # 设置以网格显示
    cw.setGridVisible(True)
    ```

     * date = sw.selectedDate() **获取当前选择日期**
     * date.toString("yyyy-MM-dd dddd") **格式化日期**

   * 设置各种风格日期和时间:QDataTimeEdit() :输入框形式

      * ```
        te = QDateTimeEdit() # 1
        te = QDateTimeEdit(QDateTime.currentDateTime()) # 2设置显示为当前日期时间
        te = QDateTimeEdit(QDateTime.currentDate()) # 3设置显示为当前日期
        te = QDateTimeEdit(QDateTime.currentTime()) # 4设置显示为当前时间
        te.setDisplayFormat("yyyy-MM-dd HH:mm:ss") # 设置显示格式:"yyyy.MM.dd" "HH:mm:ss"
        ```

     * te.setCalendarPopup(True) **可以通过下拉箭头将输入框设置成表格控件形式的日历**

     * 事件触发:te.dateChanged.connect...;te.timeChanged...;te.dateTimeChanged...

```python
if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = DemoClass()
	main.show()
	exit(app.exec_())
```

