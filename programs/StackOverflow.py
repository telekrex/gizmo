# Name: StackOverflow
# Desc: Open StackOverflow + query
# Calls: stack, overflow, stck, stackov

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://stackoverflow.com/search?q={query}')
else:
    webbrowser.open(f'https://stackoverflow.com')