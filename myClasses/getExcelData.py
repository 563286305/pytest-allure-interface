# -*- coding: utf-8 -*-
'''
Created on 2018.09.18
@author: wuyou
'''
import classes.operExcel
import os
excel = classes.operExcel.operExcel()
casepath = os.path.dirname(__file__)
basepath = os.path.dirname(casepath)
config_excel = os.path.join(basepath + "\config\\","Configuration.xlsx")
casefile_excel = os.path.join(basepath + "\\testCase\\","testCase.xlsx")
config_sheet = 'testEnv'
class getExcelData:
    def __init__(self,casesheetname):
        self.sheetname = casesheetname
        # end = excel.get_excel_row_count(config_excel, config_sheet)
        # configdict = excel.get_excel_name_value_dict(config_excel, config_sheet,'B','C','2',end)
        self.configdict = self.getConfig()
        self.core_sql_addr = self.configdict['core_sql_addr']
        self.core_sql_usr = self.configdict['core_sql_usr']
        self.core_sql_psw = self.configdict['core_sql_psw']
        self.core_port = self.configdict['core_port']
        self.core_db = self.configdict['core_db']
        self.search_url = self.configdict['search_url']
        self.deal_url = self.configdict['deal_url']
        self.encryption_url = self.configdict['encryption_url']
        self.asyn_url = self.configdict['asyn_url']
        self.request_col = self.configdict['request_col']
        self.sql_col = self.configdict['sql_col']
        self.expect_col = self.configdict['expect_col']
        self.asyn_col = self.configdict['asyn_col']
        self.search_pos_start = self.configdict['search_pos_start']
        self.search_pos_end = self.configdict['search_pos_end']
        self.search_neg_start = self.configdict['search_neg_start']
        self.search_neg_end = self.configdict['search_neg_end']
        self.search_pos_sheet = self.configdict['search_pos_sheet']
        self.search_neg_sheet = self.configdict['search_neg_sheet']
        self.deal_pos_sheet = self.configdict['deal_pos_sheet']
        self.deal_pos_start = self.configdict['deal_pos_start']
        self.deal_pos_end = self.configdict['deal_pos_end']
        self.ids_col = self.configdict['ids_col']
        self.deal_expect_col = self.configdict['deal_expect_col']
        self.deal_sync_sheet = self.configdict['deal_sync_sheet']
        self.deal_sync_start = self.configdict['deal_sync_start']
        self.deal_sync_end = self.configdict['deal_sync_end']
        self.sync_deal_except_col = self.configdict['sync_deal_except_col']


    def getConfig(self):
        end = excel.get_excel_row_count(config_excel, config_sheet)
        configdict = excel.get_excel_name_value_dict(config_excel, config_sheet,'B','C','2',end)

        return(configdict)

    def getTestData(self):
        request_col = self.request_col
        sql_col = self.sql_col

        if self.sheetname == '交易异步':
            sheet = self.deal_pos_sheet
            asyn_col = self.asyn_col
            deal_expect_col = self.deal_expect_col
            start = self.deal_pos_start
            end = self.deal_pos_end
            request_data = excel.colname_read_excel_return_list(casefile_excel,sheet, request_col, start, end)
            asynData = excel.colname_read_excel_return_list(casefile_excel, sheet,asyn_col, start, end)
            sqlCommands = excel.colname_read_excel_return_list(casefile_excel,sheet,sql_col, start, end)
            expectDict = excel.colname_read_excel_return_list(casefile_excel, sheet,deal_expect_col, start, end)
            testdataList = list(zip(request_data,asynData,sqlCommands,expectDict))

        elif self.sheetname == '交易非异步':
            sheet = self.deal_sync_sheet
            sync_deal_except_col = self.sync_deal_except_col
            start = self.deal_sync_start
            end = self.deal_sync_end
            request_data = excel.colname_read_excel_return_list(casefile_excel,sheet, request_col, start, end)
            sqlCommands = excel.colname_read_excel_return_list(casefile_excel,sheet,sql_col, start, end)
            expectDict = excel.colname_read_excel_return_list(casefile_excel, sheet,sync_deal_except_col, start, end)
            testdataList = list(zip(request_data,sqlCommands,expectDict))


        elif self.sheetname == '查询正测':
            sheet = self.search_pos_sheet
            start = self.search_pos_start
            end = self.search_pos_end
            request_data = excel.colname_read_excel_return_list(casefile_excel,sheet, request_col, start,end)
            sqlCommands = excel.colname_read_excel_return_list(casefile_excel,sheet,sql_col,start,end)
            testdataList = list(zip(request_data,sqlCommands))

        elif self.sheetname == '查询反测':
            sheet = self.search_neg_sheet
            expect_col = self.expect_col
            start = self.search_neg_start
            end = self.search_neg_end
            request_data = excel.colname_read_excel_return_list(casefile_excel,sheet,request_col,start,end)
            expect_data = excel.colname_read_excel_return_list(casefile_excel,sheet,expect_col,start,end)
            testdataList = list(zip(request_data,expect_data))

        else:
            testdataList = []

        return(testdataList)

    def getIds(self):
        ids_col = self.ids_col
        if self.sheetname == '交易异步':
            start = self.deal_pos_start
            end = self.deal_pos_end
            sheet = self.deal_pos_sheet
        elif self.sheetname == '交易非异步':
            start = self.deal_sync_start
            end = self.deal_sync_end
            sheet = self.deal_sync_sheet
        elif self.sheetname == '查询正测':
            sheet = self.search_pos_sheet
            start = self.search_pos_start
            end = self.search_pos_end
        elif self.sheetname == '查询反测':
            sheet = self.search_neg_sheet
            start = self.search_neg_start
            end = self.search_neg_end
        else:
            sheet = start = end = 'None'

        ids = excel.colname_read_excel_return_list(casefile_excel, sheet,ids_col ,start,end)

        return ids

if __name__=='__main__':
    get = getExcelData('交易异步')
    a= get.getTestData()
    print(a)