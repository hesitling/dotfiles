from subprocess import check_call

dconf_setting = [
    {
        'path': 'org.gnome.desktop.interface',
        'kv': [

            #@reference_tag(cursor_theme)
            ['cursor-blink', 'false'],
            ['cursor-size', '28'],
            ['cursor-theme', 'GoogleDot-White'],

            #@reference_tag(font)
            ['font-name', 'system-ui 12'],
            ['document-font-name', 'serif 13'],
            ['monospace-font-name', 'monospace 13'],
            ['font-hinting', 'slight'],
            ['font-rendering', 'manual'],

            ['gtk-im-module', 'fcitx'],
            ['gtk-theme', 'Breeze-Dark'], #@reference_tag(gtk_theme)
            ['color-scheme', 'prefer-dark'],
            ['icon-theme', 'Breeze'], #@reference_tag(icon_theme)
        ],
    }
]

for i in dconf_setting:
    for j in i['kv']:
        check_call(['gsettings', 'set'] + [i['path']] + j)
