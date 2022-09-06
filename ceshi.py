# for i in range(10):
#     m = i + 1
#     print(m)
from PySide6.QtWidgets import QMessageBox
msgBox = QMessageBox()
msgBox.setText("The document has been modified.")
msgBox.setInformativeText("Do you want to save your changes?")
msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
msgBox.setDefaultButton(QMessageBox.Save)
msgBox.show()
ret = msgBox.exec()