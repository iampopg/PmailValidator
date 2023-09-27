import requests

def outlook(email):
    url = "https://login.live.com/GetCredentialType.srf?opid=E20A6406BC861088&id=292841&cobrandid=90015&id=292841&mkt=EN-US&lc=1033&uaid=920b14d5d6bf44ffa016db850db98351"

    headers = {
        "Host": "login.live.com",
        "Cookie": "logonLatency=LGN01=638314009268568894; uaid=920b14d5d6bf44ffa016db850db98351; MSPRequ=id=292841&lt=1695804127&co=1; MSCC=129.205.113.166-NG; OParams=11O.DXHudZ6kWSPTjJUi5IDqD4KpEUlLpA0iH0PEjwdoFgCynEZYVN6NI5czkPggg2LbGLZSpJMQUwv3mjrtNJFvmubsH86vLYf3yIAPjnUmrlIBTWcUASFC0V3pwZRWwSmjRh4n5Vg3ccCKcsKBCnp11VbdlqOHmeMS5byWfkachFo*R2IR9CKTc8OebLYfAdI64QJlslh4uz!UwLtjquzPWFeedvd*GxyEjAJmgnGORr8B0LpjhJ8U3P3*I1vNEFG!DA4VdsGotc92x9AyXZKfhLROy4aIq5Q8ZePziGw92YVaY7*Y2zAGW9gX6FY*lfuekFrd5zgPveTyggcv*Zv4f!IhqVeuExshhGu5*KiWUMagbXNqyBbFKVXjVo*XBwifZPH5WIeZcffFrYPxr3yVLWQ$; MicrosoftApplicationsTelemetryDeviceId=2fe78802-2998-4de6-8454-3a26390a72db; MSPOK=$uuid-00719c4e-4a7a-4abb-975a-59efb6d94fa4$uuid-b7634892-e73f-42aa-a269-0e601903e3eb$uuid-ced79d02-6924-4f9c-b375-ece945060213$uuid-530ba6b6-95f1-4823-aaa8-a79e87361813; ai_session=7nmGXiGKQJeO+mH/u4/Cvh|1695804136015|1695804136015; MSFPC=GUID=75ca84759a7b49cb9270fe16e37a4d19&HASH=75ca&LV=202309&V=4&LU=1695804139050",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=16&ct=1695804126&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d1de62e38-f966-749f-c3bf-4f31c9bca49a&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015",
        "Hpgid": "33",
        "Hpgact": "0",
        "Client-Request-Id": "920b14d5d6bf44ffa016db850db98351",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": "612",
        "Origin": "https://login.live.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers",
        "Connection": "close"
    }

    payload = {
        "username": email,
        "uaid": "920b14d5d6bf44ffa016db850db98351",
        "isOtherIdpSupported": True,
        "checkPhones": False,
        "isRemoteNGCSupported": True,
        "isCookieBannerShown": False,
        "isFidoSupported": True,
        "forceotclogin": False,
        "otclogindisallowed": False,
        "isExternalFederationDisallowed": False,
        "isRemoteConnectSupported": False,
        "federationFlags": 3,
        "isSignup": False,
        "flowToken": "-DYnn!lCkHP8PszeLrmVlEVGGEyV!gLob8b7uhq5X7HDF!NRohul0q2dTfywaF3JcNO9GeOaVL9cRFVqEmz7q7v4rZ32MMVygwIArMpnnE6JnX2703S2J5HAmp1wh*mJWQQMBXib7z3kIFNHRfsmXFlzB!WeDL3G4cnVyguTtNMtyNS8J6abqIWL4DUJ79!*aw6hPbSPJoIVSTfm3UX6JLRZ7F8Tmzg1pBLnAxOC9DSiC"
    }
    try:
        response = requests.post(url,json=payload, headers=headers)
        x = response.json()
        
        
        
        if_exists_result = x["IfExistsResult"]
        # print(if_exists_result)
        
       
        isSADef = x['Credentials']['OtcLoginEligibleProofs'][0]['isSADef']
            
        if isSADef == False:
            return "dead"
        else:
            if if_exists_result == 5 or if_exists_result == 0:
                
                return('valid')
            else:
                # print(if_exists_result)
                return('invalid')
    except KeyError:
        response = requests.post(url,json=payload, headers=headers)
        x = response.json()
        if_exists_result = x["IfExistsResult"]
        if if_exists_result == 5 or if_exists_result == 0:
                
            return('valid')
        else:
            # print(if_exists_result)
            return('invalid')
    except Exception as e:
        pass