#coding=utf-8
"""
Export Settings Example

This example shows how to change an exporter settings.
This works also for importers/scene loaders.
"""

import c4d
from c4d import documents, plugins, storage
def Get_Child(obj):
    """
    传入一个对象，或者对象的所有对象

    Parameters/参数
    ----------
    obj : c4d.BaseObject
        传入的一个对象

    return/返回值
    ----------
    list 传入对象的子级（不包括对象本身）
    """
    # 创建一个列表
    obj_list = []
    # 获取传入的对象的所有子集(仅仅是子集,不是子集的子集)列表
    new_obj_list = obj.GetChildren()
    # 如果列表不为空,说明有子集,因此需要继续判断子集是否还有子集
    # 如果列表为空,说明对象没有子集,因此直接返回
    if new_obj_list:
        # 如果new_obj_list不为空,就将子集添加到返回的列表中,在没有孙子集情况下已经获取了所有子集
        obj_list = obj_list + new_obj_list
        for obj_i in new_obj_list:
            # 遍历所有子集,检查其是否有子集
            if obj_i.GetChildren():
                # 判断是否有子集,如果有子集就调用自己,检查是否还有子集
                obj_list = obj_list + Get_Child(obj_i)
    return obj_list

def get_file_mesh(doc):
    """
    获取传入文件中的所有mesh对象，返回为列表
    """
    def get_child(obj = None, type_id = None):
        """
        传入一个对象，或者对象的所有对象

        Parameters/参数
        ----------
        obj : c4d.BaseObject
            传入的一个对象

        return/返回值
        ----------
        list 传入对象的子级（不包括对象本身）
        """
        if obj:
            if type_id:
                # 创建一个列表
                obj_list = []
                # 获取传入的对象的所有子集(仅仅是子集,不是子集的子集)列表
                new_obj_list = obj.GetChildren()
                # 如果列表不为空,说明有子集,因此需要继续判断子集是否还有子集
                # 如果列表为空,说明对象没有子集,因此直接返回
                if new_obj_list:
                    # 如果new_obj_list不为空,就将子集添加到返回的列表中,在没有孙子集情况下已经获取了所有子集
                    for obj_i in new_obj_list:
                        if obj_i.GetRealType() == type_id:
                            obj_list.append(obj_i)
                        # 遍历所有子集,检查其是否有子集
                        if obj_i.GetChildren():
                            # 判断是否有子集,如果有子集就调用自己,检查是否还有子集
                            obj_list = obj_list + get_child(obj_i, type_id = type_id)
                return obj_list
            else:
                # 创建一个列表
                obj_list = []
                # 获取传入的对象的所有子集(仅仅是子集,不是子集的子集)列表
                new_obj_list = obj.GetChildren()
                # 如果列表不为空,说明有子集,因此需要继续判断子集是否还有子集
                # 如果列表为空,说明对象没有子集,因此直接返回
                if new_obj_list:
                    # 如果new_obj_list不为空,就将子集添加到返回的列表中,在没有孙子集情况下已经获取了所有子集
                    obj_list = obj_list + new_obj_list
                    for obj_i in new_obj_list:
                        # 遍历所有子集,检查其是否有子集
                        if obj_i.GetChildren():
                            # 判断是否有子集,如果有子集就调用自己,检查是否还有子集
                            obj_list = obj_list + get_child(obj_i, type_id = type_id)
        else:
            pass
    high_objs = doc.GetObjects()
    for high_obj in high_objs:
        if high_obj.GetRealType() != 5100:
            high_objs.remove(mesh)

    mesh_list = high_objs
    for mesh in high_objs:
        mesh_list = mesh_list + get_child(mesh, 5100)
    return mesh_list


def set_gltf_plugin_settings():
    """
    设置导出gltf插件的设置参数，可用于c4dpy.exe执行任务;亦可用于c4d的ui界面中执行
    """
    pluginList = c4d.plugins.FilterPluginList(c4d.PLUGINTYPE_SCENESAVER, True)
    for plugin in pluginList:
        plugin_id = plugin.GetID()
        if plugin_id == 1041129:
            imexporter_obj = {}
            plugin.Message(c4d.MSG_RETRIEVEPRIVATEDATA, imexporter_obj)
            gltf_export_settings = imexporter_obj['imexporter']
            gltf_export_settings[c4d.GLTFEXPORTER_TEXTURES] = True

def load_fbx__export_gltf(import_fbx_path = None, export_gltf_path = None):
    """
    加载一个fbx文件，并且将其导出为gltf文件
    """
    if not import_fbx_path or not export_gltf_path:
        return
    plugin_id = 1041129

    new_doc = c4d.documents.LoadDocument(import_fbx_path, c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS)

    c4d.documents.InsertBaseDocument(new_doc)
    c4d.documents.SetActiveDocument(new_doc)

    doc = c4d.documents.GetActiveDocument()
    # 使用ui对话框指定保存路径（仅可用于打开c4d时，不可用于c4dpy.exe中）
    # filePath = storage.LoadDialog(title="Save File for Alembic Export", flags=c4d.FILESELECT_SAVE, force_suffix="abc")

    # 打印输出一下加载文档中的mesh,以判断是否成功加载文件
    mesh_list = get_file_mesh(doc)
    for mesh in mesh_list:
        print(mesh)

    set_gltf_plugin_settings()
    if documents.SaveDocument(doc, export_gltf_path, c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST, plugin_id):
        print("Document successfully exported to:{}".format(export_gltf_path))
    else:
        print("Export failed!")

def main():
    load_fbx__export_gltf(
                    import_fbx_path = r"D:\tmp\c4d\test_gltf_export\source_fbx\gltf_export_test.fbx".replace("\\", "/"),
                    export_gltf_path = r"D:\tmp\c4d\test_gltf_export\export_gltf\06.gltf".replace("\\", "/")
                            )
if __name__=='__main__':
    main()