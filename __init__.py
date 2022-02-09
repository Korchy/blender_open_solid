# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_open_solid

import bpy
from bpy.app.handlers import persistent
from . import open_solid_ops
from . import open_solid_ui
from .open_solid import OpenSolid
from .addon import Addon

bl_info = {
    'name': 'OpenSolid',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': 'In background',
    'doc_url': 'https://b3d.interplanety.org/en/blender-add-on-open-solid/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-open-solid/',
    'description': 'Open .blend with solid 3D Viewport mode'
}


@persistent
def open_solid_register():
    # register OpenSolid
    if bpy.context and hasattr(bpy.context, 'scene'):
        OpenSolid.register(context=bpy.context)
    else:
        return 0.25


def register():
    if not Addon.dev_mode():
        # open_solid_ops.register()
        # open_solid_ui.register()
        bpy.app.timers.register(
            function=open_solid_register,
            first_interval=0.25
        )
    else:
        print('It seems you are trying to use the dev version of the '
              + bl_info['name']
              + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        OpenSolid.unregister()
        # open_solid_ui.unregister()
        # open_solid_ops.unregister()


if __name__ == '__main__':
    register()
