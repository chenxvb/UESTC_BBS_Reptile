import requests
import json

headers = {
    "Host": "www.chengdianxz.cn",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; IN2020 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5307 MMWEBSDK/20221206 MMWEBID/9683 MicroMessenger/8.0.32.2300(0x28002037) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "http://www.chengdianxz.cn/info/list?module=ershou",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "If-None-Match": "W/\"0d166f562aff70e9ac9b44ed2874e2bc\"",
    "Connection": "close"
}

def getRankStr():
    with open("./config.json", 'r', encoding="utf-8") as f:
        headers["Cookie"] = json.load(f)["WeiBang_Cookies"]
        
    try:
        r = requests.get("http://www.chengdianxz.cn/info/list?module=ershou&cid=0&page=1", headers=headers)
    except requests.exceptions.ProxyError:
        print('微帮: 代理出错')
        exit(0)

    rsp = json.loads(r.text)

    results = []
    for i in range(rsp["count"]):
        results.append(rsp["data"][i]["desc"])
    return results