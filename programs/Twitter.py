# Name: Twitter/X
# Desc: Open Twitter/X + query
# Calls: twitter, twit, twt, tw, x

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '%20')
    webbrowser.open(f'https://twitter.com/search?q={query}&src=typed_query')
else:
    webbrowser.open('https://www.twitter.com/')