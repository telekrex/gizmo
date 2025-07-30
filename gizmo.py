import webbrowser
import shortcuts
import command
import sys
import os


try:
    # linux
    if sys.platform.lower() == 'linux':
        os.system('clear')
        # dont know Linux for "set window title"
        # as I've had issues making this work because
        # of the infinite terminal emulators out there
    # windows
    else:
        os.system('cls')
        os.system('title Gizmo')
except:
    pass


if __name__ == "__main__":
    while True:
        i = input('> ')
        print()
        if i:
            # split input into parts, if parts
            try:
                instructions = i.split(', ')
            except:
                instructions = [i.strip()]
            
            for instruction in instructions:
                instruction = instruction.strip()

                # try to find a command in the instruction text
                c, args = command.find_program(instruction)
                if c:
                    # if we found one, run it
                    command.run(c, args)
                    print()
                
                # try to find a shortcut in the instruction text
                shortcut_type, sources = shortcuts.identify_shortcut(instruction)
                if shortcut_type:
                    if shortcut_type == 'url':
                        shortcuts.launch_url(sources)
                    if shortcut_type == 'file':
                        shortcuts.launch_file_or_folder(sources)
                    if shortcut_type == 'folder':
                        shortcuts.launch_file_or_folder(sources)
                
                # if a domain is likely present
                if '.' in instruction:
                    # ignore adding things to bookmarks
                    if not instruction.startswith('bm'):
                        # try to open the url in browser
                        for domain in ['.com', '.org', '.net']:
                            if domain in instruction:
                                webbrowser.open(f'https://{instruction}')

                # in other case,                
                else:
                    print()

        else:
            break