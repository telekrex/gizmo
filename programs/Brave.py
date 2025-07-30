# Name: Brave
# Desc: Opens Brave Search + query
# Calls: $, brave, brv, bra

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://search.brave.com/search?q={query}&source=desktop')
else:
    webbrowser.open('https://search.brave.com/')