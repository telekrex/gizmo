# Name: Dictionary
# Desc: Open Dictionary.com + query
# Calls: dictionary

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '-')
    webbrowser.open(f'https://www.dictionary.com/browse/{query}')
else:
    webbrowser.open(f'https://dictionary.com')