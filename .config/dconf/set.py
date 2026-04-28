import os
from subprocess import check_call

dconf_setting = [
    {
        'path': 'org.gnome.desktop.interface',
        'kv': [

            #@reference_tag(cursor_theme)
            ['cursor-blink', 'false'],
            ['cursor-size', os.environ['XCURSOR_SIZE']],
            ['cursor-theme', os.environ['XCURSOR_THEME']],

            #@reference_tag(font)
            ['font-name', 'system-ui 12'],
            ['document-font-name', 'serif 13'],
            ['monospace-font-name', 'monospace 13'],
            ['font-hinting', 'slight'],
            ['font-rendering', 'manual'],

            ['gtk-im-module', os.environ['INPUT_METHOD']],
            ['gtk-theme', os.environ['GTK_THEME']],
            ['color-scheme', 'prefer-dark'],
            ['icon-theme', os.environ['ICON_THEME']],
        ],
    }
]

for i in dconf_setting:
    for j in i['kv']:
        check_call(['gsettings', 'set'] + [i['path']] + j)
