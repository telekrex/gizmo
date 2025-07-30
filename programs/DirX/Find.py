# Name: Find/ DirX
# Desc: Search for and open a given directory or file
# Calls: find, dir, gimme, getme, grab, pu, open


import os, sys


ext = [
    '.txt',
    '.md',
    '.html',
    '.ods',
    '.odt',
    '.png',
    '.jpg',
    '.jpeg',
    '.mp4'
]


def find(thing):
    with open('Programs/DirX/roots.txt', 'r') as rootsfile:
        roots = rootsfile.read().split('\n')
        for root in roots:
            for subdir, dirs, files in os.walk(root):
                for file in files:
                    if file == query:
                        return f'{subdir}\{file}'
                for directory in dirs:
                    if directory == query:
                        return f'{subdir}\{directory}'


if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    # if argument is "roots",
    # list the roots on file
    if query == 'roots':
        with open('Programs/Homebrew/DirX/roots.txt', 'r') as rootsfile:
            roots = rootsfile.read().split('\n')
            print('  roots:')
            for root in roots:
                print(f'  {root}')
    else:
        # otherwise,
        # perform regular program
        print(f'  searching for {query}...')
        x = find(query)
        if x:
            print(f'  opening {x}...')
            os.system(f'start {x}')
        else:
            print(f'  {query} could not be found.')