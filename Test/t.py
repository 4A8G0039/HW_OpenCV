import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChangecolorspaceWindow(QWidget):
    def __init__(self):
        super(Ui_ChangecolorspaceWindow, self).__init__()
        self.setWindowTitle(u"Change_colorspace")
        self.setFixedSize(700, 300)
        self.main_verticalLayout = QVBoxLayout()
        self.u_r_horizontalLayout = QHBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################

        self.Upper_label = QLabel()
        sizePolicy.setHeightForWidth(self.Upper_label.sizePolicy().hasHeightForWidth())
        self.Upper_label.setSizePolicy(sizePolicy)
        self.Upper_label.setMinimumSize(QSize(40, 0))
        self.Upper_label.setText("Upper :")
        self.u_r_horizontalLayout.addWidget(self.Upper_label)

        self.u_r = QLabel()
        self.u_r.setText('R')
        self.u_r_horizontalLayout.addWidget(self.u_r)

        self.u_r_Slider = QSlider()
        self.u_r_Slider.setMaximum(250)
        self.u_r_Slider.setValue(0)
        self.u_r_Slider.setOrientation(Qt.Horizontal)
        self.u_r_horizontalLayout.addWidget(self.u_r_Slider)

        self.u_r_v = QLabel()
        sizePolicy.setHeightForWidth(self.u_r_v.sizePolicy().hasHeightForWidth())
        self.u_r_v.setSizePolicy(sizePolicy)
        self.u_r_v.setMinimumSize(QSize(20, 0))
        self.u_r_v.setText("0")
        self.u_r_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.u_r_horizontalLayout.addWidget(self.u_r_v)


        self.main_verticalLayout.addLayout(self.u_r_horizontalLayout)

#####################################################################################

        self.u_g_horizontalLayout = QHBoxLayout()
        self.u_g_horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.u_g_horizontalLayout.addItem(self.u_g_horizontalSpacer)

        self.u_g = QLabel()
        self.u_g.setText("G")
        self.u_g_horizontalLayout.addWidget(self.u_g)

        self.u_g_Slider = QSlider()
        self.u_g_Slider.setMaximum(250)
        self.u_g_Slider.setValue(0)
        self.u_g_Slider.setOrientation(Qt.Horizontal)
        self.u_g_horizontalLayout.addWidget(self.u_g_Slider)

        self.u_g_v = QLabel()
        sizePolicy.setHeightForWidth(self.u_g_v.sizePolicy().hasHeightForWidth())
        self.u_g_v.setSizePolicy(sizePolicy)
        self.u_g_v.setMinimumSize(QSize(20, 0))
        self.u_g_v.setText("0")
        self.u_g_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.u_g_horizontalLayout.addWidget(self.u_g_v)

        self.main_verticalLayout.addLayout(self.u_g_horizontalLayout)

#####################################################################################

        self.u_b_horizontalLayout = QHBoxLayout()
        self.u_b_horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.u_b_horizontalLayout.addItem(self.u_b_horizontalSpacer)

        self.u_b = QLabel()
        self.u_b.setText("B")
        self.u_b_horizontalLayout.addWidget(self.u_b)

        self.u_b_Slider = QSlider()
        self.u_b_Slider.setMaximum(250)
        self.u_b_Slider.setValue(0)
        self.u_b_Slider.setOrientation(Qt.Horizontal)
        self.u_b_horizontalLayout.addWidget(self.u_b_Slider)

        self.u_b_v = QLabel()
        sizePolicy.setHeightForWidth(self.u_b_v.sizePolicy().hasHeightForWidth())
        self.u_b_v.setSizePolicy(sizePolicy)
        self.u_b_v.setMinimumSize(QSize(20, 0))
        self.u_b_v.setText("0")
        self.u_b_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.u_b_horizontalLayout.addWidget(self.u_b_v)

        self.main_verticalLayout.addLayout(self.u_b_horizontalLayout)

#####################################################################################  LINE


        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.main_verticalLayout.addWidget(self.line)


