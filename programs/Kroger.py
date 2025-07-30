# Name: Kroger
# Desc: Open Kroger.com + query
# Calls: kroger, groceries

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.kroger.com/search?query={query}&searchType=default_search')
else:
    webbrowser.open(f'https://kroger.com')