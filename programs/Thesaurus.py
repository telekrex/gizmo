# Name: Thesaurus
# Desc: Open Thesaurus.com + query
# Calls: thesaurus

import webbrowser, sys
if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    query = query.replace(' ', '%20')
    webbrowser.open(f'https://www.thesaurus.com/browse/{query}')
else:
    webbrowser.open(f'https://thesaurus.com')