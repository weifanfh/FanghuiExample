# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    #显示双击列表中的项目名称
    def listwidgetitem_info(self,item):
        print(item.text())
    #显示按钮的名称
    def pushbutton_info(self):
        print(self.pushButton.text())

    # 显示按钮的名称
    def pushbutton_info2(self):
        print(self.pushButton2.text())

    def setupUi(self, Widget):
        def aaa(self,item):
            print(item.text())

        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.listWidget = QListWidget(Widget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 20, 256, 192))
        # self.pushButton = QPushButton(Widget)
        # self.pushButton.setObjectName(u"pushButton")
        # self.pushButton.setGeometry(QRect(80, 280, 80, 18))

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 280, 80, 18))
        self.pushButton2 = QPushButton(Widget)
        self.pushButton2.setObjectName(u"pushButton")
        self.pushButton2.setGeometry(QRect(80, 330, 80, 18))

        #self.pushButton.clicked.connect(lambda:self.ppp("dfmd"))
        #self.listWidget.itemDoubleClicked.connect(lambda:self.aaa(self.listWidget))
        self.listWidget.itemDoubleClicked.connect(self.listwidgetitem_info)
        self.pushButton.clicked.connect(self.pushbutton_info)
        self.pushButton2.clicked.connect(self.pushbutton_info2)
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"这是一个Qt窗口", None))

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
        #设置按钮的名称
        self.pushButton.setText(QCoreApplication.translate("Widget", u"第一个按钮", None))
        self.pushButton2.setText(QCoreApplication.translate("Widget", u"第二个按钮", None))

    # retranslateUi

