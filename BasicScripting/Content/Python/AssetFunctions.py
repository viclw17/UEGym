import unreal 

texture_png = 'D:/Git/UEGym/BasicScripting/unreal.png'
sound_wav =  'D:/Git/UEGym/BasicScripting/Explosion01.WAV'
def importMyAssets():
    texture_task = buildImportTask(texture_png, '/Game/Textures')
    sound_task = buildImportTask(sound_wav, '/Game/Sounds')
    executeImportTasks([texture_task, sound_task])

# unreal.AssetImportTask
def buildImportTask(filename, destination_path):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '') # llama
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    return task

# unreal.AssetTools
def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            print 'Imported: %s' % path