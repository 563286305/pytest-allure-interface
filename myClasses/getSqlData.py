# -*- coding: utf-8 -*-
'''
Created on 2018.09.18
@author: wuyou
'''
import classes.operMySQL
import myClasses.getExcelData
operMySQL = classes.operMySQL
getExcelData = myClasses.getExcelData.getExcelData('testEnv')
class getSqlData():
    def __init__(self):
        configdict = getExcelData.getConfig()
        self.core_sql_addr = configdict['core_sql_addr']
        self.core_sql_usr = configdict['core_sql_usr']
        self.core_sql_psw = configdict['core_sql_psw']
        self.core_port = configdict['core_port']
        self.core_db = configdict['core_db']
        self.search_url = configdict['search_url']

        self.child2_sql_addr = configdict['child2_sql_addr']
        self.child2_sql_usr = configdict['child2_sql_usr']
        self.child2_sql_psw = configdict['child2_sql_psw']

        self.child1_sql_addr = configdict['child1_sql_addr']
        self.child1_sql_usr = configdict['child1_sql_usr']
        self.child1_sql_psw = configdict['child1_sql_psw']
        self.child1_ams_trans_db = configdict['child1_ams_trans_db']
        self.ssh_host = configdict['ssh_host']
        self.ssh_usr = configdict['ssh_usr']
        self.ssh_psw = configdict['ssh_psw']
        self.child_port = configdict['child_port']

        self.con_ams_core_test = operMySQL.operMySQL('', '', '',self.core_sql_addr,self.core_port,self.core_sql_usr,self.core_sql_psw,'ams_core_test')

        self.ams_trans_db = operMySQL.operMySQL(self.ssh_host, \
                                                self.ssh_usr, \
                                                self.ssh_psw, \
                                                self.child1_sql_addr, \
                                                self.child_port, \
                                                self.child1_sql_usr, \
                                                self.child1_sql_psw, \
                                                     'ams_trans_db')
        self.ams_notify_non_realtime = operMySQL.operMySQL(self.ssh_host, \
                                                self.ssh_usr, \
                                                self.ssh_psw, \
                                                self.child2_sql_addr, \
                                                self.child_port, \
                                                self.child2_sql_usr, \
                                                self.child2_sql_psw, \
                                                     'ams_notify_non_realtime')
        self.ams_core_test_Tables = ['t_account_bill_trade_blotter',\
                                't_account_bill_registry_online',\
                                't_account_bill_detail',\
                                't_account_bookkeeping',\
                                't_account_bill_registry_offline',\
                                't_deposit_account_info',\
                                't_deposit_account_bank',\
                                't_customer_order']
        self.ams_trans_db_Tables = ['t_ams_trans_processs_log','t_ams_trans_inamt_asyn_notice',\
                                    't_ams_trans_adjust_log']
        self.ams_notify_non_realtime_Tables=['t_ams_notify_msg_transfer_log','t_ams_notify_msg_transfer_log_history']

    def getTableColumnsDict(self):
        sqlcommand_ams_trans_db ='select column_name from information_schema.COLUMNS where TABLE_NAME = %s and TABLE_SCHEMA="ams_trans_db"'
        sqlcommand_ams_notify_non_realtime = 'select column_name from information_schema.COLUMNS where TABLE_NAME = %s and TABLE_SCHEMA="ams_notify_non_realtime"'
        sqlcommand_ams_core_test ='select column_name from information_schema.COLUMNS where TABLE_NAME = %s'
        columnNameDict={}

        for key in self.ams_core_test_Tables:
            columnName = self.con_ams_core_test.run_sql_single_with_value_return_collist(sqlcommand_ams_core_test,key)
            print(columnName)
            columnNameDict[key]=columnName

        for key in self.ams_trans_db_Tables:
            columnName = self.ams_trans_db.run_sql_single_with_value_return_collist(sqlcommand_ams_trans_db,key)
            columnNameDict[key]=columnName

        for key in self.ams_notify_non_realtime_Tables:
            columnName = self.ams_notify_non_realtime.run_sql_single_with_value_return_collist(sqlcommand_ams_notify_non_realtime,key)
            columnNameDict[key]=columnName

        return columnNameDict

    def getSearchTableValues(self,request_dict,sql_dict):
        valueDict = {}
        for key in sql_dict:
            if key in self.ams_core_test_Tables:
                command = sql_dict[key]
                valueDict[key]=self.con_ams_core_test.fetch_all(command)
                print(str(key)+" 查询结果：   " + str(valueDict[key]))
                assert valueDict[key]
            if key == 'response':
                valueDict[key]=sql_dict[key]
        return valueDict

    def getDealTableValues(self,requestData,sql_dict,aysnStr):

        if requestData!='None' and requestData!='':
            valueTransSerialNo = requestData['head']['transSerialNo']
            if 'subAcct' in requestData['body']:
                valueSubAcct = requestData['body']['subAcct']
            elif "outSubAcct" in requestData['body']:
                valueSubAcct = requestData['body']['outSubAcct']
            else:
                valueSubAcct = None

        else:
            if aysnStr!='None' and aysnStr!='':
                aysnNo = aysnStr.split('|-|')[2]
                aysnDepoNO = aysnStr.split('|-|')[4]

        columnNameDict = self.getTableColumnsDict()

        checkResultDict = {}

        if 't_ams_trans_inamt_asyn_notice' in sql_dict:
            command = sql_dict['t_ams_trans_inamt_asyn_notice']
            valuelist = self.ams_trans_db.run_sql_single_with_value_return_rawlist(command, aysnNo)
            asynNoticeDict = dict(zip(columnNameDict['t_ams_trans_inamt_asyn_notice'],valuelist))
            #更新valueTransSerialNo值
            valueTransSerialNo = asynNoticeDict['TRANS_NO']
            checkResultDict['t_ams_trans_inamt_asyn_notice']=asynNoticeDict

        for key in sql_dict:
            command = sql_dict[key]

            #子库一表
            if key == 't_ams_trans_processs_log':
                valuelist = self.ams_trans_db.run_sql_single_with_value_return_rawlist(command, valueTransSerialNo)
                assert 'empty' not in valuelist
                checkResultDict['t_ams_trans_processs_log']=dict(zip(columnNameDict['t_ams_trans_processs_log'],valuelist))
            elif key == 't_ams_trans_adjust_log':
                valuelist = self.ams_trans_db.run_sql_single_with_value_return_rawlist(command, valueTransSerialNo)
                checkResultDict['t_ams_trans_adjust_log']=dict(zip(columnNameDict['t_ams_trans_adjust_log'],valuelist))

            #核心库表
            elif key == 't_account_bill_trade_blotter':
                valuelist = self.con_ams_core_test.run_sql_single_with_value_return_rawlist(command, valueTransSerialNo)
                checkResultDict['t_account_bill_trade_blotter']=dict(zip(columnNameDict['t_account_bill_trade_blotter'],valuelist))

            elif key == 't_account_bill_registry_online':
                valuelist = self.con_ams_core_test.run_sql_single_with_value_return_rawlist(command,valueTransSerialNo)
                checkResultDict['t_account_bill_registry_online']=dict(zip(columnNameDict['t_account_bill_registry_online'],valuelist))

            elif key=='t_account_bill_detail':
                valuelist = self.con_ams_core_test.run_sql_single_with_value_return_rawlist(command,valueTransSerialNo)
                checkResultDict['t_account_bill_detail']=dict(zip(columnNameDict['t_account_bill_detail'],valuelist))

            elif key=='t_account_bookkeeping':
                if requestData!='None':
                    valuelist = self.con_ams_core_test.run_sql_single_with_value_return_rawlist(command, valueSubAcct)
                else:
                    if aysnStr!='None':
                        valuelist = self.con_ams_core_test.run_sql_single_with_value_return_rawlist(command, aysnDepoNO)
                checkResultDict['t_account_bookkeeping']=dict(zip(columnNameDict['t_account_bookkeeping'],valuelist))

            #字库二表
            elif key == 't_ams_notify_msg_transfer_log':
                valuelist = self.ams_notify_non_realtime.run_sql_single_with_value_return_rawlist(command, valueTransSerialNo)
                checkResultDict['t_ams_notify_msg_transfer_log']=dict(zip(columnNameDict['t_ams_notify_msg_transfer_log'],valuelist))

            elif key == 't_ams_notify_msg_transfer_log_history':
                valuelist = self.ams_notify_non_realtime.run_sql_single_with_value_return_rawlist(command, valueTransSerialNo)
                checkResultDict['t_ams_notify_msg_transfer_log_history']=dict(zip(columnNameDict['t_ams_notify_msg_transfer_log_history'],valuelist))

            else:
                pass

        print("数据库检查结果为：    " )
        print(checkResultDict)
        return(checkResultDict)

    def connClose(self):
        self.con_ams_core_test.close()
        self.ams_trans_db.close()
        self.ams_notify_non_realtime.close()

if __name__=="__main__":
    # run = getSqlData()
    # run.get_table_allcolumn()
    for i in range(0):
        print('aaaaaa')