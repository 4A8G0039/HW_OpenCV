#pyside2-uic mainwindow.ui > ui_mainwindow.py
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main_Window(QMainWindow):
    # def __init__(self):
    #     super(Ui_MainWindow, self).__init__()
    #     self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(300, 300) #設定視窗大小
        MainWindow.setWindowTitle("4A8G0039") #設定視窗標題
    #CentralWidget#
        self.centralwidget = QWidget(MainWindow) #新增一個QWidget命名為centralwidget
        self.verticalLayout = QHBoxLayout(self.centralwidget) #設定centralwidget為水平Layout並命名為verticalLayout
        self.verticalLayout.setContentsMargins(0, 0, 0, 0) #設定verticalLayout的邊距
        self.Img_Lable = QLabel(self.centralwidget) #新增一個QLabel命名為Img_Lable
        self.Img_Lable.setMinimumSize(QSize(0, 0)) #設定QLabel的最小尺寸
        self.Img_Lable.setAlignment(Qt.AlignCenter) #設定QLabel裡的物件置中
        self.verticalLayout.addWidget(self.Img_Lable, 0, Qt.AlignHCenter|Qt.AlignVCenter) #把Img_Lable加進verticalLayout並設為水平置中，垂直置中
        MainWindow.setCentralWidget(self.centralwidget) #將主視窗的CentralWidget設為centralwidget
    #CentralWidget#
    #MenuBar#
        self.Top_menubar = QMenuBar(MainWindow) #新增一個QMenuBar命名為Top_menubar
        self.Top_menubar.setGeometry(QRect(0, 0, 600, 25)) #設定Top_menubar的尺寸
    #File_menu
        self.File_menu = QMenu(self.Top_menubar)
        self.File_menu.setTitle("File")
        self.OpenFile_action = QAction(MainWindow)
        self.OpenFile_action.setText("OpenFile")
        self.OpenFile_action.setShortcut("Ctrl+O")
        self.File_menu.addAction(self.OpenFile_action)
        self.SaveFile_action = QAction(MainWindow)
        self.SaveFile_action.setText("SaveFile")
        self.SaveFile_action.setShortcut("Ctrl+S")
        self.File_menu.addAction(self.SaveFile_action)
        self.Top_menubar.addAction(self.File_menu.menuAction())
    #File_menu
    #Setting_menu
        self.Setting_menu = QMenu(self.Top_menubar)
        self.Setting_menu.setTitle("Setting")
        self.ROI_action = QAction(MainWindow)
        self.ROI_action.setText("ROI")
        self.Setting_menu.addAction(self.ROI_action)

        self.Image_Information_menu = QMenu(self.Setting_menu)
        self.Image_Information_menu.setTitle("Image information")
        self.Show_Histogram_action = QAction(MainWindow)
        self.Show_Histogram_action.setText("Histogram")
        self.Image_Information_menu.addAction(self.Show_Histogram_action)
        self.Show_Imgsize_action = QAction(MainWindow)
        self.Show_Imgsize_action.setText("Image Size")
        self.Image_Information_menu.addAction(self.Show_Imgsize_action)
        self.Setting_menu.addAction(self.Image_Information_menu.menuAction())

        self.Change_Colorspace_menu = QMenu(self.Setting_menu)
        self.Change_Colorspace_menu.setTitle("Change Colorspace")
        self.Change_HSV_action = QAction(MainWindow)
        self.Change_HSV_action.setText("HSV")
        self.Change_Colorspace_menu.addAction(self.Change_HSV_action)
        self.Change_GRAY_action = QAction(MainWindow)
        self.Change_GRAY_action.setText("GRAY")
        self.Change_Colorspace_menu.addAction(self.Change_GRAY_action)
        self.Setting_menu.addAction(self.Change_Colorspace_menu.menuAction())

        self.Top_menubar.addAction(self.Setting_menu.menuAction())
    #Setting_menu
    #Image_Processing_menu
        self.Image_Processing_menu = QMenu(self.Top_menubar)
        self.Image_Processing_menu.setTitle("Image Processing")
        self.Image_Thresholding_action = QAction(MainWindow)
        self.Image_Thresholding_action.setText("Image Thresholding (影像二值化)")
        self.Image_Processing_menu.addAction(self.Image_Thresholding_action)
        self.Histogram_Equalization_action = QAction(MainWindow)
        self.Histogram_Equalization_action.setText("Histogram Equalization (直方圖等化)")
        self.Image_Processing_menu.addAction(self.Histogram_Equalization_action)
        self.Perspective_Transform_action = QAction(MainWindow)
        self.Perspective_Transform_action.setText("Perspective Transform (透視投影轉換)")
        self.Image_Processing_menu.addAction(self.Perspective_Transform_action)

        self.Geometric_Transform_menu = QMenu(self.Image_Processing_menu)
        self.Geometric_Transform_menu.setTitle("Geometric Transform (幾何轉換)")
        self.Translate_Rotate_action = QAction(MainWindow)
        self.Translate_Rotate_action.setText("Translate and Rotate (平移/旋轉)")
        self.Geometric_Transform_menu.addAction(self.Translate_Rotate_action)
        self.Affine_Transform_action = QAction(MainWindow)
        self.Affine_Transform_action.setText("Affine Transform (仿射轉換)")
        self.Geometric_Transform_menu.addAction(self.Affine_Transform_action)
        self.Image_Processing_menu.addAction(self.Geometric_Transform_menu.menuAction())

        self.Image_Filtering_action = QAction(self.Image_Processing_menu)
        self.Image_Filtering_action.setText("Image Filtering (影象濾波)")
        self.Image_Processing_menu.addAction(self.Image_Filtering_action)

        self.Top_menubar.addAction(self.Image_Processing_menu.menuAction())
    #Image_Processing_menu

        MainWindow.setMenuBar(self.Top_menubar)
    #MenuBar#
    #StatusBar#
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
    #StatusBar#
        QMetaObject.connectSlotsByName(MainWindow)
        