#####################################################################################  LINE

        self.l_r_horizontalLayout = QHBoxLayout()
        self.Lower_label = QLabel()
        sizePolicy.setHeightForWidth(self.Lower_label.sizePolicy().hasHeightForWidth())
        self.Lower_label.setSizePolicy(sizePolicy)
        self.Lower_label.setMinimumSize(QSize(40, 0))
        self.Lower_label.setText("Lower :")
        self.l_r_horizontalLayout.addWidget(self.Lower_label)

        self.l_r = QLabel()
        self.l_r.setText("R")
        self.l_r_horizontalLayout.addWidget(self.l_r)

        self.l_r_Slider = QSlider()
        self.l_r_Slider.setMaximum(250)
        self.l_r_Slider.setValue(0)
        self.l_r_Slider.setOrientation(Qt.Horizontal)
        self.l_r_horizontalLayout.addWidget(self.l_r_Slider)

        self.l_r_v = QLabel()
        sizePolicy.setHeightForWidth(self.l_r_v.sizePolicy().hasHeightForWidth())
        self.l_r_v.setSizePolicy(sizePolicy)
        self.l_r_v.setMinimumSize(QSize(20, 0))
        self.l_r_v.setText("0")
        self.l_r_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.l_r_horizontalLayout.addWidget(self.l_r_v)

        self.main_verticalLayout.addLayout(self.l_r_horizontalLayout)

#####################################################################################

        self.l_g_horizontalLayout = QHBoxLayout()
        self.l_g_horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.l_g_horizontalLayout.addItem(self.l_g_horizontalSpacer)

        self.l_g = QLabel()
        self.l_g.setText("G")
        self.l_g_horizontalLayout.addWidget(self.l_g)

        self.l_g_Slider = QSlider()
        self.l_g_Slider.setMaximum(250)
        self.l_g_Slider.setValue(0)
        self.l_g_Slider.setOrientation(Qt.Horizontal)
        self.l_g_horizontalLayout.addWidget(self.l_g_Slider)

        self.l_g_v = QLabel()
        sizePolicy.setHeightForWidth(self.l_g_v.sizePolicy().hasHeightForWidth())
        self.l_g_v.setSizePolicy(sizePolicy)
        self.l_g_v.setMinimumSize(QSize(20, 0))
        self.l_g_v.setText("0")
        self.l_g_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.l_g_horizontalLayout.addWidget(self.l_g_v)


        self.main_verticalLayout.addLayout(self.l_g_horizontalLayout)

#####################################################################################

        self.l_b_horizontalLayout = QHBoxLayout()
        self.l_b_horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.l_b_horizontalLayout.addItem(self.l_b_horizontalSpacer)

        self.l_b = QLabel()
        self.l_b.setText("B")
        self.l_b_horizontalLayout.addWidget(self.l_b)

        self.l_b_Slider = QSlider()
        self.l_b_Slider.setMaximum(250)
        self.l_b_Slider.setValue(0)
        self.l_b_Slider.setOrientation(Qt.Horizontal)
        self.l_b_horizontalLayout.addWidget(self.l_b_Slider)

        self.l_b_v = QLabel()
        sizePolicy.setHeightForWidth(self.l_b_v.sizePolicy().hasHeightForWidth())
        self.l_b_v.setSizePolicy(sizePolicy)
        self.l_b_v.setMinimumSize(QSize(20, 0))
        self.l_b_v.setText("0")
        self.l_b_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.l_b_horizontalLayout.addWidget(self.l_b_v)

        self.main_verticalLayout.addLayout(self.l_b_horizontalLayout)

        self.setLayout(self.main_verticalLayout)

#####################################################################################

        self.u_r_Slider.valueChanged.connect(self.u_r_valueChanged)
        self.u_g_Slider.valueChanged.connect(self.u_g_valueChanged)
        self.u_b_Slider.valueChanged.connect(self.u_b_valueChanged)
        self.l_r_Slider.valueChanged.connect(self.l_r_valueChanged)
        self.l_g_Slider.valueChanged.connect(self.l_g_valueChanged)
        self.l_b_Slider.valueChanged.connect(self.l_b_valueChanged)


    def u_r_valueChanged(self):
        self.u_r_v.setText(f"{self.u_r_Slider.value()}")
        print(self.u_r_Slider.value())

    def u_g_valueChanged(self):
        self.u_g_v.setText(f"{self.u_g_Slider.value()}")
        print(self.u_g_Slider.value())

    def u_b_valueChanged(self):
        self.u_b_v.setText(f"{self.u_b_Slider.value()}")
        print(self.u_b_Slider.value())

    def l_r_valueChanged(self):
        self.l_r_v.setText(f"{self.l_r_Slider.value()}")
        print(self.l_r_Slider.value())

    def l_g_valueChanged(self):
        self.l_g_v.setText(f"{self.l_g_Slider.value()}")
        print(self.l_g_Slider.value())

    def l_b_valueChanged(self):
        self.l_b_v.setText(f"{self.l_b_Slider.value()}")
        print(self.l_b_Slider.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_ChangecolorspaceWindow()
    window.show()
    sys.exit(app.exec_())