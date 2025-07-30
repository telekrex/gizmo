# Name: Research
# Desc: Combined search: google + brave + wikipedia + youtube + reddit + twitter
# Calls: research, search, searchall, ~

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '+')
    webbrowser.open(f'https://search.brave.com/search?q={query}&source=desktop')
    webbrowser.open(f'https://en.wikipedia.org/w/index.php?fulltext=1&search={query}')
    webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
    webbrowser.open(f'https://www.google.com/search?q={query}')
    webbrowser.open(f'https://www.reddit.com/search/?q={query}')
    webbrowser.open(f'https://twitter.com/search?q={query}&src=typed_query')
else:
    print('  No search term found! What are you doing, mate?')