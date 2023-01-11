#coding=utf-8
import os
import sys

import pymel.core as pm
import maya.cmds as cmds

def get_sg_many_uv_map_file(sg_node_name = ''):
    """
    获取sg节点的用于匹配多象限贴图的路径字符串和匹配得到的贴图，并且作为一个字典返回
    其中，字典的键：match_path对应匹配用的路径字符串；map_paths对应贴图列表
    """
    if not sg_node_name:
        raise LookupError(u'请传入需要获取贴图的sg节点名称字符串...')
        
    from maya.app.general.fileTexturePathResolver import findAllFilesForPattern
    sg_node = pm.PyNode(sg_node_name)
    match_path = sg_node.fileTextureName.get().replace("\\", "/")
    map_paths = findAllFilesForPattern(sg_node.computedFileTextureNamePattern.get(), 1)
    return {'match_path': match_path, 'map_paths' : map_paths}


def unlock_timeline():
    """
    如果sceneConfigurationScriptNode节点被锁定了，会导致无法修改时间线的范围；此方法可以检测时间线是否被锁，如果是则解锁
    """
    is_lock_timeline = []
    for i in cmds.ls('*sceneConfigurationScriptNode*', type='script'):
        if cmds.getAttr('%s.b' % i, l = True):
            is_lock_timeline.append(True)

    if True in is_lock_timeline:
        result = cmds.confirmDialog(title = u"解锁时间线", message = u"检测到时间线被锁定, 是否解锁？", button = [u'是', u'否'], cancelButton = u'否', dismissString = u'否')
        if result == u'是':
            for i in cmds.ls('*sceneConfigurationScriptNode*', type='script'):
                cmds.setAttr('%s.b' % i, e=1, l=0)
            is_lock_timeline = []
            for i in cmds.ls('*sceneConfigurationScriptNode*', type='script'):
                if cmds.getAttr('%s.b' % i, l = True):
                    is_lock_timeline.append(True)
            if True not in is_lock_timeline:
                cmds.confirmDialog( title = u'提示', message = u'已成功解锁时间线', button = ['OK'])
    else:
        cmds.confirmDialog(title = u"提示", message = u"时间线并未被锁, 不需要解锁", button = ['OK'])


def render_setting():
    """
    设置渲染设置参数的方法，特别注意分辨率的设置方式
    """
    import mtoa.core

    # 创建一个天空光照
    mtoa.utils.createLocator("aiSkyDomeLight", asLight=True)

    # settings中记录了需要设置到渲染设置中的参数；需要特别注意分辨率的设置：需要同时设置：defaultResolution.width、defaultResolution.height、
    # defaultResolution.deviceAspectRatio这三个属性
    settings = {"defaultArnoldRenderOptions.AASamples": 1,
                "defaultArnoldRenderOptions.GIDiffuseSamples": 1,
                "defaultArnoldRenderOptions.GISpecularSamples": 1,
                "defaultArnoldRenderOptions.GITransmissionSamples": 1,
                "defaultArnoldRenderOptions.GISssSamples": 1,
                "defaultArnoldRenderOptions.GIVolumeSamples": 1,
                "defaultArnoldRenderOptions.use_existing_tiled_textures": False,
                "defaultResolution.width": 640,
                "defaultResolution.height": 480,
                "defaultResolution.deviceAspectRatio": int(640/480)
                }

    for render_attr, value in settings.items():
        cmds.setAttr(render_attr, value)

def get_set_xgen_length_width():
    """
    获取xgen的descriptions的长度与宽度并且进行设置，具体的关于maya的xgen的api可以看maya官网关于xgen的介绍
    """
    import xgenm as xg
    length = None
    width =None
    set_value = True
    scale_value = 15

    for collection in xg.palettes():
        for description in xg.descriptions(collection):
            try:
                # 获取毛发description的长度和宽度
                primitive = xg.getActive(collection, description, 'Primitive')
                length = xg.getAttr('length', str(collection), str(description), str(primitive))
                width = xg.getAttr('width', str(collection), str(description), str(primitive))
                # print(len, width)
                
                des_length = float(length.split(";")[0].split("=")[-1])
                des_width = float(width.split(";")[0].split("=")[-1])
                
                target_length = des_length*scale_value
                target_width = des_width*scale_value
                length = length.replace(str(des_length), str(target_length))
                width = width.replace(str(des_width), str(target_width))
                
                #print(length, width)
                #print(str(des_length), str(target_length), str(des_width), str(target_width))
            except:
                print("xxxxxxxxxxxxxxxxxxxxxxxx{}".format(description))
            if set_value == True:
                xg.setAttr('length', length, collection, description, primitive)
                xg.setAttr('width', width, collection, description, primitive)


def move_keyframe(fbx_dir, fbx_export_dir):
    """
    批量将一个文件夹中的所有fbx的动画偏移到第0帧，并且重新输出到一个新的文件夹中
    """
    def get_file_list(fbx_dir):
        """
        获取一个文件夹中的所有fbx文件，作为一个列表返回
        """
        fbx_filename_list = []
        file_list = os.listdir(fbx_dir)
        for file_name in file_list:
            if file_name.split(".")[1] == "fbx":
                fbx_filename_list.append(os.path.join(fbx_dir, file_name))
        return fbx_filename_list

    def move_fbx_frame(import_filename, export_dir):
        export_filename = os.path.join(export_dir, os.path.basename(import_filename))
        
        #cmds.file(newFile=True, force=1)
        #cmds.file(import_filename, i=True)
        # 强行打开一个fbx文件
        cmds.file(import_filename, open = True, force=True)
        
        # 选择所有的变换（transform）节点，一般变换节点才有动画
        cmds.select(cmds.ls(type='transform'))
        #cmds.select("DeformationSystem",add=True)
        
        # 获取具有动画的最小帧和最大帧时间线位置
        start = min(cmds.keyframe(q=1))
        end = max(cmds.keyframe(q=1))

        # 将选择的对象的动画全部偏移到第0帧，设置时间线范围
        cmds.keyframe(edit = 1, at = ['tx','ty','tz','rx','ry','rz','sx','sy','sz', 'visibility'], timeChange = -start, relative = 1)
        cmds.playbackOptions(animationStartTime = 0, animationEndTime = end - start)
        
        # 导出fbx文件
        pm.mel.FBXResetExport()
        pm.mel.FBXExport(f = export_filename)
        print(u"export:{}finalish!".format(export_filename))
    
    # 获取fbx文件列表
    file_list = get_file_list(fbx_dir)

    # 测试3个文件的方法
    def test(in_file_list):
        for i in range(3):
            move_fbx_frame(in_file_list[i], fbx_export_dir)
    #test(file_list)

    # 批量跑任务
    for fbx_file_name in file_list:
        move_fbx_frame(fbx_file_name, fbx_export_dir)

    #cmds.file(newFile=True, force=1)


def clean_unknowns():
    """
    清理无效节点和插件
    """
    unknown_nodes = cmds.ls(type="unknown")
    #清除无效节点
    if unknown_nodes:
        cmds.delete(unknown_nodes)
    # 清除无效插件（未安装的插件）
    unknown_plugins = cmds.unknownPlugin(query=True, list=True)
    if unknown_plugins:
        for plugin in unknown_plugins:
            try:
                cmds.unknownPlugin(plugin, remove=True)
            except Exception as error:
                # Oddly enough, even if a plugin is unknown, it can still have a dependency in the scene.
                # So in this case, we log the error to look at after.
                print("Unknown plugin cannot be removed due to ERROR: {}".format(error))






