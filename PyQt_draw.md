```python
from PyQt5.QtCore import *
# form PyQt.QtCore import Qt
from PyQt5.QtGui import *
# from PyQt.QtGui import QColor,Qfont,QPainter
form PyQt5.QtWidgets import *
# from PyQt.QtWidgets import QApplication,QWidget
import sys
```

* 绘图API:绘制文本QPainter **必须在painterEvent事件方法中回值各种元素** painterEvent会在*创建窗口*&*变化窗口尺寸*时自动调用

  * ```python
    def paintEvent(self, event)
    	# 基本格式
        painter = QPainter()
        painter.begin()
        # TODO 对应相应的API实现
        painter.drawText(...)
        painter.end()
    ```

  1. 文本
     * painter.setPen(QColor(150, 43, 5))
     * painter.setFont(QFont("SimSun", 25))
     * painter.drawText(event.rect(), Qt.alignCenter, self.text) 
       * event.rect()代表绘制区域及尺寸;Qt.alignCenter居中对齐; self.text绘制文本
  2. 各种图形(直线, 点, 椭圆, 弧, 扇形, 多边形等) 像素点(-2PI, 2PI)
     * drawPoint(x, y)
  3. 图像

```python
if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = DemoClass()
	main.show()
	exit(app.exec_())
```
