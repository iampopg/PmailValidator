import requests

url = "https://geo.yahoo.com/p"
headers = {
    "Host": "geo.yahoo.com",
    "Cookie": "A3=d=AQABBMAV_2QCEPOdGqmVO5g-E61EBoY0NDEFEgEBAQFnAGUIZY14zSMA_eMAAA&S=AQAAAgvpZlTBjqpMHkc6Q1Qv8us",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
    "Sec-Ch-Ua-Platform": "",
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Dest": "image",
    "Referer": "https://login.aol.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"
}

params = {
    "username": "sadja@aol.com",

}

response = requests.get(url, headers=headers, params=params)

print(response.text)
