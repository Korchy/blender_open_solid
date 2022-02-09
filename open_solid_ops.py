# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .open_solid import open_solid


class OPEN_SOLID_OT_main(Operator):
    bl_idname = 'open_solid.main'
    bl_label = 'open_solid: main'
    bl_description = 'open_solid - main operator'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        open_solid.open_solid(
           context=context
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return True


def register():
    register_class(OPEN_SOLID_OT_main)


def unregister():
    unregister_class(OPEN_SOLID_OT_main)
