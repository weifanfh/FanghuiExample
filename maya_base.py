#coding=utf-8

def get_sg_many_uv_map_file(sg_node_name = ''):
    """
    获取sg节点的用于匹配多象限贴图的路径字符串和匹配得到的贴图，并且作为一个字典返回
    其中，字典的键：match_path对应匹配用的路径字符串；map_paths对应贴图列表
    """
    if not sg_node_name:
        raise LookupError(u'请传入需要获取贴图的sg节点名称字符串...')
        
    from maya.app.general.fileTexturePathResolver import findAllFilesForPattern
    import pymel.core as pm
    sg_node = pm.PyNode(sg_node_name)
    match_path = sg_node.fileTextureName.get().replace("\\", "/")
    map_paths = findAllFilesForPattern(sg_node.computedFileTextureNamePattern.get(), 1)
    return {'match_path': match_path, 'map_paths' : map_paths}

