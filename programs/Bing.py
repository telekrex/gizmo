# Name: Bing
# Desc: Open Bing + query
# Calls: bing, bng

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.bing.com/search?q={query}')
else:
    webbrowser.open(f'https://bing.com')