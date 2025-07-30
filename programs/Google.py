# Name: Google
# Desc: Open Google + query
# Calls: google

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.google.com/search?q={query}')
else:
    webbrowser.open(f'https://google.com')