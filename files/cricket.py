from bs4 import BeautifulSoup
import requests

def cricket_score():
    html_text = requests.get('https://www.cricbuzz.com/').text
    soup = BeautifulSoup(html_text, "html.parser")
    sect = soup.find_all('li', class_='cb-match-card')
    section = sect[0]

    team_one = section.find('div', class_ = 'cb-hmscg-bwl-txt')
    #team_one  = team_one.find('div', class_ = 'cb-hmscg-tm-name')
    team_one_name = team_one.find('span')['title']
    team_one_score = team_one.find_all('div', class_ = 'cb-ovr-flo')[1].text

    team_two = section.find('div', class_ = 'cb-hmscg-bat-txt')
    #team_two  = team_two.find('div', class_ = 'cb-hmscg-tm-name')
    team_two_name = team_two.find('span')['title']
    team_two_score = team_two.find_all('div', class_ = 'cb-ovr-flo')[1].text

    result = section.find('div', class_ = 'cb-mtch-crd-state')
    final_result = result.text

    # print(team_one_name)
    # print(team_one_score)
    # print(team_two_name)
    # print(team_two_score)
    # print(final_result)
    arr = [team_one_name, team_one_score, team_two_name, team_two_score, final_result]

    ans = '\n'.join(arr)
    return ans