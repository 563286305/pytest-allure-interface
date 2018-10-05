# -*- coding: utf-8 -*-
'''
Created on 2018.08.28
@author: wuyou
'''
import decimal
class resultCheck():

    def compareDealDict(self,exceptdict,checkdict):
        for key in exceptdict:
            assert key in checkdict
            print("**********检查表： "+str(key))
            info1 = exceptdict[key]
            info2 = checkdict[key]
            for core in info1:
                if core in info2:
                    print('检查字段：    '+str(core))
                    print('Expect key:  '+str(info1[core]))
                    print('Check key:  '+str(info2[core]))
                    assert info1[core]==info2[core]

    def compareSearchdict(self,exceptdict,checkdict):
        if 'data' in exceptdict:
            if isinstance(exceptdict['data'],list):
                assert len(exceptdict['data']) == len(checkdict['data'])
                num = len(exceptdict['data'])
                for i in range(num):
                    self.compareSearchdictOne(exceptdict['data'][i],checkdict['data'][i])
            else:
                self.compareSearchdictOne(exceptdict['data'],checkdict['data'])
        else:
            self.compareSearchdictOne(exceptdict,checkdict)

    def compareSearchdictOne(self,exceptdict,checkdict):
        #compare data
        except_datadict = exceptdict
        check_datadict = checkdict
        otherlist = ['bankCardList','transList','resultList','returnList','subAcctList','list','subAccts']

        for key in except_datadict:
            if key in check_datadict and key not in otherlist:
                if (not check_datadict[key]) or str(check_datadict[key])=='':
                    print("key empty: "+str(key))
                    print("SQL parser value:   "+str(except_datadict[key]))
                    print("Interface check value:  "+str(check_datadict[key]))
                    assert not check_datadict[key]
                else:
                    print("key: "+str(key))
                    if isinstance(except_datadict[key],decimal.Decimal) or isinstance(except_datadict[key],float):
                        except_datadict[key] = float(except_datadict[key])
                        check_datadict[key] = float(check_datadict[key])
                    print("SQL parser value:   "+str(except_datadict[key]))
                    print("Interface check value:  "+str(check_datadict[key]))
                    assert str(except_datadict[key])==str(check_datadict[key])

        for listname in otherlist:
            if listname in check_datadict and listname in except_datadict:
                exceptlist = except_datadict[listname]
                checklist = check_datadict[listname]
                assert len(exceptlist)==len(checklist)
                for i in range(len(checklist)):
                    checkinfo = checklist[i]
                    exceptinfo = exceptlist[i]
                    for key in checkinfo:
                        if key in exceptinfo:
                            if (not checkinfo[key]) or str(exceptinfo[key])=='':
                                print("key empty: "+str(key))
                                print("SQL value:   "+str(exceptinfo[key]))
                                print("Inf value:  "+str(checkinfo[key]))
                                assert not exceptinfo[key]
                            else:
                                if isinstance(exceptinfo[key],decimal.Decimal) or isinstance(exceptinfo[key],float):
                                    exceptinfo[key] = float(exceptinfo[key])
                                    checkinfo[key] = float(checkinfo[key])

                                print("key: "+str(key))
                                print("SQL value:   "+str(exceptinfo[key]))
                                print("Inf value:  "+str(checkinfo[key]))
                                assert str(exceptinfo[key])==str(checkinfo[key])