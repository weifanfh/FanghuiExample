# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.q=0

    def load_ui(self):
        ui_file = QFile(r"D:\Files\FangHuiExampleSource\load2\form.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file, parentWidget=self)
        self.window.pushButton.clicked.connect(self.AA)  # 调用UI文件中的控件
        ui_file.close()

    def AA(self):
        print("测试")
        import widget2
        #from QtloadUI.dialog import Dialog
        widget = widget2.Widget()
        widget.setParent(self.window)
        widget.move(0,30)
        widget.show()
        self.q=self.q+1
        print(self.q)
        #widget.
        #widget.exec_()


        #
        # loader = QUiLoader()
        # path = Path(__file__).resolve().parent / "form.ui"
        # ui_file = QFile(path)
        # ui_file.open(QFile.ReadOnly)
        # loader.load(ui_file, self)
        # ui_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
