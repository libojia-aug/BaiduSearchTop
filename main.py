import schedule
import time

import spider.baiduTop as s


def main():
    start = time.time()
    print('\nBegin at '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
    spider = s.BaiduTop()
    spider.getTopics()
    spider.getDetails()
    print('Get '+str(len(spider.topics))+' Topics')
    print('Topics list: '+'|'.join(spider.topics))

    end = time.time()
    print('End at '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)))
    print('Use '+str(end-start)+' Seconds\n')
    # print(spider.values)
    # print(spider.urls)


if __name__ == '__main__':
    # schedule.every(10).seconds.do(main)
    schedule.every(2).hour.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
    # main()
