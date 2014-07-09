####PYTHON
import HTMLParser
import urlparse

import urllib
import urllib2
import cookielib

import string
import re

### Login Url
hostUrl = 'http://www.zhihu.com/login'

### HTTP Header
headers = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',  
        'Referer' : 'www.zhihu.com'
}

### Login Post Data
postData ={
	'email':'your_account_email',
	'password':'your_account_password'
}
postData = urllib.urlencode(postData)

cj = cookielib.LWPCookieJar()
cookieInst = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookieInst, urllib2.HTTPHandler)
urllib2.install_opener(opener)  

request = urllib2.Request(hostUrl, postData, headers)
hostResp = urllib2.urlopen(request)
### DEBUG INFO
#print hostResp.info()

### POST URL
postUrl = 'http://www.zhihu.com/question/24382487'

request = urllib2.Request(postUrl)

resp = urllib2.urlopen(request)
#print resp.read()
htmlFile = open('zhihu.txt','w')
htmlFile.write(resp.read())
htmlFile.close()





