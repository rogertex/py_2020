from urllib import request

#断点调试
class Spider():
    url = 'http://www.baidu.com'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        a=2
        
    def __analysis(self,htmls):
        pass
    def go(self):
        self.__fetch_content()
        self.__analysis(htmls)




spider=Spider()
spider.go()
