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

```python
if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = DemoClass()
	main.show()
	exit(app.exec_())
```

