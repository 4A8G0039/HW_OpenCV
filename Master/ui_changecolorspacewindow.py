import sys
import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_ChangecolorspaceWindow(QWidget):
    def __init__(self):
        super(Ui_ChangecolorspaceWindow, self).__init__()
        self.setWindowTitle("Change_colorspace")
        self.setFixedSize(700, 300)
        self.qlayout = QGridLayout()
        
        self.qslider1 = QSlider(Qt.Horizontal)
        self.qslider1.setMinimum(0)  # 設定最小值
        self.qslider1.setMaximum(255)  # 設定最大值
        self.qslider1.setSingleStep(1)  # 步長
        self.qslider1.setTickPosition(QSlider.NoTicks)
        self.qlable1 = QLabel()
        self.qlable1.setText('0')
        self.qlayout.addWidget(self.qslider1, 0, 0)
        self.qlayout.addWidget(self.qlable1, 0, 1)

        self.qslider2 = QSlider(Qt.Horizontal)
        self.qslider2.setMinimum(0)  # 設定最小值
        self.qslider2.setMaximum(255)  # 設定最大值
        self.qslider2.setSingleStep(1)  # 步長
        self.qslider2.setTickPosition(QSlider.NoTicks)
        self.qlable2 = QLabel()
        self.qlable2.setText('0')
        self.qlayout.addWidget(self.qslider2, 1, 0)
        self.qlayout.addWidget(self.qlable2, 1, 1)

        self.qslider3 = QSlider(Qt.Horizontal)
        self.qslider3.setMinimum(0)  # 設定最小值
        self.qslider3.setMaximum(255)  # 設定最大值
        self.qslider3.setSingleStep(1)  # 步長
        self.qslider3.setTickPosition(QSlider.NoTicks)
        self.qlable3 = QLabel()
        self.qlable3.setText('0')
        self.qlayout.addWidget(self.qslider3, 2, 0)
        self.qlayout.addWidget(self.qlable3, 2, 1)

        self.qslider4 =  QSlider(Qt.Horizontal)
        self.qslider4.setMinimum(0)  # 設定最小值
        self.qslider4.setMaximum(255)  # 設定最大值
        self.qslider4.setSingleStep(1)  # 步長
        self.qslider4.setTickPosition(QSlider.NoTicks)
        self.qlable4 = QLabel()
        self.qlable4.setText('0')
        self.qlayout.addWidget(self.qslider4, 3, 0)
        self.qlayout.addWidget(self.qlable4, 3, 1)

        self.qslider5 = QSlider(Qt.Horizontal)
        self.qslider5.setMinimum(0)  # 設定最小值
        self.qslider5.setMaximum(255)  # 設定最大值
        self.qslider5.setSingleStep(1)  # 步長
        self.qslider5.setTickPosition(QSlider.NoTicks)
        self.qlable5 = QLabel()
        self.qlable5.setText('0')
        self.qlayout.addWidget(self.qslider5, 4, 0)
        self.qlayout.addWidget(self.qlable5, 4, 1)

        self.qslider6 = QSlider(Qt.Horizontal)
        self.qslider6.setMinimum(0)  # 設定最小值
        self.qslider6.setMaximum(255)  # 設定最大值
        self.qslider6.setSingleStep(1)  # 步長
        self.qslider6.setTickPosition(QSlider.NoTicks)
        self.qlable6 = QLabel()
        self.qlable6.setText('0')
        self.qlayout.addWidget(self.qslider6, 5, 0)
        self.qlayout.addWidget(self.qlable6, 5, 1)

        self.setLayout(self.qlayout)

        self.qslider6.valueChanged.connect(self.change)

    def change(self):
        print(self.qslider6.value())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_ChangecolorspaceWindow()
    window.show()
    sys.exit(app.exec_())