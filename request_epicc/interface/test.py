# -*- coding:utf-8 -*-
__author__ = 'wk'
import jsonpath
import json
json1 ={"message":"{\"check_code\":\"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\",\"uuid\":\"360ffba5-d3ea-4b0a-b458-cf9d1ceffae9\"}","status":"success"}
print(json1['message'])
jsn2=json1['message']

jsonstr=eval(jsn2)

result = jsonpath.jsonpath(jsonstr,'$.check_code')
#print result[0]


import urllib
import sys

data = u'channelNo=2&sessionId=7523bed2-4cc2-4249-8e4f-0f2e828c6501&proSelected=32000000&citySelected=32010000&carOwnerIdentifytype=&areaCodeLast=32000000&cityCodeLast=32010000&mobile=13888888888&email=22%40QQ.COM&identifytype=01&identifynumber=320125198610093122&birthday=1986%2F10%2F09&sex=2&startdate=2017-01-22&starthour=0&enddate=2018-01-21&endhour=24&isRenewal=0&licenseno=%E8%8B%8FAB3Q98&nonlocalflag=01&licenseflag=1&engineno=KL1392&vinno=LNBSCCAH3EF031577&frameno=LNBSCCAH3EF031577&newcarflag=0&isOutRenewal=0&lastHas050200=0&lastHas050210=0&lastHas050500=0&lastHas050291=&enrolldate=2014-12-26&transfervehicleflag=0&insuredname=%E6%9D%A8%E5%B0%8F%E9%A6%99&fullAmountName=&beforeProposalNo=&startDateCI=2017-01-22&starthourCI=0&endDateCI=2018-01-21&endhourCI=24&taxpayeridentno=&taxpayername=%E6%9D%A8%E5%B0%8F%E9%A6%99&taxtype=&certificatedate=&transferdate=2017%2F01%2F20&runAreaCodeName=&assignDriver=2&haveLoan=2&LoanName=&weiFaName=&seatCount=5&seatflag=1&carDrivers=&ccaFlag=&ccaID=&ccaEntryId=&travelMilesvalue=&isbuytax='

s_utf=urllib.quote('1900\\')
print s_utf




print str('w1.01s').split('.')[0]

import datetime

print(datetime.datetime)
