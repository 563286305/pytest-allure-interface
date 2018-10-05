# -*- coding: utf-8 -*-
'''
Created on 2018.08.27
@author: wuyou
'''
import json
import classes.dataCreate
dataCreate = classes.dataCreate.DataCreate()
class parserJson():
    #request请求数据更新
    def __init__(self):
        self.Codedict = {"CX01":"013","CX02":"014","CX03":"015","CX04":"016","CX05":"017",\
                       "CX06":"018","CX07":"019","CX18":"020","CX19":"021","CX20":"038",\
                       "CX21":"036","CX22":"039","CX23":"042","CX24":"051","CX25":"052",\
                       "CX26":"053","CX27":"063","CX28":"061","CX29":"062","BP08":"025","BP02":"023","BP04":"026",\
                       "BP05":"027","BP06":"028","BP09":"035","BP10":"040","BP11":"041",\
                       "BP12":"043","BP13":"044","BP14":"045","BP15":"046","BP17":"049",\
                       "BP18":"050","BP19":"054","BP20":"055","BP21":"056","BP22":"057","BP23":"058"}
    #更新无依赖的单条request数据
    def updateoneData(self,data):

        sysCode = data['head']['sysCode']
        transCode = data['head']['transCode']
        transSerialNo = data['head']['transSerialNo']

        datestr = dataCreate.getnowdate()
        date = datestr[2:8]

        if transCode in self.Codedict:
            code = self.Codedict[transCode]
        else:
            code = '013'

        ramdomNum = dataCreate.gen_random_numstr(11)

        #更新transDate
        if data['head']['transDate']=='generate':
            data['head']['transDate']= datestr

        if "bankNo" in data['body']:
            if data['body']['bankNo'] == 'generate':
                data['body']['bankNo'] = dataCreate.get_bank_card_no('招商银行')

        #transSerialNo为generate的时候，更新transSerialNo
        if transSerialNo=='generate':
            transSerialNo_new = sysCode+date+code+ramdomNum
            data['head']['transSerialNo'] = transSerialNo_new

        #transSerialNo为testdate的时候，将流水号的时间设置为固定值，以保证和transDate不同
        elif transSerialNo=='testdate':
            data['head']['transSerialNo'] = sysCode + "20180101" +code+ramdomNum
        #若transSerialNo直接给定了字符串，将其中的日期替换为当天日期
        elif transSerialNo!='' and transSerialNo!='generate' and transSerialNo!='testdate':
            data['head']['transSerialNo'] = transSerialNo[0:4]+datestr[2:8] + transSerialNo[10:24]

        return data

    #更新
    def updateRequestData(self,requestdata):
        requestdata = self.updateoneData(requestdata)
        #打印基本信息
        print("Request发送数据： "+'\n'+str(requestdata))
        print("流水号： " + str(requestdata['head']['transSerialNo']))
        print("transDate: "+str(requestdata['head']['transDate']))
        if 'custNo' in requestdata['body']:
            print("custNo:  "+ str(requestdata['body']['custNo']))
        if 'depositNo' in requestdata['body']:
            print("depositNo:  "+ str(requestdata['body']['depositNo']))
        if 'depositAcct' in requestdata['body']:
            print("depositAcct:  "+ str(requestdata['body']['depositAcct']))
        if 'subAcct' in requestdata['body']:
            print("subAcct:  "+ str(requestdata['body']['subAcct']))
        data = requestdata
        if requestdata['head']['transCode'] == "BP21":
            data = []
            predata = {"head":{"transSerialNo":"generate","transDate":"generate","transType":"T","transTime":"132124","channelNo":"LC_JFJR","sysCode":"1003","transCode":"BP20"},"body":{"custNo":"201802071541341201808241107","depositNo":"484756397542473729","subAcct":"484756397638942722","userName":"自动化演示","tradeType":"TZ02","ledger":"1","balanceType":"1","transAmt":"1.00","currency":"CNY","oppoDepositNo":"492699632418160641","oppoSubAcct":"492699632858562560","oppoCustNo":"201706201834352546146358244","oppoUserName":"qqq","oppoLedger":"2","oppoBalanceType":"1","applicant":"","asynBackUrl":"https://www.baidu.com/","note":"I AM beiz备注"}}
            predata = self.updateoneData(predata)
            if 'transNo' in requestdata['body']:
                requestdata['body']['transNo'] = predata['head']['transSerialNo']
            data.append(predata)
            data.append(requestdata)
        print('总发送数据为：  '+str(data))
        return data

    #异步信息更新
    def updateAsynData(self,encryptionData,requestData):
        #encryptionData = '100018091002500000403088|-|A2|-||-||-||-|20180910|-|135500|-|2|-|0000|-|OK|-||-|90|-||-||-||-||-|'
        if requestData!='None':
            asynList = encryptionData.split('-')
            transSerialNo = requestData['head']['transSerialNo']+"|"
            transDate = "|"+requestData['head']['transDate']+"|"
            asynList[0] = transSerialNo
            asynList[5] = transDate
            encryptionData_new = '-'.join(asynList)
        #encryptionData_new = transSerialNo+asynList[1:5]+transDate+asynList[6:17]
            print('异步信息加密消息: ' + '\n'+encryptionData_new)
            return(encryptionData_new)
        else:
            return(encryptionData)

    #########解析数据库表信息成和Request发送返回值相同结构的Json串
    def parserSearchSqlData(self,request_dict,sqlDict):
        expectdict={}
        for key in sqlDict:
            if key == "t_deposit_account_info":
                expectdict = self.parser_t_deposit_account_info(request_dict,expectdict,sqlDict[key])
            elif key == "t_deposit_account_bank":
                expectdict = self.parser_t_deposit_account_bank(expectdict,sqlDict[key])
            elif key == "t_account_bookkeeping":
                expectdict = self.parser_t_account_bookkeeping(request_dict,expectdict,sqlDict[key])
            elif key == "t_account_bill_detail":
                expectdict = self.parser_t_account_bill_detail(expectdict,sqlDict[key])
            elif key == "t_account_bill_registry_offline":
                expectdict = self.parser_t_account_bill_registry_offline(expectdict,sqlDict[key])
            elif key == "t_account_bill_trade_blotter":
                expectdict = self.parser_t_account_bill_trade_blotter(request_dict,expectdict,sqlDict[key])
            elif key == "t_customer_order":
                expectdict = self.parser_t_customer_order(request_dict,expectdict,sqlDict[key])
            elif key == "response":
                expectdict = sqlDict['response']

        return(expectdict)

    #解析 t_deposit_account_info
    def parser_t_deposit_account_info(self,request_dict,parserdict,data):
        print('正在解析 t_deposit_account_info 表 。。。 ')
        if request_dict['head']['transCode']=='CX21':
            if 'data' not in parserdict:
                parserdict['data']=[]
            #redata = {}
        else:
            if 'data' not in parserdict:
                parserdict['data']={}
            #redata = parserdict['data']

        if data!=None:
            for info in data:
                tmpdict = {}
                tmpdict['acctStatus']='1'
                tmpdict['acctType']=info[2]
                tmpdict['custNo']=info[4]
                tmpdict['custType']=info[5]
                tmpdict['roleType']=info[6]
                tmpdict['custName']=info[7]
                tmpdict['certType']=info[8]
                tmpdict['certNo']=info[9]
                tmpdict['phoneNo']=info[10]
                tmpdict['depositAcct']=info[12]

                tmpdict['legalName']=info[16]
                tmpdict['legalCertType']=info[17]
                tmpdict['legalCertNo']=info[18]
                tmpdict['busiLiceNo']=info[19]
                tmpdict['taxNo']=info[20]

                tmpdict['isEntrust1']=info[23]
                tmpdict['entrustTerm1']=info[24]
                tmpdict['entrustLimit1']=info[25]
                tmpdict['isEntrust2']=info[26]
                tmpdict['entrustTerm2']=info[27]
                tmpdict['entrustLimit2']=str(info[28])
                tmpdict['isEntrust3']=str(info[29])
                tmpdict['entrustTerm3']=str(info[30])
                tmpdict['entrustLimit3']=str(info[31])

                tmpdict['openAcctTime']=info[36].strftime("%Y-%m-%d %H:%M:%S")
                tmpdict['signTime']=info[37].strftime("%Y-%m-%d %H:%M:%S")

                tmpdict['acctSts']=info[42]
                tmpdict['signStatus']=info[43]
                tmpdict['stockFlg']=info[44]

                tmpdict['changePwdStatus']=info[51]
                #tmpdict['openChannel']=info[52]
                tmpdict['openChannel']=info[15]

                if request_dict['head']['transCode']=='CX21':
                    parserdict['data'].append(tmpdict)
                else:
                    parserdict['data'].update(tmpdict)
        print(parserdict)
        return parserdict

    #解析 t_deposit_account_bank
    def parser_t_deposit_account_bank(self,parserdict,data):
        print('正在解析 t_deposit_account_bank 表 。。。 ')
        if 'data' not in parserdict:
            parserdict['data'] = {}
            parserdict['data']['bankCardList'] = []
        else:
            if 'bankCardList' not in parserdict['data']:
                parserdict['data']['bankCardList'] = []
        if data !=None:
            for cardinfo in data:
                carddict = {}
                carddict['cardSts'] =cardinfo[4]
                carddict['cardPhoneNo'] =cardinfo[5]
                carddict['encryptBankCardNo'] =cardinfo[6]
                carddict['regBank'] =cardinfo[7]
                carddict['createTime'] =cardinfo[11].strftime("%Y%m%d%H%M%S")
                carddict['transCompleteTime'] =cardinfo[23].strftime("%Y%m%d%H%M%S")


                if cardinfo[8] == '0':
                    carddict['cardType'] ='B10'
                elif cardinfo[8] == '1':
                    carddict['cardType'] ='B11'
                elif cardinfo[8] == '2':
                    carddict['cardType'] ='B12'
                else:
                    carddict['cardType'] = None

                carddict['bankCardNo'] = cardinfo[19]
                carddict['isTransfer'] =cardinfo[21]

                parserdict['data']['bankCardList'].append(carddict)

        print(parserdict)
        return parserdict


    def parser_t_account_bookkeeping(self,request_dict,parserdict,data):
        print('正在解析 t_account_bookkeeping 表 。。。 ')
        if request_dict['head']['transCode']=='CX21':
            if 'data' not in parserdict:
                parserdict['data']=[]
            else:
                for datainfo in parserdict['data']:
                    if  'subAccts' not in datainfo:
                        datainfo['subAccts'] = []

            tmplist=[]
            for info in data:
                tmpdict = {}
                tmpdict['subAcct'] = info[8]
                tmpdict['fundType'] = info[9]
                tmpdict['channelNo'] = info[10]
                tmpdict['totalBalance'] = info[11]
                tmpdict['balance'] = info[12]
                tmpdict['freazeBalance'] = info[13]
                tmpdict['traBalance'] = info[14]
                tmpdict['depo_no'] = info[4]
                tmplist.append(tmpdict)
                # depo_no = info[4]

            for datainfo in parserdict['data']:
                for tmpdict in tmplist:
                    if tmpdict['depo_no'] == datainfo['depositAcct']:
                        datainfo['subAccts'].append(tmpdict)
        else:
            if 'data' not in parserdict:
                parserdict['data'] = {}
                parserdict['data']['subAcctList'] = []
            else:
                if 'bankCardList' not in parserdict['data']:
                    parserdict['data']['subAcctList'] = []
            redata=parserdict['data']

            # depositAcct

            if request_dict['head']['transCode'] == 'CX25':
                for info in data:
                    tmpdict = {}
                    tmpdict['subAcct'] = info[8]
                    tmpdict['channelNo'] = info[10]
                    tmpdict['totalBalance'] = info[11]
                    tmpdict['balance'] = info[12]
                    tmpdict['freazeBalance'] = info[13]
                    tmpdict['traBalance'] = info[14]
                    parserdict['data']['subAcctList'].append(tmpdict)
            elif request_dict['head']['transCode'] == 'CX24' or request_dict['head']['transCode'] == 'CX02':
                for info in data:
                    redata['balance']=info[1]
                    redata['freazeBalance']=info[2]
                    redata['totalBalance']=info[0]
                    redata['traBalance']=info[3]
            elif request_dict['head']['transCode'] == 'CX26'or request_dict['head']['transCode'] == 'CX29':
                for info in data:
                    redata['unpaidAmount'] = info[11]
                    redata['custNo']  = info[2]
                    redata['depositAcct']  = info[4]
                    redata['subAcct']  = info[8]
                    redata['channelNo']  = info[10]
                    redata['custName']  = info[18]
            else:
                for info in data:
                    redata['totalBalance'] = info[11]
                    redata['balance'] = info[12]
                    redata['freazeBalance'] = info[13]
                    redata['subAcct'] = info[8]

        print(parserdict)
        return   parserdict

    def parser_t_account_bill_detail(self,parserdict,data):
        print('正在解析 t_account_bill_detail 表 。。。 ')
        if 'data' not in parserdict:
            parserdict['data'] = {}
            parserdict['data']['transList'] = []
        else:
            if 'transList' not in parserdict['data']:
                parserdict['data']['transList'] = []

        if data !=None:
            for info in data:
                tmpdict = {}
                tmpdict['transTxn'] = info[5]
                tmpdict['outAcct'] = info[8]
                tmpdict['outSubAcct'] = info[7]
                tmpdict['inAcct'] = info[10]
                tmpdict['inSubAcct'] = info[9]
                tmpdict['transTime'] = info[6].strftime("%Y%m%d%H%M%S")
                tmpdict['transAmt'] = info[15]
                tmpdict['tradeType'] = info[3]
                tmpdict['note'] = info[25]
                parserdict['data']['transList'].append(tmpdict)
        print(parserdict)
        return   parserdict

    def parser_t_account_bill_registry_offline(self,parserdict,data):
        print('正在解析 t_account_bill_registry_offline 表 。。。 ')
        if 'data' not in parserdict:
            parserdict['data'] = {}
            parserdict['data']['resultList'] = []
        else:
            if 'resultList' not in parserdict['data']:
                parserdict['data']['resultList'] = []

        if data !=None:
            for info in data:
                tmpdict = {}
                tmpdict['transTime'] = info[2].strftime("%Y%m%d")+'000000'
                tmpdict['amt'] = info[12]
                tmpdict['bankCard'] = info[22]
                tmpdict['tradeType'] = info[7]
                tmpdict['channel'] = info[25]
                tmpdict['channelSeq'] = info[26]
                tmpdict['localTransSts'] = info[16]
                parserdict['data']['resultList'].append(tmpdict)
        print(parserdict)
        return   parserdict

    def parser_t_account_bill_trade_blotter(self,request_dict,parserdict,data):
        print('正在解析 t_account_bill_trade_blotter 表 。。。 ')
        if 'data' not in parserdict:
            parserdict['data'] = {}
            parserdict['data']['list'] = []
        else:
            if 'list' not in parserdict['data']:
                parserdict['data']['list'] = []

        redata = parserdict['data']

        if request_dict['head']['transCode'] == 'CX22':
            for info in data:
                tmpdict = {}
                tmpdict['transTxn']=info[0]
                parserdict['data']['list'].append(tmpdict)
        else:
            for info in data:
                redata['transTime']=info[5].strftime("%Y%m%d%H%M%S")
                redata['transResult']=info[6]
                redata['transRem']=info[29]
                redata['custNo']=json.loads(info[8])['custNo']
                redata['transAmt']=float(json.loads(info[8])['transAmt'])
                redata['bankNo']=info[13]
                if 'transCode' in request_dict['head'] and "tradeType" in request_dict['body']:
                    transCode = request_dict['head']['transCode']
                    tradeType = request_dict['body']['tradeType']

                    if transCode=="CX23" and (tradeType=='00' or tradeType=='DJ' or tradeType=='JD'):
                        redata['depositAcct']=info[23]
                        redata['subAcct']=info[24]
                    elif transCode=="CX23" and (tradeType=='01'):
                        redata['depositAcct']=info[26]
                        redata['subAcct']=info[27]
                else:
                    redata['depositAcct']=info[23]
                    redata['subAcct']=info[24]
        print(parserdict)
        return parserdict

    def parser_t_customer_order(self,request_dict,parserdict,data):
        print('正在解析 t_customer_order 表 。。。 ')
        if request_dict['head']['transCode'] == 'CX28':
            listname = 'resultList'
        else:
            listname = 'returnList'

        if 'data' not in parserdict:
            parserdict['data'] = {}
            parserdict['data'][listname] = []
        else:
            if 'returnList' not in parserdict['data']:
                parserdict['data'][listname] = []

        for info in data:
            tmpdict = {}
            if request_dict['head']['transCode'] == 'CX28':
                tmpdict['failMsg']=info[7]
            else:
                if info[6]!= '2':
                    tmpdict['failMsg']=''
                else:
                    tmpdict['failMsg']=info[7]

            tmpdict['transSerialNo']=info[0]
            tmpdict['transResult']=info[6]
            tmpdict['bankNo']=info[25]
            tmpdict['transAmt']=str(info[27])
            parserdict['data'][listname].append(tmpdict)

        print(parserdict)
        return parserdict

