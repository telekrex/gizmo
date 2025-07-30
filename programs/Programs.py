# Name: Programs
# Desc: List all installed programs/scripts
# Calls: programs, help, commands, prog, com


import os


def parse_pyfile(filename):
    # assuming this is in fact a python file
    with open(filename, 'r') as file:
        contents = file.read().strip()
        lines = contents.split('\n')
        # first three lines will be
        # 0. Name
        # 1. Desc
        # 2. Calls
        if lines[0].startswith('# Name: '):
            name = lines[0].replace('# Name: ', '')
            desc = lines[1].replace('# Desc: ', '')
            calls = lines[2].replace('# Calls: ', '')
            calls = calls.split(', ')
            return name, desc, calls


num = 0
print('  All programs:\n')
for subdir, dirs, files in os.walk('programs/'):
    for file in files:
        filepath = os.path.join(subdir, file)
        if filepath.endswith('.py'):
            try:
                name, desc, calls = parse_pyfile(filepath)
                print(f'  {name} ...... {desc} ..... {", ".join(calls)}')
                num += 1
            except Exception as e:
                pass
print(f'\n  {num} programs')