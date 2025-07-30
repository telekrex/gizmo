# Name: Reddit
# Desc: Open Reddit + query
# Calls: reddit, redd, red, redit

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.reddit.com/search/?q={query}')
else:
    webbrowser.open(f'https://www.reddit.com')