# IGGLightArchiveTool
import unreal as ue
import WorldFunctions as wf
import json

# use_selection: bool : True if you want to get only the selected actors
# actor_class: class unreal.Actor : The class used to filter the actors. Can be None if you do not want to use this filter
# actor_tag: str : The tag used to filter the actors. Can be None if you do not want to use this filter
# world: obj unreal.World : The world you want to get the actors from. If None, will get the actors from the currently open world.
# return: obj List unreal.Actor : The actors
# def getAllActors(use_selection=False, actor_class=None, actor_tag=None, world=None):
def getAllLights():
    allLights = wf.getAllActors(False, ue.Light, None, None)
    skylight = wf.getAllActors(False, ue.SkyLight, None, None)
    # allLights.append(skylight)
    return allLights

# def getData(s):
#     s = str(s)
#     if ')' in s and '<' in s:
#         return s.split(')')[1].split('>')[0].strip()
#     else:
#         return s

def makeLightDict(lightActors):
    lightDict = {}

    for item in lightActors:
        t = item.get_actor_transform()

        propertyDist = {}
        propertyDist['LightType'] = item.get_full_name().split(' ')[0]
        propertyDist['Intensity'] = item.get_brightness()
        propertyDist['Position'] = t.to_tuple()[0].to_tuple() 
        propertyDist['Rotation'] = t.to_tuple()[1].to_tuple() # euler
        propertyDist['LightColor'] = item.get_light_color().to_rgb_vector().to_tuple()

        lightName = item.get_name()
        lightDict[lightName] = propertyDist

        


    # for attr in dir(lightActors[0]):
    #     ue.log_warning(attr)
    # ue.log_warning(item.get_light_color().to_rgb_vector().to_tuple())

    return lightDict

def printAll(data):
    ue.log_warning(data)

def makeJson(d):
    res = json.dumps(d)

    with open('D:/Git/UEGym/BasicScripting/Saved/IGGLightArchive.json', 'w') as json_file:
        json.dump(d, json_file, indent=4)

    return res

def runTool():
    makeJson(makeLightDict(getAllLights()))
    printAll('Run IGGLightArchiveTool...')
    printAll('DONE!')

