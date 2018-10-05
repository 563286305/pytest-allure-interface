# -*- coding: utf-8 -*-
'''
Created on 2018.09.18
@author: wuyou
'''
import requests
import time
class webRequest():
    def getResult(self,url,datas,header,type):
        retry = 0
        jsontemp = ""
        result = ""

        while (retry < 3):
            try:
                if type == 'POST':
                    result = requests.post(url, data=str(datas).encode("utf-8"), headers=header)
                elif type == 'GET':
                    result = requests.get(url, params=str(datas).encode("utf-8"), headers=header)
                elif type == 'PUT':
                    result = requests.put(url, data=str(datas).encode("utf-8"), headers=header)
                break
            except Exception as error:
                time.sleep(2)
                retry += 1
                print("Send Request Error: " + str(error))

        if result!='':
            jsontemp = result.text
        print("Request 返回结果：    "+str(jsontemp))
        return jsontemp


if __name__=="__main__":
    run = webRequest()
    url = 'http://47.94.44.86:8065/ams/trans/intf/server.intf'
    datas = {
    "head":{
        "transSerialNo":"100318092105508850460222",
        "transDate":"20180921",
        "transType":"T",
        "transTime":"132124",
        "channelNo":"LC_JFJR",
        "sysCode":"1003",
        "transCode":"BP20"
    },
    "body":{
        "custNo":"201802071541341201808241107",
     "depositNo":"484756397542473729",
        "subAcct":"484756397638942722",
        "userName":"自动化演示",
        "tradeType":"TZ02",
        "ledger":"1",
        "balanceType":"1",
        "transAmt":"10.00",
        "currency":"CNY",
        "oppoDepositNo":"492699632418160641",
        "oppoSubAcct":"492699632858562560",
        "oppoCustNo":"201706201834352546146358244",
        "oppoUserName":"qqq",
        "oppoLedger":"2",
        "oppoBalanceType":"1",
        "applicant":"",
        "asynBackUrl":"https://www.baidu.com/",
        "note":"I AM beiz备注"
    }

}
    header = {'Content-Type': 'application/json;charset=UTF-8'}
    run.getResult(url,datas,header,'POST')
