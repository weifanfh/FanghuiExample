#coding=utf-8
import os
import sys
import csv

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

ui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui_file').replace('\\', '/')
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'source_file').replace('\\', '/')

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
        self.add_comboBox_items()
        self.add_signal()

    def add_comboBox_items(self):
        csv_file_name = os.path.join(source_dir, 'combobox_items.csv')
        with open(csv_file_name, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.ui.combobox.addItem(row['任务名'])

    def add_signal(self):

        def add_combobox_change_item_signal():
            """
            为名为：combobox下拉框添加切换选项时的信号，输出文本内容和id
            """
            def print_combobox_item_info():
                print("下拉选项文本内容：{}".format(self.ui.combobox.currentText()))
                print("下拉选项序号id：{}".format(self.ui.combobox.currentIndex()))
            self.ui.combobox.currentIndexChanged.connect(print_combobox_item_info)

        def add_text_finish_change_combobox_item_signal():
            """
            为名为text_line_1的文本框添加输入完文本后设置名为combobox的下拉框的选项（结合csv文件设置）
            """
            def text_finish_change_item():
                csv_file_name = os.path.join(source_dir, 'combobox_items.csv')
                with open(csv_file_name, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if self.ui.text_line_1.text() == row['任务名']:
                            for i in range(self.ui.combobox.count()):
                                if self.ui.combobox.itemText(i) == row['任务名']:
                                    print("设置：{}".format(self.ui.combobox.itemText(i)))
                                    self.ui.combobox.setCurrentText(row['任务名'])
            self.ui.text_line_1.editingFinished.connect(text_finish_change_item)
        def add_button_click_signal():
            """
            为名为：button 的按钮添加点击时打印信息的信号
            """
            def print_click_info():
                print("点击按钮")
            self.ui.button.clicked.connect(print_click_info)

        add_combobox_change_item_signal()
        add_text_finish_change_combobox_item_signal()
        add_button_click_signal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget_window = MainWindow_Window()
    widget_window.show()
    sys.exit(app.exec())

