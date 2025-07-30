# Name: IMDB
# Desc: Open IMDB + query
# Calls: imdb, movies

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '%20')
    webbrowser.open(f'https://www.imdb.com/find/?q={query}')
else:
    webbrowser.open(f'https://imdb.com')