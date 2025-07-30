# shortcuts
# module responsible for parsing and
# launching contents of shortcuts.txt

import sys, os, webbrowser


def identify_shortcut(entry):

    with open('shortcuts.txt', 'r') as launcherfile:
        entries = launcherfile.read().split('\n')
    
    for e in entries:
        if e:
            try:
                parts = e.split(' | ')
                alias = parts[0]
                typea = parts[1]
                sourc = parts[2]
                aliases = alias.lower().strip().split(', ')
                if ', ' in sourc:
                    sources = sourc.split(', ')
                else:
                    sources = [sourc]

                if entry.lower().strip() in aliases:
                    return typea, sources
            
            except Exception as x:
                print(f'ERROR: Shortcut does not contain valid line: {e}')
    
    return None, None


def launch_file_or_folder(addresses):
    for item in addresses:
        os.system(fr'start {item}')


def launch_url(addresses):
    for item in addresses:
        webbrowser.open(item)