# Name: Wikipedia
# Desc: Open Wikipedia + query
# Calls: wikipedia, wiki, wp

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://en.wikipedia.org/w/index.php?fulltext=1&search={query}')
else:
    webbrowser.open(f'https://en.wikipedia.org')