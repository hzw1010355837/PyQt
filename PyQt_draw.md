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
        painter = QPainter(self)
        painter.begin(self)
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

     * 通过像素点绘制直线:drawPoint(x, y)可以绘制一个像素点,使用for循环设置绘制点数

     * 绘制不同类型线(设置pen):pen=QPen(Qt.red,3~~粗细~~,Qt.SolidLine~~直线~~);painter.setPen(pen);painter.drawLine(x,y,a,b~~两点坐标~~)

     * 绘制图形

       * 弧度:painter.drawArc(QRectF(x,y,w,h)~~绘制区域~~, 起始角度, 结束角度)

       * 圆:painter.drawArc(x,y,w,h,0,360*16)

       * 带弦:painter.drawChord(...)

       * 扇形:painter.drawPie(...)

       * 椭圆:painter.drawEllipse(x,y,w,h) *当宽高一致时,绘制圆*

       * 多边形:painter.drawPolygon(polygon~~对象~~) 由多个点组成

         * ```python
           point1 = QPoint(x,y)
           point2 = QPoint(x,y)
           point3 = QPoint(x,y)
           point4 = QPoint(x,y)
           point5 = QPoint(x,y)
           # 创建多边形对象
           polygon = QPolygon([point1,point2,point3,point4,point5])
           painter.drawPolygon(polygon)
           painter.draw
           ```

  3. 图像

     * 绘制图像:painter.drawImage(rect~~区域~~, image)

     * ```python
       # 装载图像
       image = QImage("./images/book.png")
       # 绘制区域(缩小放大图像)
       rect = QRect(x.y, image.width()/3, image.height()/3) # 缩小三倍
       painter.drawImage(rect, image)
       ```

       * 加载图片时会有警告出现:格式不兼容.**处理:**`image.save("./images/book1.png")`之后再跑用image1就不会出现

* 使用画刷填充图形区域

  * 设置画刷:brush = 	QBrush(Qt.SolidPattern~~实心画刷~~)
  * painter.setBrush(brush);painter.drawRect(x,y,w,h)

```python

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = DemoClass()
	main.show()
	exit(app.exec_())
```
