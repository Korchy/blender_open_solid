# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class OPEN_SOLID_PT_panel(Panel):
    bl_idname = 'OPEN_SOLID_PT_panel'
    bl_label = 'open_solid'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'open_solid'

    def draw(self, context):
        self.layout.operator('open_solid.main', icon='BLENDER', text='open_solid execute')


def register():
    register_class(OPEN_SOLID_PT_panel)


def unregister():
    unregister_class(OPEN_SOLID_PT_panel)
