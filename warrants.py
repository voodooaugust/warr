from pandas import *
from datetime import datetime


class warrants():
	def __init__(self):
		self.setPara()
		counter = 0
	def getWarrantsFiles(self):
		distname = './wdata/' + ''.join(self.para) + str(self.counter) + '.csv'
		urllib.urlretrieve(quaryURL(self.para),distname)		
	def setPara(self):
		para = raw_input('enter sname, ucode, wtype :')
		self.para = tuple(str(x).upper() for x in para.split())

	def quaryURL(self,para):
		link = 'http://warrants.ubs.com/ch/warrants/search_c.xls?\
sname=%s&ucode=%s&wtype=%s\
&mtype=0&iv1=&iv2=&ptype=0&s1=&s2=&egear=0\
&osp1=&osp2=&d1=&d2=&m1=0&m2=0&cr1=&cr2=&' % para
		print link
		return link

w = warrants()
df = read_csv(w.quaryURL())
print df