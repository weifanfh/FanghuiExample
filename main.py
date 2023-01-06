#coding=utf-8
import os
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

ui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui_file').replace('\\', '/')


class Dialog_Window(QDialog):
    """
    继承于QDialog的窗口类
    """
    def __init__(self, parent = None):
        super(Dialog_Window, self).__init__(parent)
        self.ui = load_ui_file_as_ui(ui_file = os.path.join(ui_dir, 'window_ui.ui'), parent = self)
        set_window(self)

def set_window(window = None):
    """
    :param window: 需要被设置参数的主控件
    :return: 不返回值
    """
    if window:
        window_size = {'width': 300,
                       'height': 400}
        window_name = '窗口'

        window.resize(window_size['width'], window_size['height'])
        window.setWindowTitle(window_name)

def load_ui_file_as_ui(ui_file = None, parent = None):
    """
    :param ui_file:需要加载的ui文件,如："D:/Source/Qt/ui_test/test_fin/form.ui"
    :param parent:加载的ui的父控件，一般为：QMainWindow、QDialog
    :return:返回ui控件对象
    """
    from PySide6.QtUiTools import QUiLoader
    loader = QUiLoader()
    if ui_file:
        return loader.load(ui_file, parentWidget=parent)
    else:
        raise LookupError("请传入ui文件")

class MainWindow_Window(QMainWindow):
    """
    继承于QMainWindow的窗口类
    """
    def __init__(self, parent = None):
        super(MainWindow_Window, self).__init__(parent)
        self.ui = load_ui_file_as_ui(ui_file = os.path.join(ui_dir, 'window_ui.ui'), parent = self)
        set_window(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget_window = MainWindow_Window()
    widget_window.show()
    sys.exit(app.exec())

