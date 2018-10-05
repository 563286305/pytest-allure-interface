# -*- coding: utf-8 -*-
'''
Created on 2018.08.28
@author: wuyou
'''
import pytest
import allure
import json
# import myClasses.getExcelData
# from myClasses.testCase import testCase
# from myClasses.parseRequestData import parseRequestData
import classes.webRequest
import myClasses.interface
import myClasses.parserJson
import myClasses.getSqlData
import myClasses.resultCheck

webRequest = classes.webRequest.webRequest()
getExcelData = myClasses.getExcelData
parserJson = myClasses.parserJson.parserJson()
resultCheck = myClasses.resultCheck.resultCheck()
interface = myClasses.interface.interface()

class Test_Run():

    @pytest.fixture
    def init_param(self):
        self.configdict = getExcelData.getExcelData('testEnv').getConfig()
        self.encryption_url = self.configdict['encryption_url']
        self.asyn_url = self.configdict['asyn_url']
        self.search_url = self.configdict['search_url']
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}
        self.deal_url = self.configdict['deal_url']
        self.getSqlData = myClasses.getSqlData.getSqlData()
        yield self.getSqlData
        print("Close SQL Connection.")
        self.getSqlData.connClose()

    @allure.feature('查询类接口')
    @allure.severity("critical")
    @allure.story("反测")
    @pytest.mark.usefixtures("init_param")
    @pytest.mark.parametrize("request_data,expect_data",getExcelData.getExcelData('查询反测').getTestData(),ids =getExcelData.getExcelData('查询反测').getIds() )
    def test_search_neg(self,request_data,expect_data):
        assert request_data !='None' and expect_data!='None'
        with pytest.allure.step("测试步骤1：解析request信息"):
            request_data = json.loads(request_data)
            #request_data = pa_re.updateData(request_data)
            request_data = parserJson.updateRequestData(request_data)
            allure.attach("Request数据",str(request_data))

        with pytest.allure.step("测试步骤2：解析expect信息"):
            expect_data = json.loads(expect_data)
            allure.attach("Expect数据",str(expect_data))

        with pytest.allure.step("测试步骤3：发送Request数据 "):
            #发送request数据
            resultdict = webRequest.getResult(self.search_url,request_data,self.headers,'POST')
            resultdict= json.loads(resultdict)

        with pytest.allure.step("测试步骤4：查询结果"):
            #比对结果
            resultCheck.compareSearchdict(expect_data,resultdict)
    #
    # @allure.feature('查询类接口')
    # @allure.severity("critical")
    # @allure.story("正测")
    # @pytest.mark.usefixtures("init_param")
    # @pytest.mark.parametrize("request_data,sql_data",getExcelData.getExcelData('查询正测').getTestData(),ids =getExcelData.getExcelData('查询正测').getIds() )
    #
    # def test_search_pos(self,request_data,sql_data):
    #
    #     assert request_data !='None' and sql_data!='None'
    #     with pytest.allure.step("测试步骤1：解析request信息"):
    #         request_data = json.loads(request_data)
    #         request_data = parserJson.updateRequestData(request_data)
    #         allure.attach("Request数据",str(request_data))
    #         #根据excel中的sql语句，数据库库获取数据，并解析成json格式
    #
    #     with pytest.allure.step("测试步骤2：发送Request数据 "):
    #         #发送request数据
    #         resultdict = webRequest.getResult(self.search_url,request_data,self.headers,'POST')
    #         resultdict= json.loads(resultdict)
    #         allure.attach("Request返回结果",str(resultdict))
    #
    #     with pytest.allure.step("测试步骤3：解析数据库信息"):
    #         sql_data = json.loads(sql_data)
    #         checksqldict = self.getSqlData.getSearchTableValues(request_data,sql_data)
    #         expectdict = parserJson.parserSearchSqlData(request_data,checksqldict)
    #         allure.attach("数据库解析出的Json数据",str(expectdict))
    #
    #     with pytest.allure.step("测试步骤4：查询结果"):
    #         #比对结果
    #         resultCheck.compareSearchdict(expectdict,resultdict)

    # @allure.feature("交易类接口")
    # @allure.severity("critical")
    # @allure.story("异步")
    # @pytest.mark.usefixtures("init_param")
    # @pytest.mark.parametrize("request_data,asyn_data,sql_dict,expectDict",getExcelData.getExcelData('交易异步').getTestData(),ids =getExcelData.getExcelData('交易异步').getIds() )
    # def test_deal_asyn(self,request_data,asyn_data,sql_dict,expectDict):
    #     with pytest.allure.step("测试步骤1：解析request信息"):
    #         if request_data!='None':
    #             request_data = json.loads(request_data)
    #             request_data = parserJson.updateRequestData(request_data)
    #             allure.attach("Request数据",str(request_data))
    #
    #             with pytest.allure.step("测试步骤2：发送Request数据 "):
    #                 # 发送request数据
    #                 resultdict = webRequest.getResult(self.deal_url,request_data,self.headers,'POST')
    #                 resultdict= json.loads(resultdict)
    #                 assert resultdict['sts']=='100000'
    #                 allure.attach("Request返回结果",str(resultdict))
    #         else:
    #             allure.attach("Request数据",str(request_data))
    #
    #     with pytest.allure.step("测试步骤3：发送异步数据 "):
    #         #发送request数据
    #         asyn_data = parserJson.updateAsynData(asyn_data,request_data)
    #         resultdict = interface.asyn(asyn_data,self.headers)
    #         allure.attach("异步返回结果",str(resultdict))
    #
    #     with pytest.allure.step("测试步骤4：获取数据库查询结果 "):
    #         #获取数据库查询结果
    #         sql_dict = json.loads(sql_dict)
    #         checkdict = self.getSqlData.getDealTableValues(request_data,sql_dict,asyn_data)
    #         allure.attach("数据库查询结果",str(checkdict))
    #
    #     with pytest.allure.step("测试步骤5：比对查询结果 "):
    #         #获取数据库查询结果
    #         expectDict = json.loads(expectDict)
    #         resultCheck.compareDealDict(expectDict,checkdict)
    #
    # @allure.feature("交易类接口")
    # @allure.severity("critical")
    # @allure.story("非异步")
    # @pytest.mark.usefixtures("init_param")
    # @pytest.mark.parametrize("request_data,sql_dict,expectDict",getExcelData.getExcelData('交易非异步').getTestData(),ids =getExcelData.getExcelData('交易非异步').getIds() )
    # def test_deal_sync(self,request_data,sql_dict,expectDict):
    #
    #     with pytest.allure.step("测试步骤1：解析request信息"):
    #         request_data = json.loads(request_data)
    #         request_data = parserJson.updateRequestData(request_data)
    #         allure.attach("Request数据",str(request_data))
    #
    #     with pytest.allure.step("测试步骤2：发送Request数据 "):
    #         # 发送request数据
    #         if isinstance(request_data,list):
    #             for info in request_data:
    #                 resultdict = webRequest.getResult(self.deal_url,info,self.headers,'POST')
    #         else:
    #             resultdict = webRequest.getResult(self.deal_url,request_data,self.headers,'POST')
    #         resultdict= json.loads(resultdict)
    #         assert resultdict['sts']=='000000'
    #         allure.attach("Request返回结果",str(resultdict))
    #
    #     with pytest.allure.step("测试步骤3： 获取数据库查询结果 "):
    #         #获取数据库查询结果
    #         sql_dict = json.loads(sql_dict)
    #         if isinstance(request_data,list):
    #             checkdict = self.getSqlData.getDealTableValues(request_data[0],sql_dict,'')
    #         else:
    #             checkdict = self.getSqlData.getDealTableValues(request_data,sql_dict,'')
    #         allure.attach("数据库查询结果",str(checkdict))
    #
    #     with pytest.allure.step("测试步骤4： 比对查询结果 "):
    #         #比对查询结果
    #         expectDict = json.loads(expectDict)
    #         resultCheck.compareDealDict(expectDict,checkdict)


if __name__ == '__main__':
    pytest.main()
