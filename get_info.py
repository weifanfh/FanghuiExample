#coding=utf-8
import os
import sys

def get_module_path(module):
    """
    传入一个模块，获取模块的路径并且返回对应字符串
    """

    def get_imported_module_info():
        """
        获取已经导入的模块，返回一个字典，字典键为模块名，值为模块
        如：{'sys': <module 'sys' (built-in)>, 'os': <module 'os' from 'D:\\APP\\ProGramApp\\python36\\lib\\os.py'>}
        """
        # set(sys.modules) 获取所有的模块名并且存储为一个无序的集合
        # set(globals()) 获取全局变量，其中导入的模块也在全局变量，将全局变量存储为一个无序的集合
        # set(sys.modules) & set(globals()) 取两个集合的交集，即已经导入的模块的名称集合
        modulenames = set(sys.modules) & set(globals())
        # for循环获取对应名称的模块（已经导入了的）
        imported_module_info = {}
        for module_name in modulenames:
            imported_module_info[module_name] = sys.modules[module_name]
        return imported_module_info
    if 'inspect' not in get_imported_module_info():
        import inspect

    return inspect.getfile(module)


def get_imported_module_info():
    """
    获取已经导入的模块，返回一个字典，字典键为模块名，值为模块
    如：{'sys': <module 'sys' (built-in)>, 'os': <module 'os' from 'D:\\APP\\ProGramApp\\python36\\lib\\os.py'>}
    """
    # set(sys.modules) 获取所有的模块名并且存储为一个无序的集合
    # set(globals()) 获取全局变量，其中导入的模块也在全局变量，将全局变量存储为一个无序的集合
    # set(sys.modules) & set(globals()) 取两个集合的交集，即已经导入的模块的名称集合
    modulenames = set(sys.modules) & set(globals())
    # for循环获取对应名称的模块（已经导入了的）
    imported_module_info = {}
    for module_name in modulenames:
        imported_module_info[module_name] = sys.modules[module_name]
    return imported_module_info



