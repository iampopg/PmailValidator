import requests

url = "https://login.yahoo.com/?display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0&prompt=login&chllngnm=fail"
def yahoo(email):
    headers = {
        "Host": "login.yahoo.com",
        "Cookie": "A1=d=AQABBMAV_2QCEPOdGqmVO5g-E61EBoY0NDEFEgEBAQFnAGUIZY14zSMA_eMAAA&S=AQAAAgvpZlTBjqpMHkc6Q1Qv8us; A3=d=AQABBMAV_2QCEPOdGqmVO5g-E61EBoY0NDEFEgEBAQFnAGUIZY14zSMA_eMAAA&S=AQAAAgvpZlTBjqpMHkc6Q1Qv8us; A1S=d=AQABBMAV_2QCEPOdGqmVO5g-E61EBoY0NDEFEgEBAQFnAGUIZY14zSMA_eMAAA&S=AQAAAgvpZlTBjqpMHkc6Q1Qv8us&j=WORLD; AS=v=1&s=fmrlGgeV&d=A64ff1a58|TO6OQoD.2QqW7QunFNIJYubaCZ4D2iojp1AA34b4L5lHg0ZZGWx_y6GqPXbyiaY6Ay9NN6FpHnJi3SbI7XR.NTTpuLLxY2ErrxFC66kLE5PIoFw5T7_9xhGHqQvKPQGEptyn62TzN2f9d.USKJAxgu2lslsfyrBVWaZNM0iq9fi.zgfkChMiRfWgTPq12SH.0.b5VaYz8YTNtXzyh__BPLqMXjbihsDmkhFHZRNdcRhnFLNGvC7PIlUcBNdjBeGYobQRbD5pBqgPu_gVCS_2Z7duBgVqw7YkT8molmM9p2MvAhwAdOThLN2Tbaj1v_weBQhX4LTLYkIdbcZSRYvauRAyGLBZdtDx9jLmHbdRL6cX31_LC93N2oS2XObCd.RhQh_HHkV7RvQnv2KDjUztdFjNzQ6Wacay0jiFPv6CzvqmJ6.kBKNXOUxUiVnTJs4dLU3PONPWcOHMwNQNhz5pcnnAzjFeOxdriSVLCSDqNHD6lSXZW_zx6.ULe50lvG.Elckfke5C8J63loa2Kga1lHmkbVztMhKRG9FSANVQtMRh42N24fUusxpJZaYRL5jEl5kjWq0QP1PDAIWFki7fL09ZRoW7torJ6FR5Ze5bYjE9qf5Ho7sEtBVhzUPsf1LOH7s2EggQogY3jmyVgcpfZUhdWp.AJZKj.wUQMm3itsNwplruuydudTd1JG2yhJuHmkvnH3fDCLIu1CDJMRyuXGScuWsdxqwIW0QocOdaOM3xlQuRsn6Ps_ZSGJRc.L90oSBcacVtLfW_tMmr3cf.IjHYqJQL80afixPxspxtWtbkBcjiY0AmJTT0d4dHZCFL484H_Vd8Boc84wE1I6R.k8Va1auAt_PewltbYOr79WnLTrdkX2ndSavz3n9NIX3TsSNsk9uc4.EIM1_DrfSQx_meIHQxD3tnmM9qeyXKrFjPdYbAizp4Fw3EbXfmN9mcTmXwn11aklDx1T0TKe5egN9CVdT01.TGlJ2a~A|B6500686f|.F9tVnf.2SrYr8F8PDu2FOEdOrUkYp_QJoJG5vC5439yLlcGYGgnjb_Ju.KwjLy_nciw6.3Zvbx9Hxuxx81MpFi.d3h6_HdD3JLF_eez4et_3BDmWNpwIBptcLTQ2J8QwMY3JyQbyYZEHmuCiHIcndO6ZPjnaBKUulvAJaMOH2mWTyCedYBOA3tggLPC1alHIbCnLEDC42cnvMzwmTS7F5qb25gPNMDIW_.xt_XSNl.BnK0cqus0UY0wEYYK7qUfXernPV7Kdmrbni.UdtFCU2fvS5eqiYgkuVxQA22kLTFmxUNlNxxpaa_ywzQ9GbJ.FLEjk2eDHNgy9ABsArfHctJ7ENCVTYrz0.ThQ_yYslM3JxluTtyiX2xHtt9hwTzdbPgJ78Y5gFYImvF3829o4sK.DzPtmBUlmzveiZeR5zmWq_punGNIDwOwjsXklercDc4E18_7PY5DIMv40ewr6vODjIfnGYYlpIT3IaMfJ0raxxAMahvPSPyRiYTEMS2eib0Ss2EcR5COKcEFP6Ly1e3JaAi83MX8PJWOyxMnoFtKWyYHqQOK8ywLuD95H4XpjEjURwyk7N4XUaoH87CNbpECROVJgEsJIIKvbVvo56M5BLBsTHYI3yZmqMQxbhGOS0rPAbpDyZ1LwRCAxm5YJ0seAscYZK8qGlwEKIK3R0u0TnMuPNLcrIgd1AsMS1rZ8eKMrRGNjS5xrvaNOTlvRd__DbBEX919u8YulCh8TSzZJzawAMbLa0zOt9Jslq6lWB12Ruv.H9Sdv7vqBNbOXoLg2CgIQxYJ2q8KS0hntvFlBv3ezSDrdh3HFd3TW_zIGolZ3z4PnV166GasSu9OjYA0B2g9h63pd19ryLtfokrN1QXVzz9uO6OZIKSYsVt5k730PBgMKy4YiNRWJUVG5UQgY7w-~A",
        "Content-Length": "1569",
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
        "Referer": "https://login.yahoo.com/?display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0&prompt=login&chllngnm=fail",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
    }

    payload = {
        "browser-fp-data": '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":240,"timezone":"America/New_York","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Linux x86_64","doNotTrack":"unknown","plugins":{"count":2,"hash":"324a1d8f89b36d258428e873cbc3f19d"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Vulkan 1.3.246 (Intel(R) HD Graphics 620 (KBL GT2) (0x00005916)), Intel open-source Mesa driver)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":10,"hash":"931325cddfccb148efe006d7581957aa"},"audio":"124.04347527516074","resolution":{"w":"1920","h":"1080"},"availableResolution":{"w":"1045","h":"1920"},"ts":{"serve":1694439133957,"render":1694439134358}}',
        "crumb": "LbucvbTt8nx",
        "acrumb": "fmrlGgeV",
        "sessionIndex": "Qg--",
        "displayName": "",
        "deviceCapability": '{"pa":{"status":false}}',
        "username": email,
        "passwd": "",
        "signin": "Next",
        "persistent": "y",
    }

    response = requests.post(url, headers=headers, data=payload)

    # print(response.text)
    if 'messages.INVALID_USERNAME' not in response.text:
        return('valid')
        
    else:
        return('invalid')