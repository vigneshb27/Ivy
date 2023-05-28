import webbrowser

def opener(output):
    strt = 'https://'
    end = '.com/'
    splited_output = output.split()
    site = splited_output[-1]

    site = site.strip()
    webbrowser.open(strt + site + end)