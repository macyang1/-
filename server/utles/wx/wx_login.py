from utles.wx import settings
import requests

def login(code):
    response=requests.get(settings.code2Session.format(settings.AppId,settings.AppSecret,code))
    data=response.json()
    if data.get("openid"):
        return data
    else:
        return False


