# -*- coding:utf-8 -*-
__author__ = 'weikai'
import sys
reload(sys)
sys.setdefaultencoding('utf8')
global null, false, true
null = None
false = False
true = True

car1=  {
    "licenseType": "02",
    "colorCode": "09",
    "netWeight": 1995,
    "carKindCodeNew": "K2",
    "loanVehicleFlag": "0",
    "carChecker": "",
    "countryNature": "1",
    "lastYearDamage": "",
    "carLicenceDate": "",
    "enrollDate": "2016-05-13",
    "seatCountOld": "7",
    "carCheckerReason": "000",
    "useNatureCode": "85",
    "powerScale": "",
    "fuelType": "0",
    "purchasePriceType": "02",
    "licenseNo": "苏A6G1H1",
    "modelName": "路虎牌CJL6460L2AW5",
    "exhaustScale": "1.999",
    "expecLossRatio": "",
    "specialCarFlag": "",
    "chgOwnerFlag": "0",
    "carKindCode": "KA",
    "useYears": "1",
    "industryModelCode": "BLHEFAUB0001",
    "exhaustScaleOld": 1.999,
    "transferDate": "",
    "engineNo": "015306185318",
    "deviceQuantityCount": null,
    "useNatureCodeNew": "N85",
    "certificateNo": "",
    "certificateType": "",
    "devicePurchasePriceCount": null,
    "deviceActualValueCount": null,
    "runAreaName": "中华人民共和国境内(不含港澳台)",
    "modelAlias": "发现神行2.0T AT S版",
    "modelNamePlat": "路虎牌CJL6460L2AW5",
    "fixedLine": "",
    "vinNo": "L2CCA2BG7GG311741",
    "tradeName": "奇瑞捷豹路虎汽车有限公司",
    "noticeType": "LH-CJL6460L2AW5",
    "haulage": "0",
    "brand": "奇瑞捷豹路虎",
    "sortCode": "",
    "noDamageYears": "0",
    "certificateDate": "",
    "carRegiste": "0",
    "runAreaCode": "11",
    "seatCount": "7",
    "purchasePriceOld": "309000",
    "netWeightOld": "1995.000",
    "isPrintModelAlias": "0",
    "carName": "路虎牌CJL6460L2AW5",
    "tonCount": "0.0000",
    "vehicleDamaged": "1",
    #"vehicleCode": "LHBAHD0001",
    "bookingTime": "",
    "ecdemicVehicleFlag": "0",
    "runMiles": "45000",
    "noLicenseFlag": "0",
    "actualValueOld": "288606.00",
    "carKindCatalogCode": "K",
    "isNewCarFlag": "0",
    "abnormalCarFlag": "0",
    "modelCodePlat": "LHBAHD0001",
    "purchasePrice": "309000",
    "licenseColorCode": "01",
    "actualValue": "288606",
    "depreciation": "0.60",
    "tonCountOld": "0.0000",
    "carCheckTime": "",
    "vehicleStyle": "K32",
    "deptName": "合资",
    "modelCode": "LHBAHD0001",
    "carCheckStatus": "1"
  }

car2= {
    "carName": "路虎CJL6460L2AW5 S版",
    "noLicenseFlag": "0",
    "licenseNo": "苏A6G1H1",
    "licenseType": "02",
    "licenseColorCode": "01",
    "engineNo": "015306185318",
    "vinNo": "L2CCA2BG7GG311741",
    "carKindCatalogCode": "K",
    "carKindCodeNew": "K2",
    "carKindCode": "KB",
    "useNatureCodeNew": "N85",
    "useNatureCode": "85",
    "vehicleStyle": "K32",
    "enrollDate": "2016-05-13",
    "useYears": "0",
    "seatCount": "7",
    "exhaustScale": "1.999",
    "modelName": "路虎CJL6460L2AW5",
    "modelCode": "LHBAHD0001",
    "purchasePrice": "309000.00",
    "actualValue": "288606",
    "tonCount": "0.0000",
    "netWeight": "1995.000",
    "powerScale": "",
    "runAreaCode": "11",
    "runAreaName": "中华人民共和国境内(不含港澳台)",
    "fixedLine": "",
    "colorCode": "09",
    "haulage": "0",
    "fuelType": "0",
    "runMiles": "45000",
    "specialCarFlag": "",
    "chgOwnerFlag": "0",
    "transferDate": "",
    "loanVehicleFlag": "0",
    "ecdemicVehicleFlag": "0",
    "depreciation": "0.60",
    "noDamageYears": "0",
    "sortCode": "",
    "carCheckStatus": "1",
    "carChecker": "",
    "carCheckTime": "",
    "carCheckerReason": "000",
    "isNewCarFlag": "0",
    "bookingTime": "",
    "certificateType": "",
    "certificateNo": "",
    "certificateDate": "",
    "carRegiste": "0",
    "modelAlias": "发现神行2.0T AT S版",
    "isPrintModelAlias": "0",
    "tonCountOld": "0.0000",
    "exhaustScaleOld": "1.999",
    "seatCountOld": "5",
    "purchasePriceOld": "309000.00",
    "carLicenceDate": "",
    "lastYearDamage": "",
    "vehicleDamaged": "1",
    "expecLossRatio": "",
    "industryModelCode": "BLHEFAUB0001",
    "abnormalCarFlag": "0",
    "noticeType": "CJL6460L2AW5",
    "tradeName": "奇瑞捷豹路虎汽车有限公司",
    "modelCodePlat": "LHBAHD0001",
    "modelNamePlat": "路虎CJL6460L2AW5",
    "countryNature": "1",
    "purchasePriceType": "01",
    "actualValueOld": 288606,
    "netWeightOld": "1910.000",
    "brand": "奇瑞捷豹路虎",
    "deptName": "合资",
    "deviceQuantityCount": null,
    "devicePurchasePriceCount": null,
    "deviceActualValueCount": null
  }
for key in car1:
    if car1[key]!=car2[key]:
        print key,car1[key],car2[key]
