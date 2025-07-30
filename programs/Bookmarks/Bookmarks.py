# Name: Bookmarks
# Desc: Quickly save or read notes and links
# Calls: bookmark, bookmarks, bmark, bm, mk

import os, sys


if len(sys.argv) > 1:
    # build entry text from sys argv
    entry = ' '.join(sys.argv[1:])
  
    if entry:
        # entry is to be saved in the bookmark file
        with open('programs/Bookmarks/Bookmarks.txt', 'a+') as file:
            file.write(entry + '\n')
            print(f'  {entry} added to bookmarks')

# or, if nothing was entried,
else:
    print(f'  Bookmarks:')
    # than just list the contents of the bookmarks file
    with open('programs/Bookmarks/Bookmarks.txt', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            if line:
                print(f'  {line}')
        print()