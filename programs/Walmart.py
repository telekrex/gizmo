# Name: Walmart
# Desc: Open Walmart.com + query
# Calls: walmart, supermarket

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.walmart.com/search?q={query}')
else:
    webbrowser.open(f'https://walmart.com')