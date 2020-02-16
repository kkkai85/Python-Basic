# python 有兩個關於時間的模組，一個time 一個datetime
import time
# 取得現在時間
localtime = time.localtime()
print(localtime)
print(localtime.tm_mday)

# 格式化時間，asctime()
# 格式為"%a %b %d %H:%M:%S %Y"
nowtime = time.asctime(localtime)
print(nowtime)

# 格式化時間，strftime()
# 格式可為"%Y-%m-%d %H:%M:%S"，或是"%a %b %d %H:%M:%S %Y"
nowtime2 = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(nowtime2)
nowtime3 = time.strftime("%a %b %d %H:%M:%S %Y", localtime)
print(nowtime3)
# 格式化後時間均為字串使用

mytime = "2019-01-11 15:17:56"
# strptime() 根據指定格式把一個時間字串解析為時間元組
time = time.strptime(mytime, "%Y-%m-%d %H:%M:%S")
print(time)
print(time.tm_hour)

import datetime

nowtime = datetime.datetime.now()
print ("今天的日期時間是 %s" % nowtime)
print ("ISO格式的日期時間是 %s" % nowtime.isoformat() )
print ("年份是 %s" %nowtime.year)
print ("月份是 %s" %nowtime.month)
print ("日期是  %s" %nowtime.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (nowtime.day, nowtime.month, nowtime.year) )
print ("小時是 %s" %nowtime.hour)
print ("分鐘是 %s" %nowtime.minute)
print ("秒是  %s" %nowtime.second)



tStart = time.time()

for i in range(1, 10):
	print(i)

tEnd = time.time()

a = (tEnd - tStart)
print(a)