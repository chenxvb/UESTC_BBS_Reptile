from urllib.parse import urlencode
import requests
import json

def FangTang(data:str):
    with open("./config.json", 'r', encoding="utf-8") as f:
        FangTang_APIkey = json.load(f)["FangTang_APIkey"]
        
    if FangTang_APIkey == "":
        return
    try:
        r = requests.get(f"https://sctapi.ftqq.com/{FangTang_APIkey}.send?" + urlencode({"title":data}))
    except:
        print('FangTang : 上传出错')
        exit(0)

def tgSend(data:str):
    with open("./config.json", 'r', encoding="utf-8") as f:
        tmp = json.load(f)
        payload = {
                'text': data,
                "cookie": tmp["telegram_cookie"],
                'chatid' : tmp["telegram_chatid"]
                }
        url = tmp["telegram_url"]

        
    if url == "":
        return
    
    try:
        response = requests.post(url, json=payload)
    except:
        print('tg : 上传出错')
        exit(0)

def sendMsg(data:str):
    tgSend(data)
    FangTang(data)
