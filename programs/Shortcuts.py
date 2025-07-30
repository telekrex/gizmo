# Name: Shortcuts
# Desc: List all shortcuts, or edit
# Calls: shortcuts, sc

import os

num = 0
print('  All shortcuts:\n')
with open('shortcuts.txt', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        if line:
            try:
                parts = line.split(' | ')
                calls = parts[0]
                type = parts[1]
                url = parts[2]
                print(f'  {calls}')
                num += 1
            except:
                pass

print(f'\n   {num} shortcuts')