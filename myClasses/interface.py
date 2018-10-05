# -*- coding: utf-8 -*-
'''
Created on 2018.08.27
@author: wuyou
'''
import requests
import json
import classes.webRequest
import myClasses.getExcelData
webRequest = classes.webRequest.webRequest()
getExcelData = myClasses.getExcelData.getExcelData('testEnv')

class interface():
	def __init__(self):
		self.configdict = getExcelData.getConfig()
		self.encryption_url = self.configdict['encryption_url']
		self.asyn_url = self.configdict['asyn_url']
		self.search_url = self.configdict['search_url']

	def asyn(self,encryptionData,headers):
		print("异步明文消息：	"+str(encryptionData))
		resultEncrypt = webRequest.getResult(self.encryption_url,encryptionData,headers,'POST')
		assert resultEncrypt!=''
		if resultEncrypt!='':
			resultEncrypt = json.loads(resultEncrypt)
			asynData = "1|-|12|-|90|-|N01|-|"+resultEncrypt['sign'] + "|-|"+"\n"+resultEncrypt['cipher']+"|-|"
			print("异步推送消息：	")
			print(asynData)
			resultAsyn = webRequest.getResult(self.asyn_url,asynData,headers,'POST')
			assert resultAsyn!=''
			print("异步推送结果：	")
			print(resultAsyn)

		print("异步信息加密结果：")
		print(resultEncrypt)


	# #异步通知
	# def asyn(self,encryption_url,asyn_url,encryptionData):
	# 	headers = {'Content-Type': 'application/json;charset=UTF-8'}
	# 	print("异步明文消息：	"+str(encryptionData))
    #
	# 	try:
	# 		result1 = requests.post(encryption_url,data=encryptionData,headers=headers)
	# 		result1 = json.loads(result1.content)
	# 		print("异步信息加密结果：")
	# 		print(result1)
	# 		asynData = "1|-|12|-|90|-|N01|-|"+result1['sign'] + "|-|"+"\n"+result1['cipher']+"|-|"
	# 		print("异步推送消息：	")
	# 		print(asynData)
	# 		#asynData = '1|-|12|-|90|-|N01|-|VO6FesgZ|-|'+'\n'+'Els9X/WjIEFBVOhoe9wnB2Nod7v7ABZzdNo9AhUsIADn+zNlBtxUDevqjmA1cqUjPHzlQQrYZhI6THfYRou9JfhNj5wCnjRThyc2pL3PP3RUO3ciNNfW8AefJtC3+f5LJnwlKGwE5+A=|-|'
	# 		result2 = requests.post(asyn_url,data=asynData)
	# 		print("异步推送结果：	")
	# 		print(result2.text)
    #
	# 	except Exception as error:
	# 		result = 'false'
	# 		print(result)

	#查询交易接口:
	def search_deal(self,url,data):
		try:
			headers = {'Content-Type': 'application/json;charset=UTF-8'}
			result = requests.post(url,data=json.dumps(data),headers=headers )
			print("Request接口返回结果：")
			print(result.text)
			return str(result.text)
		except Exception as error:
			print(url + " : Check rate failed! ")
			print("data:	"+ str(data))
			result = 'false'
			return result

	def searchInf(self,data):
		headers = {'Content-Type': 'application/json;charset=UTF-8'}
		resultSearch = webRequest.getResult(self.search_url,data,headers,'POST')
		assert resultSearch!=''
		return resultSearch

if __name__ == '__main__':
	#url = 'http://47.94.44.86:8075/ams/query/intf/server.intf'
	url = 'http://47.94.44.86:8065/ams/trans/intf/server.intf'
	#SecCode用基金的fundcode
	#data = {'SecCode':'110025'}
	data = {
       "head": {
    "transType": "T",
    "transCode": "BP08",
    "transDate": "20180910",
    "transTime": "132020",
    "transSerialNo": "100018091002500000403088",
    "channelNo": "XD_YRTX",
    "sysCode": "1000"
  },
  "body": {

"custNo":"201706201834352546146358244",
"depositNo":"468726852404379649",
"subAcct":"468726852907696128",
        "tradeType":"A2",
    "rechargeAmtType": "1",
    "transAmt": "1.00",
    "currency": "CNY",
    "note": "111"
  }
}



#{"data":{"desc":"216-平台充值调用银行充值接口返回处理中，推送账务流水成功【系统处理中，请稍后查询处理结果】"},"msg":"处理中","sts":"100000","success":false}

#20180904
#200218090301612345123418

	inf = interface()
	# result = inf.search(url,data)
	# print(str(result))
	encryption_url='http://47.94.44.86:8796/ams/notify/intf/gen!server.intf'
	asyn_url='http://47.94.44.86:8796/ams/notify/intf/bank!server.intf'
	#encryptionData = '100018091102577393717889|-|A2|-||-||-||-|20180911|-|135500|-|2|-|0000|-|OK|-||-|90|-||-||-||-||-|'
	encryptionData = "100018091102573262411418|-|A2|-||-||-||-|20180911|-|135500|-|2|-|0000|-|OK|-||-|90|-||-||-||-||-|\n"
	headers = {'Content-Type': 'application/json;charset=UTF-8'}
	result = inf.asyn1(encryption_url,asyn_url,encryptionData,headers)
	#result = inf.asyn(encryption_url,asyn_url,encryptionData)