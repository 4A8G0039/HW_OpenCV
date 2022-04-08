#pyside2-uic mainwindow.ui > ui_mainwindow.py
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    # def __init__(self):
    #     super(Ui_MainWindow, self).__init__()
    #     self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(300, 300) #設定視窗大小
        MainWindow.setWindowTitle("4A8G0039") #設定視窗標題
        self.centralwidget = QWidget(MainWindow) #設定視窗centralwidget為QWidget
        self.verticalLayout = QVBoxLayout(self.centralwidget) #設定視窗centralwidget為垂直Layout
        self.verticalLayout.setContentsMargins(0, 0, 0, 0) #設定Layout的邊距

        self.Img_Lable = QLabel(self.centralwidget) #
        self.Img_Lable.setEnabled(True)
        self.Img_Lable.setMinimumSize(QSize(0, 0))
        self.Img_Lable.setAlignment(Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.Img_Lable, 0, Qt.AlignHCenter|Qt.AlignVCenter)



        self.Top_menubar = QMenuBar(MainWindow)
        self.Top_menubar.setGeometry(QRect(0, 0, 600, 25))

        self.File_menu = QMenu(self.Top_menubar)
        self.File_menu.setTitle("File")
        self.Top_menubar.addAction(self.File_menu.menuAction())
        self.OpenFile_action = QAction(MainWindow)
        self.OpenFile_action.setText("OpenFile")
        self.OpenFile_action.setShortcut("Ctrl+O")
        self.File_menu.addAction(self.OpenFile_action)
        self.File_menu.addSeparator()
        self.SaveFile_action = QAction(MainWindow)
        self.SaveFile_action.setText("SaveFile")
        self.SaveFile_action.setShortcut("Ctrl+S")
        self.File_menu.addAction(self.SaveFile_action)

        self.Setting_menu = QMenu(self.Top_menubar)
        self.Setting_menu.setTitle("Setting")
        self.Top_menubar.addAction(self.Setting_menu.menuAction())
        self.ROI_action = QAction(MainWindow)
        self.ROI_action.setText("ROI")
        self.Setting_menu.addAction(self.ROI_action)
        self.Setting_menu.addSeparator()


        self.Image_information = QMenu(self.Setting_menu)
        self.Image_information.setTitle("Image_information")

        self.Show_histogram_action = QAction(MainWindow)
        self.Show_histogram_action.setText("Show histogram")
        self.Image_information.addAction(self.Show_histogram_action)
        self.Show_imgsize_action = QAction(MainWindow)
        self.Show_imgsize_action.setText("Show_imgsize_action")
        self.Image_information.addAction(self.Show_imgsize_action)

        self.Setting_menu.addAction(self.Image_information.menuAction())


        self.Setting_menu.addSeparator()
        self.Change_HSV_action = QAction(MainWindow)
        self.Change_HSV_action.setText("Change HSV")
        self.Setting_menu.addAction(self.Change_HSV_action)
        self.Setting_menu.addSeparator()
        self.Change_RAY_action = QAction(MainWindow)
        self.Change_RAY_action.setText("Change RAY")
        self.Setting_menu.addAction(self.Change_RAY_action)

        self.Image_Processing_menu = QMenu(self.Top_menubar)
        self.Image_Processing_menu.setTitle("Image Processing")
        self.Top_menubar.addAction(self.Image_Processing_menu.menuAction())


        self.action = QAction(MainWindow)
        self.Image_Processing_menu.addAction(self.action)
        self.Image_Processing_menu.addSeparator()
        self.action_3 = QAction(MainWindow)
        self.Image_Processing_menu.addAction(self.action_3)

        MainWindow.setMenuBar(self.Top_menubar)

        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        