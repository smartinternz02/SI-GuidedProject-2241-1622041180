import requests

url = "https://japerk-text-processing.p.rapidapi.com/sentiment/"

payload = "text=great%20movie&language=english"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "e20c6ee4b2msha3baddc9742b4b6p1f2b79jsna4363e849479",
    'x-rapidapi-host': "japerk-text-processing.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
