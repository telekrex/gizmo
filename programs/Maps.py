# Name: Maps
# Desc: Open Google Maps + query
# Calls: maps, map, locate

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.google.com/maps/search/{query}/')
else:
    webbrowser.open(f'https://www.google.com/maps/')