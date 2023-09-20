import requests

url = "https://login.yahoo.com/?display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0&prompt=login&chllngnm=fail"
def yahoo(email):
    # url = "https://login.yahoo.com/?.intl=in"

    headers = {
        "Host": "login.yahoo.com",
        "Cookie": "A1=d=AQABBMAV_2QCEPOdGqmVO5g-E61EBoY0NDEFEgEBAQFnAGUIZY14zSMA_eMAAA&S=AQAAAgvpZlTBjqpMHkc6Q1Qv8us; A3=d=AQABBMAV_2QCEPOdGqmVO5g-E61EBoY0NDEFEgEBAQFnAGUIZY14zSMA_eMAAA&S=AQAAAgvpZlTBjqpMHkc6Q1Qv8us; A1S=d=AQABBMAV_2QCEPOdGqmVO5g-E61EBoY0NDEFEgEBAQFnAGUIZY14zSMA_eMAAA&S=AQAAAgvpZlTBjqpMHkc6Q1Qv8us&j=WORLD; AS=v=1&s=fmrlGgeV&d=A65010343|4rNa_xb.2QI8oFqY16dEUh.GkfRflsiMad7zvPzXKq4pUUliXIqu44LnhC933dzobKpebEYWNALmkhwJ8h0g0CA14rQlNUOdgbodAi01utLLSWoJ90.sTBl0PLJssSsl3YJHYHWa8OdWdsaqKpU4q6Mhf4x5lloR2tZadXQzReumKNHxbMYJSq2HaZWRkGXAwIo5vZo1kJyi9EiiIT.WvEWF3HrKlODj9zoRAf5i7_gtzWve.JjUwEDn4QzoxUoTOrmqtHMsqY46dd3E8rjGCg0lHvloPL1y7hYXZtwpmDSXvIwpCdRNRq5jsM4kC2PK6oPytbSWCE8KSJLAuYLuaC7GLL.kDljnAYEBFxuSPBTW2..WS8GdnDDnQS0KOzuNmGxVHlQ7JRIZqD_QDYhFg5Nsc8n23.lWlIiJm_fLGzZaVuzD7xMGriaAKEwqkYC4LBaiR9fBsXYgvQeC6Ixxvd9QiesLbEr3giAoBkhYAwEMjADJtPFKgmWWBJlZNo68I4zhHzFHpsPovcPgQ1qzvu6r1scIbQIZ5QagLdZS8c78NP7uoQ3sC4VAjqpfyXZ3G79dKDzxTSgXWkh_YKqVB2SpIyfLnrp.rpRyJiWdXaj8hvny.Ckq_g.pe38JtP33TjE4uCsFLPLJdE3j4C1yBK.Pl147O9vknbHauWGqVCxILhev8tvuasrLy9V4LtQKzLUrg4EyPAbjAJ1Q9SxRpGMnsYBEnao_Abr9sdSwQs12EyL9fcCHJsWU7tUYLfefXZBL_tdmuEo8fWhCSc8b5yJymDOM3pS._ObEYlPP5YldiUYSsIceVOdOjUihYsOdav5R9QJOohpkcwlb8gyl9abt3jSEM8dz18OfWIKT4Tx_w5XDuGVfBKrrW9Cjc6wvbnT_UQVKwOI42U0mqDoyW6gL4MSw2ILu4Q.hH9FNxooNpLZ8GWbB1v7qTciRg3iGhY3PmqPL9xT4djvqrwk2MhPP1G9Pm1XtwiMWpQY5_W8WyzktBjKKVUMCmlYMOVVKoYvaqkdJMH63dDhXaJNPXnUqDFdTstqYsbmZ1pubGyIB6gLxYOFbwiYO~A|B6502517b|Z8kVh8b.2RLHBO6NxK1oE4t.e7A9jDc11fa16MAH.dXZyhel5JxkfCZW6GiBz01AyPUdNWn7KkkTX78N7zltEqg1QtlTv.YA5NTVjUgdPdJfdpyYfGHs9lgjAi.MRA1yDZo4Njtp7ufaVXVvvDzJEUz1zSDoEq_8BxW5HhM_aFonm32LU9LFm9BUd3yMdUu82MvBr63yTmgBqlVOtMsZoQLSEHjAimQh8DxrYp.Of6NkPiHl5Xqjrrr3QOifQdV2McPCwfas_Ari0Sx.IzsHmvdHs.ENUREV5hvz5K1RlBaE.UEacApSLzPnfl6asIyzZGxhCVRYdXBJ6z3.5W_.Si48AAw9tu3lHMtdo9XtcteOBVcOA.iHQtJn7BsBIK.0jwjM1Iy5muudK0gwBg5woH4TTj5EeyjwrfhWV3Q7z4NILIOyfPFasQxnWRyZMjquLde0Mp7RHSLMhPXRtrcB15nsy6b7eTlCkrrKY1M2FWGO21zn7odlq4cnW6sJ5bR8LnFqDMERIHBWEgRCuc2NRVW0o.hq1EosxXT2js2QRLWEbSxiTK4lmmDAG8zbJIf38zMmrnDcp1FFZMKYx84zlM1HS.SG6v7eR_Mq1mzpozqjJyrvbhjatVPelerRmaBQE3IV0osGwtL_njz5gN9AvZxw_l6C4y5r_XcSiHESJqN7hYr8NN.Ja2Xv6dJ5d9_vtz0Si.p89PaMcEqwa6ycROjhZcDjq1BhZrH4txkdRNuJB5S4ANtB3tD3ahKJg3ZOdozEktG_mkNNlJuFoVHJciDQ9zkE_vDm6yT9FsPOjtNC3Y4ROHOSOPLs3L6uisgb75wLtSTs5MPSSqQ8ZQfCuDie5a_36aruXVFfh04M6UR14IX3XmszbCtKqZp_2sQlbpNIfCa9pRCPmq.xQ.mDzoOVRjOizBHZXSvocIwSNGVA_GyzJJX9eo8G8IRg78n9aWOtTJdYAnQ0wRURq0D0pNxB_9eD4FkgbRSMOF0A7DBqB_qNF.UOzbXzJXsTDKM.wYmpdhehsZ30_oFhIaQWm6aIRmgH3jge_QPweQqG3BE1dh4NbiZ4190JM4AeE30C~A",
        "Content-Length": "1570",
        "Sec-Ch-Ua": "",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
        "Sec-Ch-Ua-Platform": '""',
        "Accept": "*/*",
        "Origin": "https://login.yahoo.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://login.yahoo.com/?.intl=in",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    data = {
        "browser-fp-data": "%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A240%2C%22timezone%22%3A%22America%2FNew_York%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Linux%20x86_64%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A2%2C%22hash%22%3A%22324a1d8f89b36d258428e873cbc3f19d%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)%7EANGLE%20(Intel%2C%20Vulkan%201.3.246%20(Intel(R)%20HD%20Graphics%20620%20(KBL%20GT2)%20(0x00005916))%7E%20Intel%20open-source%20Mesa%20driver)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A1%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A10%2C%22hash%22%3A%22931325cddfccb148efe006d7581957aa%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221920%22%2C%22h%22%3A%221080%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%221045%22%2C%22h%22%3A%221920%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1694564356982%2C%22render%22%3A1694564357554%7D%7D",
        "crumb": "LbucvbTt8nx",
        "acrumb": "fmrlGgeV",
        "sessionIndex": "Qw--",
        "displayName": "",
        "deviceCapability": "%7B%22pa%22%3A%7B%22status%22%3Afalse%7D%7D",
        "username": email,
        "passwd": "",
        "signin": "Next",
        "persistent": "y"
    }

    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    if 'messages.INVALID_USERNAME'  in response.text:
        return('invalid')
        
    elif 'messages.ERROR_NOTFOUND' in response.text:
        return('Yahoo data')
    elif 'rate limited' in response.text:
        return('Limited rate')
    else:
        print(response.text)
        return('valid')
    
# yahoo('sawdyk123@yahoo.com')