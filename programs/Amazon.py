# Name: Amazon
# Desc: Open Amazon + query
# Calls: amazon, shopping, am, ama, amaz, shop, store

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.amazon.com/s?k={query}')
else:
    webbrowser.open(f'https://www.amazon.com')