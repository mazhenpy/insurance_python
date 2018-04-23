# -*- coding:utf-8 -*-
import json
jsoncode={
    "晋J": "14230000",
    "晋K": "14240000",
    "晋H": "14220000",
    "晋L": "14260000",
    "晋M": "14270000",
    "晋B": "14020000",
    "晋C": "14030000",
    "晋A": "14010000",
    "晋F": "14060000",
    "晋D": "14040000",
    "晋E": "14050000",
    "川Z": "51380000",
    "川Y": "51370000",
    "川X": "51160000",
    "川S": "51300000",
    "川R": "51130000",
    "川Q": "51250000",
    "川W": "51340000",
    "川V": "51330000",
    "川U": "51320000",
    "川T": "51310000",
    "川K": "51100000",
    "川J": "51090000",
    "川H": "51080000",
    "川M": "51390000",
    "川L": "51110000",
    "川C": "51030000",
    "川B": "51070000",
    "川A": "51010000",
    "川F": "51060000",
    "川E": "51050000",
    "川D": "51040000",
    "京": "11000000",
    "鲁J": "37090000",
    "鲁K": "37100000",
    "鲁H": "37080000",
    "鲁N": "37140000",
    "鲁L": "37110000",
    "鲁M": "37230000",
    "鲁B": "37020000",
    "鲁C": "37030000",
    "鲁A": "37010000",
    "鲁F": "37060000",
    "鲁G": "37070000",
    "鲁D": "37040000",
    "鲁E": "37050000",
    "鲁R": "37290000",
    "鲁S": "37120000",
    "鲁P": "37150000",
    "鲁Q": "37130000",
    "贵G": "52250000",
    "贵F": "52240000",
    "贵E": "52230000",
    "贵D": "52220000",
    "津": "12000000",
    "贵B": "52020000",
    "贵A": "52010000",
    "贵J": "52270000",
    "贵H": "52260000",
    "辽H": "21080000",
    "辽K": "21100000",
    "辽J": "21090000",
    "辽M": "21120000",
    "辽L": "21110000",
    "辽N": "21130000",
    "辽A": "21010000",
    "辽C": "21030000",
    "辽B": "21020000",
    "辽E": "21050000",
    "辽D": "21040000",
    "辽G": "21070000",
    "辽F": "21060000",
    "辽P": "21140000",
    "新P": "65300000",
    "新Q": "65310000",
    "新R": "65320000",
    "新A": "65010000",
    "新B": "65230000",
    "新C": "65900000",
    "新D": "65400000",
    "新E": "65270000",
    "新F": "65410000",
    "新G": "65420000",
    "新H": "65430000",
    "新J": "65020000",
    "新K": "65210000",
    "新L": "65220000",
    "新M": "65280000",
    "新N": "65290000",
    "桂P": "45060000",
    "冀T": "13110000",
    "冀R": "13100000",
    "冀E": "13050000",
    "冀D": "13040000",
    "冀G": "13070000",
    "冀F": "13060000",
    "冀A": "13010000",
    "冀C": "13030000",
    "冀B": "13020000",
    "冀H": "13080000",
    "冀J": "13090000",
    "渝": "50000000",
    "桂E": "45050000",
    "桂D": "45040000",
    "桂G": "45130000",
    "桂F": "45140000",
    "桂A": "45010000",
    "宁B": "64020000",
    "宁C": "64030000",
    "宁A": "64010000",
    "桂C": "45030000",
    "宁D": "64040000",
    "宁E": "64050000",
    "甘B": "62020000",
    "甘M": "62280000",
    "桂L": "45260000",
    "甘N": "62290000",
    "桂K": "45090000",
    "桂J": "45110000",
    "赣H": "36020000",
    "赣J": "36030000",
    "赣K": "36050000",
    "赣L": "36060000",
    "赣A": "36010000",
    "赣B": "36070000",
    "赣C": "36220000",
    "赣D": "36240000",
    "赣E": "36230000",
    "赣F": "36250000",
    "赣G": "36040000",
    "鄂Q": "42280000",
    "沪": "31000000",
    "鄂S": "42130000",
    "鄂R": "42920000",
    "鄂H": "42080000",
    "鄂K": "42090000",
    "鄂J": "42110000",
    "鄂M": "42900000",
    "鄂L": "42120000",
    "鄂N": "42300000",
    "鄂A": "42300000",
    "鄂C": "42030000",
    "鄂B": "42020000",
    "鄂E": "42050000",
    "鄂G": "42070000",
    "鄂F": "42060000",
    "藏E": "54240000",
    "豫P": "41270000",
    "豫Q": "41280000",
    "豫R": "41130000",
    "豫S": "41150000",
    "豫D": "41040000",
    "豫E": "41050000",
    "豫F": "41060000",
    "豫G": "41070000",
    "豫A": "41010000",
    "豫B": "41020000",
    "豫C": "41030000",
    "豫L": "41110000",
    "豫M": "41120000",
    "豫N": "41140000",
    "豫H": "41080000",
    "豫J": "41090000",
    "豫K": "41100000",
    "蒙A": "15010000",
    "蒙C": "15030000",
    "蒙B": "15020000",
    "蒙E": "15060000",
    "蒙D": "15040000",
    "蒙G": "15230000",
    "蒙F": "15220000",
    "蒙H": "15250000",
    "蒙K": "15270000",
    "蒙J": "15260000",
    "蒙M": "15290000",
    "蒙L": "15280000",
    "浙E": "33050000",
    "黑P": "23270000",
    "黑G": "23030000",
    "黑F": "23070000",
    "黑E": "23060000",
    "黑D": "23080000",
    "黑C": "23100000",
    "黑B": "23020000",
    "黑A": "23010000",
    "黑N": "23110000",
    "黑M": "23230000",
    "黑K": "23090000",
    "黑J": "23050000",
    "黑H": "23040000",
    "藏B": "54210000",
    "粤V": "44520000",
    "藏A": "54010000",
    "藏F": "54250000",
    "粤R": "44180000",
    "浙A": "33010000",
    "浙B": "33020000",
    "浙C": "33030000",
    "浙D": "33060000",
    "藏D": "54230000",
    "浙F": "33040000",
    "浙G": "33120000",
    "浙H": "33080000",
    "浙J": "33100000",
    "浙K": "33250000",
    "浙L": "33090000",
    "云Q": "53330000",
    "云P": "53320000",
    "云S": "53350000",
    "云R": "53340000",
    "云M": "53300000",
    "云L": "53290000",
    "云H": "53260000",
    "云K": "53280000",
    "云J": "53270000",
    "云E": "53230000",
    "云D": "53030000",
    "云G": "53250000",
    "云F": "53040000",
    "云A": "53010000",
    "云C": "53210000",
    "贵C": "52030000",
    "湘N": "43120000",
    "湘M": "43110000",
    "湘L": "43100000",
    "湘K": "43250000",
    "湘J": "43070000",
    "湘H": "43090000",
    "湘G": "43080000",
    "湘F": "43060000",
    "湘E": "43050000",
    "湘D": "43040000",
    "湘C": "43030000",
    "湘B": "43020000",
    "湘A": "43010000",
    "湘U": "43310000",
    "粤W": "44530000",
    "藏C": "54220000",
    "粤U": "44510000",
    "粤T": "44200000",
    "粤S": "44190000",
    "藏G": "54260000",
    "粤Q": "44170000",
    "粤P": "44160000",
    "粤X": "44710000",
    "粤G": "44080000",
    "粤F": "44020000",
    "粤E": "44060000",
    "粤D": "44050000",
    "粤C": "44040000",
    "粤B": "44030000",
    "粤A": "44010000",
    "粤N": "44150000",
    "粤M": "44140000",
    "粤L": "44130000",
    "粤K": "44090000",
    "粤J": "44070000",
    "粤H": "44120000",
    "闽J": "35090000",
    "闽H": "35070000",
    "闽G": "35040000",
    "闽F": "35080000",
    "闽E": "35060000",
    "闽D": "35020000",
    "闽C": "35150000",
    "闽B": "35030000",
    "闽A": "35110000",
    "鄂P": "42910000",
    "苏F": "32060000",
    "苏G": "32070000",
    "苏D": "32040000",
    "苏E": "32050000",
    "苏B": "32020000",
    "苏C": "32030000",
    "苏A": "32010000",
    "苏N": "32130000",
    "苏L": "32110000",
    "苏M": "32120000",
    "苏J": "32090000",
    "苏K": "32100000",
    "苏H": "32080000",
    "陕H": "61250000",
    "陕K": "61270000",
    "陕J": "61060000",
    "陕E": "61050000",
    "陕D": "61040000",
    "陕G": "61240000",
    "陕F": "61070000",
    "陕A": "61010000",
    "陕C": "61030000",
    "陕B": "61020000",
    "青D": "63230000",
    "青E": "63250000",
    "青F": "63260000",
    "青G": "63270000",
    "青A": "63010000",
    "青B": "63210000",
    "青C": "63220000",
    "青H": "63290000",
    "皖Q": "34260000",
    "皖P": "34250000",
    "皖S": "34160000",
    "皖R": "34290000",
    "皖E": "34050000",
    "皖D": "34040000",
    "皖G": "34070000",
    "皖F": "34060000",
    "皖A": "34010000",
    "皖C": "34030000",
    "皖B": "34020000",
    "皖M": "34110000",
    "皖L": "34220000",
    "皖N": "34240000",
    "皖H": "34080000",
    "皖K": "34120000",
    "皖J": "34100000",
    "吉H": "22240000",
    "吉J": "22070000",
    "吉A": "22010000",
    "吉B": "22020000",
    "吉C": "22030000",
    "吉D": "22040000",
    "吉E": "22050000",
    "吉F": "22060000",
    "吉G": "22080000",
    "甘P": "62300000",
    "桂R": "45080000",
    "甘E": "62050000",
    "甘D": "62040000",
    "甘G": "62220000",
    "甘F": "62210000",
    "甘A": "62010000",
    "甘C": "62030000",
    "桂B": "45020000",
    "桂M": "45270000",
    "甘L": "62270000",
    "桂N": "45070000",
    "甘H": "62230000",
    "甘K": "62260000",
    "甘J": "62240000",
    "琼E": "46902900",
    "琼D": "46903500",
    "琼F": "46900300",
    "琼A": "46010000",
    "琼C": "46900600",
    "琼B": "46020000"
}
def get_citycode(liceseNo):
    return jsoncode.get(liceseNo[0:2].encode('utf-8'),"32010000")
