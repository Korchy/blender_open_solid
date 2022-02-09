# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/

from . import open_solid_ops
from . import open_solid_ui
from .addon import Addon


bl_info = {
    'name': 'open_solid',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '',
    'wiki_url': 'https://b3d.interplanety.org/en/',
    'tracker_url': 'https://b3d.interplanety.org/en/',
    'description': ''
}


def register():
    if not Addon.dev_mode():
        open_solid_ops.register()
        open_solid_ui.register()
    else:
        print('It seems you are trying to use the dev version of the '
           + bl_info['name']
           + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        open_solid_ui.unregister()
        open_solid_ops.unregister()


if __name__ == '__main__':
    register()
