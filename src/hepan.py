from lxml import etree
import requests
import json

bbsHeader = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Cache-Control": "max-age=0",
             "Connection": "keep-alive",
             "Host": "bbs.uestc.edu.cn",
             "Referer": "https://bbs.uestc.edu.cn",
             "Sec-Fetch-Dest": "document",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-User": "?1",
             "Upgrade-Insecure-Requests": "1",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}


def GetRequest():
    with open("./config.json", 'r', encoding="utf-8") as f:
        bbsHeader["Cookie"] = json.load(f)["HePan_Cookies"]
        
    url = 'https://bbs.uestc.edu.cn/forum.php?mod=forumdisplay&fid=61'
    try:
        r = requests.get(url, headers=bbsHeader)
    except requests.exceptions.ProxyError:
        print('河畔: 代理出错')
        exit(0)

    return r


def getRankStr():
    r = GetRequest()
    html = etree.HTML(r.text)
    result = []
    for i in range(10):
        title = html.xpath(
            f'/html/body/div[6]/div[4]/div/div/div[4]/div[2]/form/table/tbody[{9 + i}]' + '/tr/th/a[3]/text()')
        result.append(title[0])

    return result
    # print(result)
