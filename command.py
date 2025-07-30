# command
# module responsible for parsing /programs
# and running them within gizmo's ecosys

import sys, os


def parse_pyfile(filename):
    # Return name, description, and calls
    # parsed from a python file; assumed
    # to be a proper gizmo program.
    # open the file,
    with open(filename, 'r') as file:
        # get its contents,
        contents = file.read().strip()
        # put lines into a list,
        lines = contents.split('\n')
        # first three lines will be
        # 0. Name of the program
        # 1. Description of the program
        # 2. Calls, what triggers the program
        # set vars with these respective names,
        # from the lines read from contents
        name = lines[0].replace('# Name: ', '')
        desc = lines[1].replace('# Desc: ', '')
        calls = lines[2].replace('# Calls: ', '')
        calls = calls.split(', ')
    # finally, return these vars
    return name, desc, calls


def find_program(prompt):
    # Return a program path + arguments,
    # if we can find a program triggered
    # in the given prompt (string).
    # first, we need to break down the prompt
    # separate all terms from the prompt
    prompt_terms = prompt.split(' ')
    # the first term should be the command
    would_be_command = prompt_terms[0]
    try:
        # if there are arguments...
        slices = prompt_terms[1:]
        arguments = ' '.join(slices)
    except:
        # there may be no arguments;
        # in this case just set to blank
        arguments = ''
    # begin to loop over all files in /programs,
    for subdir, dirs, files in os.walk('programs'):
        # and for each file,
        for file in files:
            # make sure we only look at .py files,
            filepath = os.path.join(subdir, file)
            if filepath.endswith('.py'):
                # attempt to parse this file,
                try:
                    name, desc, calls = parse_pyfile(filepath)
                    # now, if our would_be command is one of
                    # this program's calls (triggers),
                    if would_be_command in calls:
                        # return the program's path and arguments
                        return filepath, arguments
                except:
                    return '', ''
    return '', ''


def run(program, arguments):
    # run the specified program with its arguments;
    # this is pretty straightforward.
    if sys.platform.lower() == 'linux':
        # linux uses python3,
        os.system(f'python3 {program} {arguments}')
    else:
        # otherwise just use python.
        os.system(f'python {program} {arguments}')