# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QPushButton, QCheckBox,
    QSizePolicy, QWidget, QDialog)

from dialog_ui_form import Ui_Dialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class Ui_Widget(object):





    def printinfo(self, Item):
        print(Item.text())

    def additem(self):
        self.listWidget.addItem("按钮")

    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)

        def showwindows():
            Widget.close()
            widget = Dialog()
            widget.show()
            widget.exec_()

        def addcheck():
            self.checkBox = QCheckBox("这是一个复选框", Widget)
            self.checkBox.setObjectName("复选框")
            self.checkBox.setGeometry(QRect(400, 410, 200, 18))
            self.checkBox.show()
            self.checkBox.setText(QCoreApplication.translate("Widget", "按钮按钮", None))



        # def ppp():
        #     Widget.close()
        self.listWidget = QListWidget(Widget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 20, 531, 221))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 280, 491, 41))

        self.pushButton2 = QPushButton(Widget)
        self.pushButton2.setObjectName(u"pushButton")
        self.pushButton2.setGeometry(QRect(80, 350, 491, 41))

        self.retranslateUi(Widget)
        self.pushButton.clicked.connect(self.additem)
        self.listWidget.itemDoubleClicked.connect(self.printinfo)
        self.pushButton.clicked.connect(showwindows)
        self.pushButton2.clicked.connect(addcheck)
        # self.pushButton.clicked.connect(ppp)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Widget", u"\u65b0\u5efa\u9879\u76ee1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Widget", u"\u65b0\u5efa\u9879\u76ee2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Widget", u"\u65b0\u5efa\u9879\u76ee3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Widget", u"\u65b0\u5efa\u9879\u76ee4", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Widget", u"\u65b0\u5efa\u9879\u76ee5", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Widget", "按钮1", None))
        self.pushButton2.setText(QCoreApplication.translate("Widget", "按钮2", None))

    # retranslateUi

