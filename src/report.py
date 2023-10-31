from urllib.parse import urlencode
import requests
import json

def FangTang(data:str):
    with open("./config.json", 'r', encoding="utf-8") as f:
        FangTang_APIkey = json.load(f)["FangTang_APIkey"]
        
    try:
        r = requests.get(f"https://sctapi.ftqq.com/{FangTang_APIkey}.send?" + urlencode({"title":data}))
    except requests.exceptions.ProxyError:
        print('FangTang 上报: 代理出错')
        exit(0)

