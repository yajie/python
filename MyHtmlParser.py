from sgmllib import SGMLParser


class URLParser(SGMLParser):
	urlList=[]
	def reset(self):
		self.is_a = ""
		self.name = []
		SGMLParser.reset(self)

	def start_a(self,attrs):
		self.is_a = 1
		href = [ v for k,v in attrs if k == 'href']
		if href:
			URLParser.urlList.extend(href)

	def handle_data(self,data):
		if self.is_a:
			self.name.append(data)

if __name__ == '__main__':	
	fileHandle  = open('G:\py-dev\url.html','r')
	urlParser = URLParser()

	urlParser.feed(fileHandle.read())
	print urlParser.urlList

	fileHandle.close()
