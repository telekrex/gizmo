# Name: GitHub
# Desc: Open GitHub + query
# Calls: gh, github

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '%20')
    webbrowser.open(f'https://github.com/search?q={query}&type=repositories')
else:
    webbrowser.open(f'https://github.com/')