import os
import time
import json

import spider.web as web
import spider.tools as tools


class BaiduTop():
    def __init__(self):
        self.topics = []
        self.values = []
        self.urls = []
        # self.details = []

    def getTopics(self):
        soup = web.getSoup('gbk', 'http://top.baidu.com/buzz?b=1&fr=topindex')

        for item in soup.find_all(class_='keyword'):
            self.topics.append(item.a.get_text())
            self.urls.append(item.a['href'])

        for item in soup.find_all(class_='last')[2:]:
            self.values.append(item.span.get_text())

    def getDetails(self):
        for i in range(len(self.urls)):
            self.getDetail(i)

    def getDetail(self, i):
        soup = web.getSoup('utf-8', self.urls[i])
        detail = {'timeline': [], 'video': [], 'info': []}
        try:
            headlines = {}
            headlines['title'] = tools.formatString(soup.find(class_='c-span-last').span.a.get_text())
            headlines['desc'] = tools.formatString(soup.find(class_='c-span-last').p.get_text())
            for item in soup.find_all(class_='timeline-item_URKTk'):
                timeline = {}
                timeline['time'] = item.span.get_text()
                timeline['title'] = item.a.get_text()
                detail['timeline'].append(timeline)
            for item in soup.find_all(class_='op-short-video-pc-title-new'):
                video = {}
                video['title'] = tools.formatString(item.get_text())
                detail['video'].append(video)
            for item in soup.find_all(class_='op_sp_realtime_new_overflow'):
                info = {}
                info['title'] = tools.formatString(item.find(class_='op_sp_realtime_group_title_new').a.get_text())
                info['desc'] = tools.formatString(item.find(class_='op_sp_realtime_new_subabs').get_text())
                detail['info'].append(info)
        except Exception as e:
            # Anti Cheating
            if soup.title.get_text() == '百度安全验证':
                print('Anti cheating ======================>')
                print(self.topics[i])
                print(self.urls[i])
                print('<====================================')
                i = i-1
                time.sleep(30)
            else:
                print('catch error ========================>')
                print(e)
                # print(soup)
                print(self.topics[i])
                print(self.urls[i])
                print('<====================================')

        # self.details.append(detail)
        self.save(i, detail)

    def save(self, i, detail):
        t = time.localtime()
        path_list = ['./data', time.strftime("%Y", t), time.strftime("%m-%d", t), time.strftime("%H", t)]
        path = '/'.join(path_list)
        if not os.path.exists(path):
            os.makedirs(path)
        fo = open(path+'/'+self.values[i]+'_'+self.topics[i], "a")
        fo.write(json.dumps(detail, ensure_ascii=False)+"\n")
        fo.close()
