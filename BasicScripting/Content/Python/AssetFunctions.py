import unreal 

### string path for assets 
# texture_png = 'D:/Git/UEGym/BasicScripting/unreal.png'
# sound_wav =  'D:/Git/UEGym/BasicScripting/Explosion01.WAV'
static_mesh_fbx = 'D:/Git/UEGym/BasicScripting/bunny_low.FBX'
skeletal_mesh_fbx = 'D:/Git/UEGym/BasicScripting/SK_FBX_Tube.FBX'
animation_fbx = 'D:/Git/UEGym/BasicScripting/SK_FBX_Tube_Animation.FBX'

def importMyAssets():
    texture_task = buildImportTask(texture_png, '/Game/Textures')
    sound_task = buildImportTask(sound_wav, '/Game/Sounds')
    # executeImportTasks([texture_task, sound_task])
    static_mesh_task = buildImportTask(static_mesh_fbx, '/Game/StaticMeshes', buildStaticMeshImportOptions())
    skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, '/Game/SkeletalMeshes', buildSkeletalMeshImportOptions())
    # executeImportTasks([static_mesh_task, skeletal_mesh_task])
    animation_task = buildImportTask(animation_fbx, '/Game/Animation', buildAnimationImportOptions('/Game/SkeletalMeshes/SK_FBX_Tube_Skeleton'))
    # executeImportTasks([animation_task])
    executeImportTasks([static_mesh_task])

# unreal.AssetImportTask https://docs.unrealengine.com/en-US/PythonAPI/class/AssetImportTask.html
def buildImportTask(filename, destination_path, options = None):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '') # llama
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    # options (Object): [Read-Write] Import options specific to the type of asset
    task.set_editor_property('options', options)
    return task

# unreal.AssetTools https://docs.unrealengine.com/en-US/PythonAPI/class/AssetTools.html
def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            print 'Imported: %s' % path

#######################################

def buildStaticMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI https://docs.unrealengine.com/en-US/PythonAPI/class/FbxImportUI.html
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', False) # static mesh
    # unreal.FbxMeshImportData https://docs.unrealengine.com/en-US/PythonAPI/class/FbxMeshImportData.html
    # unreal.FbxStaticMeshImportData https://docs.unrealengine.com/en-US/PythonAPI/class/FbxStaticMeshImportData.html
    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    
    options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)

    return options


def buildSkeletalMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI https://docs.unrealengine.com/en-US/PythonAPI/class/FbxImportUI.html
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', True)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', True)
    # unreal.FbxMeshImportData https://docs.unrealengine.com/en-US/PythonAPI/class/FbxMeshImportData.html
    # unreal.FbxStaticMeshImportData https://docs.unrealengine.com/en-US/PythonAPI/class/FbxStaticMeshImportData.html
    # property:static_mesh_import_data -> type:FbxSkeletalMeshImportData
    options.skeletal_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)

    options.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)
    options.skeletal_mesh_import_data.set_editor_property('update_skeleton_reference_pose', False)

    return options


def buildAnimationImportOptions(skeleton_path):
    options = unreal.FbxImportUI()
    options.set_editor_property('import_animations', True)
    options.skeleton = unreal.load_asset(skeleton_path) # unreal.load_asset()
    
    options.anim_sequence_import_data.set_editor_property('import_translation', unreal.Vector(0.0,0.0,0.0))
    options.anim_sequence_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0,0.0,0.0))
    options.anim_sequence_import_data.set_editor_property('import_uniform_scale', 1.0)

    options.anim_sequence_import_data.set_editor_property('animation_length', unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME)
    options.anim_sequence_import_data.set_editor_property('remove_redundant_keys', False)
    return options










###########################
# Save

# unreal.EditorAssetLibrary
def saveAsset():
    unreal.EditorAssetLibrary.save_asset('/Game/BP_Test', only_if_is_dirty=True)

def saveDirectory():
    unreal.EditorAssetLibrary.save_directory('/Game', only_if_is_dirty=True, recursive=True)

# unreal.Package
# https://docs.unrealengine.com/en-US/PythonAPI/class/Package.html
def getPackageFromPath():
    # print "call getPackageFromPath()"
    return unreal.load_package('/Game/BP_Test')

# unreal.EditorLoadingAndSavingUtils
# import AssetFunctions
# reload(AssetFunctions)
# print AssetFunctions.getAllDirtyPackages()
def getAllDirtyPackages():
    packages = unreal.Array(unreal.Package)
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_content_packages():
        packages.append(x)
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_map_packages():
        packages.append(x)
    return packages

# import AssetFunctions
# reload(AssetFunctions)
# print AssetFunctions.saveAllDirtyPackages()
def saveAllDirtyPackages(show_dialog=True):
    if show_dialog:
        unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog(save_map_packages = True, save_content_packages = True)
    else:
        unreal.EditorLoadingAndSavingUtils.save_dirty_packages(save_map_packages = True, save_content_packages = True)

# import AssetFunctions
# reload(AssetFunctions)
# print AssetFunctions.savePackages(AssetFunctions.getAllDirtyPackages(), True)
def savePackages(packages=[], show_dialog=False):
    if show_dialog:
        unreal.EditorLoadingAndSavingUtils.save_packages_with_dialog(packages, only_dirty=False) 
    else:
        unreal.EditorLoadingAndSavingUtils.save_packages(packages, only_dirty=False)
