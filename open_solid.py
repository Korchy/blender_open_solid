# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_open_solid

import bpy
from bpy.app.handlers import persistent


class OpenSolid:

    @staticmethod
    def to_solid(context):
        # switch all 3D Viewport areas to the "Solid" mode
        if context:
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    if area.spaces[0].shading.type in ['MATERIAL', 'RENDERED']:
                        area.spaces[0].shading.type = 'SOLID'

    @staticmethod
    def register():
        # register
        if inst_col_on_scene_load_post not in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.append(inst_col_on_scene_load_post)

    @staticmethod
    def unregister():
        # unregister
        if inst_col_on_scene_load_post in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.remove(inst_col_on_scene_load_post)


@persistent
def inst_col_on_scene_load_post(*args):
    # on scene load post
    OpenSolid.to_solid(context=bpy.context)
