import webbrowser


def youtube(output):
    url = 'https://youtube.com/'
    query = '/results?search_query='
    splited_output = output.split()

    if 'search' in splited_output:
        search = ""
        ind = splited_output.index('search')
        for i in range(ind + 1, len(splited_output)):
            if splited_output[ind + 1] not in ['with', 'for', 'as']:
                search += ' ' + splited_output[i]
            elif i != ind + 1:
                search += ' ' + splited_output[i]

        search = search.strip()
        webbrowser.open(url + query + search)
    else:
        webbrowser.open(url)
