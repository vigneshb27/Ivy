import requests

def stocks():
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"function":"GLOBAL_QUOTE","symbol":"BK"}

    headers = {
        "X-RapidAPI-Key": "e2989ccabcmsh01fccc90f05d285p111414jsnaad35efe3848",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    return response['Global Quote']