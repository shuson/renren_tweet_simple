#--------------------------------------
# Module Name:       renren_tweet
#
# Author:            shuson
#--------------------------------------
import sgmllib
import sys, urllib, urllib2,cookielib
import datetime,time
class Renren_tweet(sgmllib.SGMLParser):
  def __init__ (self,username,password):
		self.username = username
		self.password = password
		self.domain="renren.com"
		self.homeUrl="http://www.renren.com/223538568"

		sgmllib.SGMLParser.__init__(self)

		try:
			self.cookieJar = cookielib.CookieJar()
			self.cookieProc = urllib2.HTTPCookieProcessor(self.cookieJar)
			self.opener = urllib2.build_opener(self.cookieProc)
			urllib2.install_opener(self.opener)
		except Exception,e:
			print e
	def login (self):
		print "login...."
		url1 = 'http://www.renren.com/PLogin.do'
		params ={'email':self.username,'password':self.password,'domain':self.domain,'homeUrl':self.homeUrl}
		req = urllib2.Request(url1,urllib.urlencode(params))
		if self.opener.open(req).geturl()=='http://www.renren.com/223538568':
			print 'Successfully login'

		self.infocontent = urllib2.urlopen(req).read()
		#self.infocontent = self.opener.open(req).readlines()
		idPosition=self.infocontent.index("'id':'")
		self.id=self.infocontent[idPosition+6:idPosition+15]
		tokPosition=self.infocontent.index("get_check:'")
		self.tok=self.infocontent[tokPosition+11:tokPosition+21]
		rtkPosition=self.infocontent.index("get_check_x:'")
		self.rtk=self.infocontent[rtkPosition+13:rtkPosition+21]
	
	def postTweet (self,content):
		url2 = "http://shell.renren.com/"+self.id+'/status'
		params = {'content':content,'hostid':self.id,'requestToken':self.tok,'_rtk':self.rtk,'channel':'renren'}
		req2 = urllib2.Request(url2,urllib.urlencode(params))
		self.tweet = urllib2.urlopen(req2).read()
		print self.tweet

username ='xxxx@xxx.com'
password = 'password'
tweet = Renren_tweet(username,password)
tweet.login()
tweet.postTweet("Does it work?")
		
