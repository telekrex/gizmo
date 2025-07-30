# Name: YouTube
# Desc: Opens YouTube + query
# Calls: youtube, yt, yout

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
else:
    webbrowser.open('https://www.youtube.com')