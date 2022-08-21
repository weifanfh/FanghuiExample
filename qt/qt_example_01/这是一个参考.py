#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 14:52
# @Author  : @linlianqin
# @Site    :
# @File    : QTextEdit_learn.py
# @Software: PyCharm
# @description:

from PySide6.QtWidgets import *


class qtexteditlearn(QWidget):
    def __init__(self):
        super(qtexteditlearn, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("qtexteditlearn")

        self.textedit = QTextEdit()
        self.button1 = QPushButton("显示文本")
        self.button2 = QPushButton("显示HTML")
        self.button3 = QPushButton("获取文本")
        self.button4 = QPushButton("获取HTML")

        self.resize(300, 280)

        layout = QVBoxLayout()
        layout.addWidget(self.textedit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.button1.clicked.connect(self.showText)
        self.button2.clicked.connect(self.showHTML)
        self.button3.clicked.connect(self.getText)
        self.button4.clicked.connect(self.getHTML)

        self.setLayout(layout)

    # 获取文本
    def getText(self):
        print(self.textedit.toPlainText())

    # 获取HTML
    def getHTML(self):
        print(self.textedit.toHtml())

    # 显示文本
    def showText(self):
        self.textedit.setPlainText("hello world")

    # 显示HTML
    def showHTML(self):
        self.textedit.setHtml('<font color="blue" size="5">Hello World</font>')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWin = qtexteditlearn()

    mainWin.show()
    sys.exit(app.exec_())