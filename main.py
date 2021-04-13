import spider.baiduTop as s

def main():
    spider = s.BaiduTop()
    spider.getTopics()
    spider.getDetails()
    print(spider.topics)
    print(spider.values)
    print(spider.urls)

if __name__ == '__main__':
    main()