# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
import urllib2, logging, csv, re, json, sys

url = sys.argv[1]
logging.info(url)
cc = urllib2.urlopen(url)
csv_read = csv.reader(cc)
ss = json.load(cc)

#print sys.argv[1],':',type(sys.argv[1])

ans = 0
cnt = 0
ym = int(sys.argv[4])
if ym < 1000:
	ym = ym * 100
#print ym,':',type(ym)
for i in ss:
	arg1 = sys.argv[2].decode('utf-8')
	if i[u'鄉鎮市區'] == arg1:
		strchk = i[u'土地區段位置或建物區門牌']
		arg2 = sys.argv[3].decode('utf-8')
		chk = strchk.find(arg2)
		ymchk = i[u'交易年月']
		if ymchk >= ym:
			if chk >= 0:
				#print i[u'總價元'],':',type(i[u'總價元'])
				ans += i[u'總價元']
				cnt += 1
print int(ans / cnt)






	#for ii in i:
	#	if i == "文":
	#	print ii
	#print i[u'鄉鎮市區']
