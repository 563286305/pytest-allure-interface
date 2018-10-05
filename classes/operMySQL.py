# -*- coding: utf-8 -*-
'''
Created on 2018.09.18
@author: wuyou
'''
import pymysql
from sshtunnel import SSHTunnelForwarder

class operMySQL:
    def __init__(self, ssh_host, ssh_user, ssh_password, host, port, user, password, db):
        self.ssh_host = ssh_host
        self.ssh_port = 22
        self.ssh_user = ssh_user
        self.ssh_password = ssh_password
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password

        if ssh_host!='':
            self._server = self.serverrun()
            self._server.start()
            self._conn = self.conmysql_ssh()
        else:
            self._conn = self.conmysql()
            self._server = False
        if (self._conn):
            self._cursor = self._conn.cursor()

    # 链接跳板机
    def serverrun(self):
        server = False
        try:
            server = SSHTunnelForwarder(
                ssh_address_or_host=(self.ssh_host, 22),
                ssh_username=self.ssh_user,
                ssh_password=self.ssh_password,
                remote_bind_address=(self.host, int(self.port)))
        except Exception:
            server = False
        return server

    # 通过跳板机连接
    def conmysql_ssh(self):
        conn = False
        try:
            conn = pymysql.connect(
                user=self.user,
                passwd=self.password,
                host='127.0.0.1',
                db=self.db,
                charset='utf8',
                port=self._server.local_bind_port)
        except Exception:
            conn = False
        return conn

    #直接链接
    def conmysql(self):
        conn = False
        try:
            conn = pymysql.connect(host=self.host,
							   port=int(self.port),
							   user=self.user,
							   passwd=self.password,
		                       db=self.db,
							   charset='utf8')
        except Exception:
            conn = False
        return conn

    #sql查询，得到一个竖列，取值，返回list
    def run_sql_single_with_value_return_collist(self,sqlcommand, value):
        print("SQLCommand:  "+str(sqlcommand))
        print("SQLValue:    "+str(value))

        res = False
        resultlist= []
        value = [value]
        if (self._conn):
            try:
                self._cursor.execute(str(sqlcommand),value)
                res = self._cursor.fetchall()
            except Exception as error:
                print(error)
                res = False
        if res:
            for i in range(len(res)):
                resultlist.append(str(res[i][0]))
        else:
            result = "empty"
            resultlist.append(result)
        return(resultlist)

    #sql查询，得到一个横行，取值，返回list
    def run_sql_single_with_value_return_rawlist(self,sqlcommand, value):
        print("SQLCommand:  "+str(sqlcommand))
        print("SQLValue:    "+str(value))
        res = False
        resultlist= []
        value = [value]
        if (self._conn):
            try:
                self._cursor.execute(str(sqlcommand),value)
                res = self._cursor.fetchall()
            except Exception as error:
                print(error)
                res = False

        if res:
            for i in range(len(res[0])):
                resultlist.append(str(res[0][i]))
        else:
            result = "empty"
            resultlist.append(result)

        return resultlist



    # 查询
    def fetch_all(self, sql):
        res = False
        if (self._conn):
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception:
                res = False
        return res
    #
    # # 增加
    # def insert(self, sql):
    #     flag = False
    #     if (self._conn):
    #         try:
    #             self._cursor.execute(sql)
    #             self._conn.commit()
    #             flag = True
    #         except Exception:
    #             flag = False
    #     return flag
    #
    # # 更新
    # def update(self, sql):
    #     flag = False
    #     if (self._conn):
    #         try:
    #             self._cursor.execute(sql)
    #             self._conn.commit()
    #             flag = True
    #         except Exception:
    #             flag = False
    #     return flag
    #
    # # 删除
    # def update(self, sql):
    #     flag = False
    #     if (self._conn):
    #         try:
    #             self._cursor.execute(sql)
    #             self._conn.commit()
    #             flag = True
    #         except Exception:
    #             flag = False
    #     return flag

    # 关闭
    def close(self):
        if (self._conn):
            self._conn.close()
        if self._server:
            self._server.stop()
            self._server.close()

if __name__=="__main__":
    run = operMySQL()
    command = "select * from t_account_bill_trade_blotter  where ABTB_SEQ=%s"
    value = '100018091902523703696808'
    a = run.run_sql_single_with_value_return_rawlist(command,value)
    print(a)