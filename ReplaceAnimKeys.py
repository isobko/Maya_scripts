import maya.cmds as cmds

REPLACE_NUMBER = 0
COMPARE = 0.01

def replaceKey():
    objs = cmds.ls(selection=True)
    for item in objs:
        times = cmds.keyframe(item, query=True, timeChange=True)
        values = cmds.keyframe(item, query=True, valueChange=True)
        for i in values:
            if i <= COMPARE:
                cmds.setKeyframe(item, time=times[0], value=REPLACE_NUMBER, at='scaleX')
                cmds.setKeyframe(item, time=times[0], value=REPLACE_NUMBER, at='scaleY')
                cmds.setKeyframe(item, time=times[0], value=REPLACE_NUMBER, at='scaleZ')

replaceKey()