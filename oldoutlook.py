import requests

def outlook(email):
    
    url = 'https://login.live.com//GetCredentialType.srf?opid=E20A6406BC861088&id=292841&cobrandid=90015&id=292841&mkt=EN-US&lc=1033&uaid=920b14d5d6bf44ffa016db850db98351'

    # Define the payload template (without the username)
    payload_template = {
        "isOtherIdpSupported": True,
        "checkPhones": False,
        "isRemoteNGCSupported": True,
        "isCookieBannerShown": False,
        "isFidoSupported": True,
        "country": "US",
        "forceotclogin": False,
        "isExternalFederationDisallowed": False,
        "isRemoteConnectSupported": False,
        "federationFlags": 0,
        "isSignup": False,
        "flowToken": "AQABAAEAAAAtyolDObpQQ5VtlI4uGjEPmVTvB5eZTaL_xvRdNX8zoF_M9oCPfpR1_3-Wz9ETrDbl5ca9Avq0LYJkoyoMgY5LIhrw_zFYKZPKDynsKoHPZfgeKmWiIAs1DXbLOrj1FwddvGzTm1ABWqIWhpNkryjIGv9-pljgbUnhPWj9pTn9ffvUpp8V2MtaAhrj46pyDne0WQmgpo5yxrOcie6NRDmX-vIRN1MIuXjLJ27VP51D0OM2hEp1OD47P6dtU6fk3-n2oCqUh1nP1tJCP1Pr47Uw2d3Hx3uCPYHHQJ8S3DkYwNqi4ieYGWQoRIaGrswGKuHiQRsyIuf8jtXEVXyOGqJhVIrV13orhsMe8QFdNAQE95yTcr7oSV6cXL7EWJdelszMsPUosCWSNdpwVI3lFGrKkYHetSaT2PrQem5AJIKBpKpvdLzk4q_P1P5_HA5hrOLCjH451cW4GJ2aVLL8wejgiEdppAzICHiHJOAthyGUP1R7w0z62wD6Ml9QOrRuqGS1KRxOCycJSUhLQcXDX5yIL1PCokaNJIAca5y1wkJb4zMbwhsGoVaUnWZK8XjTWYovsLqEn1dvUW_GrQxdQzwyIAA",
        "isAccessPassSupported": True,
        "username": email
    }


    headers = {
        "Host": "login.microsoftonline.com",
        # (other headers here)
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close"
    }

    response = requests.post(url,json=payload_template, headers=headers)
    x = response.json()
    print(x)
    
    if_exists_result = x["IfExistsResult"]
    # print(if_exists_result)
    if if_exists_result == 5 or if_exists_result == 0:
        
        return('valid')

    else:
        print(if_exists_result)
        return('invalid')
    