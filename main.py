from src.myjson import json_read, json_write
import src.hepan as hp
import src.weibang as wb
import src.report as rp
import time
import os
import json

keywords = []


def keywordCheck(data: list, func):
    tmp = data
    data = func.getRankStr()

    if func == hp:
        json_write("./data/hepanRank.json", data)

    if func == wb:
        json_write("./data/weibangRank.json", data)

    if tmp != data:  # 检查是否更新
        # print(data)
        # print(tmp)
        if func == hp:
            print("\n河畔更新：", data[0])
        if func == wb:
            print("\n微帮更新：", data[0])

        for i in keywords:
            if i in data[0]:
                if func == hp:
                    rp.FangTang("河畔更新：" + data[0])
                if func == wb:
                    rp.FangTang("微帮更新：" + data[0])
                # rp.xiaoWei(data[0])
                
    return data

if __name__ == "__main__":
    
    hepanFlag = True
    weibangFlag = True
    
    with open("./config.json", 'r', encoding="utf-8") as f:
        tmp = json.load(f)
        keywords = tmp["keywords"]
        if tmp["HePan_Cookies"] == '':
            hepanFlag = False
            print("未输入河畔 Cookie, 不启动河畔检索")
        if tmp["WeiBang_Cookies"] == '':
            weibangFlag = False
            print("未输入微帮 Cookie, 不启动微帮检索")
        
    
    if weibangFlag:
        print("检查微帮 json")
        if os.path.exists("./data/weibangRank.json"):
            print("读取微帮 json")
            rankWeibang = json_read("./data/weibangRank.json")
        else:
            print("微帮 json 不存在")
            rankWeibang = []


    if hepanFlag:
        print("检查河畔 json")
        if os.path.exists("./data/hepanRank.json"):
            print("读取河畔 json")
            rankHepan = json_read("./data/hepanRank.json")
        else:
            print("河畔 json 不存在")
            rankHepan = []

    print("\n爬虫启动！\n")
    
    while (True):
        try:
            if hepanFlag:
                rankHepan = keywordCheck(rankHepan, hp)
            if weibangFlag:
                rankWeibang = keywordCheck(rankWeibang, wb)
            
            time.sleep(60)

        except KeyboardInterrupt:
            print("用户中断 KeyboardInterrupt，保存中...")

            if hepanFlag:
                print("Saving: hepanRank.json")
                json_write("./data/hepanRank.json", rankHepan)

            if weibangFlag:
                print("Saving: weibangRank.json")
                json_write("./data/weibangRank.json", rankWeibang)

            print("Over....")
            exit(0)
            
        except Exception as error:
            print("error: " + error)

            if hepanFlag:
                print("Saving: hepanRank.json")
                json_write("hepanRank.json", rankHepan)

            if weibangFlag:
                print("Saving: weibangRank.json")
                json_write("weibangRank.json", rankWeibang)

            print("Over....")
            exit(0)
