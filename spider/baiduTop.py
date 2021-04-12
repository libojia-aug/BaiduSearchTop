import requests
from bs4 import BeautifulSoup

import spider.spider as s

class BaiduTop(s.Spider):
    def __init__(self):
        s.Spider.__init__(self)

    def getTopics(self):
        response = requests.get('http://top.baidu.com/buzz?b=1&fr=topindex')
        response.encoding = 'gbk'
        soup = BeautifulSoup(response.text, 'html.parser')
        

        for item in soup.find_all(class_='keyword'):
            self.topics_list.append(item.a.get_text())
            self.urls_list.append(item.a['href'])
            # print(item.a['href'])

        for item in soup.find_all(class_='last')[2:]:
            self.values_list.append(int(item.span.get_text()))
        
    def getDetails(self):
    	pass