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
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setFixedSize(300, 300)
        MainWindow.setIconSize(QSize(24, 24))
        self.OpenFile_action = QAction(MainWindow)
        self.OpenFile_action.setObjectName(u"OpenFile_action")
        self.SaveFile_action = QAction(MainWindow)
        self.SaveFile_action.setObjectName(u"SaveFile_action")
        self.ROI_action = QAction(MainWindow)
        self.ROI_action.setObjectName(u"ROI_action")
        self.Show_histogram_action = QAction(MainWindow)
        self.Show_histogram_action.setObjectName(u"Show_histogram_action")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.Show_change_colorspace_action = QAction(MainWindow)
        self.Show_change_colorspace_action.setObjectName(u"Show_change_colorspace_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Img_Lable = QLabel(self.centralwidget)
        self.Img_Lable.setObjectName(u"Img_Lable")
        self.Img_Lable.setEnabled(True)
        self.Img_Lable.setMinimumSize(QSize(0, 0))
        self.Img_Lable.setMouseTracking(False)
        self.Img_Lable.setTabletTracking(False)
        self.Img_Lable.setScaledContents(False)
        self.Img_Lable.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Img_Lable, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        MainWindow.setCentralWidget(self.centralwidget)
        self.Top_menubar = QMenuBar(MainWindow)
        self.Top_menubar.setObjectName(u"Top_menubar")
        self.Top_menubar.setGeometry(QRect(0, 0, 600, 25))
        self.File_menu = QMenu(self.Top_menubar)
        self.File_menu.setObjectName(u"File_menu")
        self.Setting_menu = QMenu(self.Top_menubar)
        self.Setting_menu.setObjectName(u"Setting_menu")
        self.menuImage_Processing = QMenu(self.Top_menubar)
        self.menuImage_Processing.setObjectName(u"menuImage_Processing")
        MainWindow.setMenuBar(self.Top_menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Top_menubar.addAction(self.File_menu.menuAction())
        self.Top_menubar.addAction(self.Setting_menu.menuAction())
        self.Top_menubar.addAction(self.menuImage_Processing.menuAction())
        self.File_menu.addAction(self.OpenFile_action)
        self.File_menu.addSeparator()
        self.File_menu.addAction(self.SaveFile_action)
        self.Setting_menu.addAction(self.ROI_action)
        self.Setting_menu.addSeparator()
        self.Setting_menu.addAction(self.Show_histogram_action)
        self.Setting_menu.addSeparator()
        self.Setting_menu.addAction(self.Show_change_colorspace_action)
        self.menuImage_Processing.addAction(self.action)
        self.menuImage_Processing.addSeparator()
        self.menuImage_Processing.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"4A8G0039", None))
        self.OpenFile_action.setText(QCoreApplication.translate("MainWindow", u"OpenFile", None))
#if QT_CONFIG(shortcut)
        self.OpenFile_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.ROI_action.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u5b9aROI", None))
        self.Show_histogram_action.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u5f71\u50cf\u76f4\u65b9\u5716", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5f71\u50cf\u4e8c\u503c\u5316", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u65b9\u5716\u7b49\u5316", None))
        self.Show_change_colorspace_action.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u6216\u6539\u8b8a\u8272\u5f69\u7a7a\u9593", None))
        self.SaveFile_action.setText(QCoreApplication.translate("MainWindow", u"SaveFile", None))
#if QT_CONFIG(shortcut)
        self.SaveFile_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Img_Lable.setText("")
        self.File_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.Setting_menu.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuImage_Processing.setTitle(QCoreApplication.translate("MainWindow", u"Image Processing", None))
    # retranslateUi

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_MainWindow()
#     window.show()
    
 
#     sys.exit(app.exec_())