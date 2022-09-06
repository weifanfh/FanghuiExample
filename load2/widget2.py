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

    def load_ui(self):
        ui_file = QFile(r"D:\Files\FangHuiExampleSource\load2\form2.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file, parentWidget=self)
        self.window.pushButton.clicked.connect(self.AA)  # 调用UI文件中的控件
        ui_file.close()

    def AA(self):
        print("测试")
        from QtloadUI.dialog import Dialog
        widget = Dialog()
        widget.setParent(self.window)
        widget.show()
        widget.exec_()


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
