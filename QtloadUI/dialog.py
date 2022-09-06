# This Python file uses the following encoding: utf-8
import os
# from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile
# from PySide2.QtUiTools import QUiLoader
from PySide2.QtUiTools import QUiLoader


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.load_ui()

    def load_ui(self):
        ui_file = QFile(r"D:\Files\FangHuiExampleSource\QtloadUI\form_test.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        window = loader.load(ui_file, parentWidget=self)
        ui_file.close()
        print(Dialog)
        print("测试")
        #ui_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    #widget.exec_()
    sys.exit(app.exec_())
